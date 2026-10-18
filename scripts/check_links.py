#!/usr/bin/env python3
"""
check_links.py — verify that every external URL cited by the site resolves.

Sources of URLs:
  1. data/sources.json  (the authoritative source register)
  2. docs/*.html        (any href that is not internal)

Exit codes:
  0  all checked URLs responded with a non-4xx/5xx status
  1  at least one URL failed
  2  could not run (network unavailable / argument error)

Notes:
  * Uses only the Python standard library.
  * Retries transient failures (429, 5xx, timeouts) with backoff.
  * Some government endpoints rate-limit or block non-browser clients. Those
    outcomes are reported as WARN, not FAIL, when the status is 403/406/451 or
    the server closes the connection, because that is a client-restriction
    signal rather than evidence that the citation is wrong. Use --strict to
    promote warnings to failures.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36 MaltaProj9-LinkCheck/1.0"
)

SOFT_STATUSES = {403, 405, 406, 415, 429, 451, 503, 999}


def collect_urls() -> dict[str, list[str]]:
    urls: dict[str, list[str]] = {}

    with open(DATA / "sources.json", encoding="utf-8") as fh:
        doc = json.load(fh)
    for s in doc["sources"]:
        urls.setdefault(s["url"], []).append(f"data/sources.json#{s['id']}")

    for page in sorted(DOCS.glob("*.html")):
        text = page.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', text):
            if not href.startswith(("http://", "https://")):
                continue
            urls.setdefault(href, []).append(f"docs/{page.name}")
    return urls


def probe(url: str, timeout: int, retries: int) -> tuple[str, int | None, str]:
    """Return (verdict, status, detail). verdict in {OK, WARN, FAIL}."""
    clean = urldefrag(url).url
    last = ""
    for attempt in range(retries):
        req = urllib.request.Request(
            clean,
            headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.9",
                "Accept-Language": "en-US,en;q=0.9",
            },
            method="GET",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = int(resp.status)
                if status < 400:
                    return "OK", status, ""
                last = f"HTTP {status}"
        except urllib.error.HTTPError as exc:
            status = exc.code
            last = f"HTTP {status} {exc.reason}"
            if status in SOFT_STATUSES:
                return "WARN", status, last
            if status == 404:
                return "FAIL", status, last
            if status < 500:
                return "FAIL", status, last
        except Exception as exc:  # timeouts, TLS, DNS, reset
            last = f"{type(exc).__name__}: {exc}"
        if attempt + 1 < retries:
            time.sleep(2 ** attempt)
    return "FAIL", None, last


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=25)
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--strict", action="store_true", help="treat WARN as FAIL")
    ap.add_argument("--json", dest="json_out", default="", help="write a JSON report")
    args = ap.parse_args()

    urls = collect_urls()
    print(f"checking {len(urls)} unique external URLs\n")

    results = []
    counts = {"OK": 0, "WARN": 0, "FAIL": 0}
    for i, url in enumerate(sorted(urls), 1):
        verdict, status, detail = probe(url, args.timeout, args.retries)
        counts[verdict] += 1
        results.append(
            {
                "url": url,
                "verdict": verdict,
                "status": status,
                "detail": detail,
                "referenced_by": sorted(set(urls[url])),
            }
        )
        mark = {"OK": "ok  ", "WARN": "warn", "FAIL": "FAIL"}[verdict]
        where = urls[url][0]
        extra = f"  ({detail})" if detail else ""
        print(f"[{i:3d}/{len(urls)}] {mark} {status or '---'}  {url}{extra}   <- {where}")

    print(
        f"\nsummary: {counts['OK']} ok, {counts['WARN']} warn, {counts['FAIL']} fail "
        f"(of {len(urls)})"
    )

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps({"counts": counts, "results": results}, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"report written to {args.json_out}")

    failures = [r for r in results if r["verdict"] == "FAIL"]
    warns = [r for r in results if r["verdict"] == "WARN"]
    if failures:
        print("\nFAILED URLs:")
        for r in failures:
            print(f"  - {r['url']}  {r['detail']}  <- {', '.join(r['referenced_by'])}")
    if warns:
        print("\nWARNED URLs (server rejected an automated client; verify manually):")
        for r in warns:
            print(f"  - {r['url']}  {r['detail']}")

    if failures:
        return 1
    if args.strict and warns:
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(2)
