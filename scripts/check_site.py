#!/usr/bin/env python3
"""Dependency-free checks for local navigation and sourced findings tables."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_HOSTS = {
    "congress.gov", "cms.gov", "dhcs.ca.gov", "coveredca.com",
    "healthcare.gov", "irs.gov", "benefitscal.com",
}


class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.rows: list[list[str]] = []
        self.current_row: list[str] | None = None
        self.row_has_data = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(str(attributes["id"]))
        if tag == "a" and attributes.get("href") is not None:
            href = str(attributes["href"])
            self.links.append(href)
            if self.current_row is not None:
                self.current_row.append(href)
        if tag == "tr":
            self.current_row = []
            self.row_has_data = False
        elif tag == "td" and self.current_row is not None:
            self.row_has_data = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "tr" and self.current_row is not None:
            if self.row_has_data:
                self.rows.append(self.current_row)
            self.current_row = None
            self.row_has_data = False


def official_url(href: str) -> bool:
    parsed = urlparse(href)
    if parsed.scheme != "https" or not parsed.hostname:
        return False
    host = parsed.hostname.lower().removeprefix("www.")
    return any(host == suffix or host.endswith("." + suffix) for suffix in OFFICIAL_HOSTS)


def main() -> int:
    errors: list[str] = []
    pages = sorted(ROOT.glob("*.html"))
    if not pages:
        errors.append("No top-level HTML pages found.")

    for page in pages:
        parser = AuditParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for href in parser.links:
            parsed = urlparse(href)
            if parsed.scheme or href.startswith("//"):
                continue
            target_name = unquote(parsed.path)
            target = (page.parent / target_name).resolve() if target_name else page.resolve()
            if ROOT.resolve() not in target.parents and target != ROOT.resolve():
                errors.append(f"{page.name}: link escapes repository: {href}")
                continue
            if not target.exists() or not target.is_file():
                errors.append(f"{page.name}: broken local link: {href}")
                continue
            if parsed.fragment and target.suffix.lower() == ".html":
                target_parser = AuditParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in target_parser.ids:
                    errors.append(f"{page.name}: missing fragment target in {target.name}: #{parsed.fragment}")

        for row_number, row_links in enumerate(parser.rows, start=1):
            if not any(official_url(link) for link in row_links):
                errors.append(f"{page.name}: table data row {row_number} lacks an HTTPS official-source link.")

    css = ROOT / "assets" / "site.css"
    if not css.is_file():
        errors.append("Missing assets/site.css")

    if errors:
        print("Site checks FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print(f"Site checks passed: {len(pages)} HTML pages; local links/fragments resolve; all data rows have official HTTPS sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
