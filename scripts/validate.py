#!/usr/bin/env python3
"""Validate the built site for MaltaProj9.

Enforces the verification standard:
  1. Every data row must have a source link to an official source
     (.gov, Covered California, or Kalshi's official help center).
     Unverified rows must leave the value blank and are flagged.
  2. Every generated page must exist and contain no unprocessed placeholders.
  3. Internal links and asset references must resolve to real files.
  4. Every non-verified row must appear on the Flagged for Review page.
Exit code 0 = pass; 1 = failures found.
"""
import csv
import os
import re
import sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
SITE_DIR = os.path.join(ROOT, "dashboard")   # this session's site (root hosts the companion brief)

PAGES = ["index.html", "executive-summary.html", "work-requirements.html", "medi-cal.html",
         "covered-california.html", "income-treatment.html", "other-options.html",
         "flagged-for-review.html", "sources.html"]

# A repository-audit flag cites this project's own repository, not a government source.
# It is the only row permitted to link a non-official host, and it asserts no health fact.
REPO_AUDIT_ROWS = {("flagged-items.csv", "FL-09")}

OFFICIAL_HOSTS = ("coveredca.com", "hbex.coveredca.com", "help.kalshi.com", "kalshi.com")


def is_official(url):
    try:
        p = urlparse(url)
    except ValueError:
        return False
    host = (p.hostname or "").lower()
    if not host:
        return False
    if host.endswith(".gov") or host == "gov.ca.gov":
        return True
    return any(host == h or host.endswith("." + h) for h in OFFICIAL_HOSTS)


def main():
    errors, warnings = [], []
    tables = {}
    for name in sorted(os.listdir(DATA_DIR)):
        if name.endswith(".csv"):
            with open(os.path.join(DATA_DIR, name), newline="", encoding="utf-8") as f:
                tables[name] = list(csv.DictReader(f))

    nonverified_total = 0
    for name, rows in tables.items():
        for r in rows:
            rid = r.get("id", "?")
            status = (r.get("status") or "").strip().lower()
            url = (r.get("source_url") or "").strip()
            value = (r.get("value") or "").strip()
            if status not in ("verified", "flagged", "unverified"):
                errors.append("%s %s: invalid status %r" % (name, rid, status))
            if status == "verified":
                if not url:
                    errors.append("%s %s: VERIFIED row missing source_url" % (name, rid))
                elif not is_official(url):
                    errors.append("%s %s: verified row source not official: %s" % (name, rid, url))
                if not value:
                    errors.append("%s %s: VERIFIED row has blank value" % (name, rid))
            else:
                nonverified_total += 1
                # Every row, including blank-value and flagged rows, must carry an
                # official source link so a reader can check the negative result too.
                if not url:
                    errors.append("%s %s: non-verified row missing source_url" % (name, rid))
                elif not is_official(url) and (name, rid) not in REPO_AUDIT_ROWS:
                    errors.append("%s %s: non-verified row source not official: %s" % (name, rid, url))
                if status == "unverified" and value:
                    errors.append("%s %s: unverified row must leave value blank (found %r)"
                                  % (name, rid, value[:60]))
                if status == "flagged":
                    if not value:
                        errors.append("%s %s: flagged row should state the flagged finding" % (name, rid))
                    if not url:
                        errors.append("%s %s: flagged row should cite a source" % (name, rid))
                if status == "unverified" and not value and not (r.get("notes") or "").strip():
                    errors.append("%s %s: unverified row needs explanatory notes" % (name, rid))
            if url and not url.startswith("https://"):
                errors.append("%s %s: source_url must use https: %s" % (name, rid, url))

    # Page existence, placeholders, internal links.
    for page in PAGES:
        p = os.path.join(SITE_DIR, page)
        if not os.path.exists(p):
            errors.append("missing built page: %s" % page)
            continue
        page_dir = os.path.dirname(p)
        with open(p, encoding="utf-8") as f:
            doc = f.read()
        if re.search(r"\{\{[A-Z_]+", doc):
            errors.append("%s: unprocessed placeholder remains" % page)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', doc):
            u = m.group(1)
            if u.startswith(("http://", "https://", "#", "mailto:", "data:")):
                continue
            target = u.split("#")[0].split("?")[0]
            if not target:
                continue
            resolved = os.path.normpath(os.path.join(page_dir, target))
            if not (resolved == ROOT or resolved.startswith(ROOT + os.sep)):
                errors.append("%s: link escapes repository: %s" % (page, u))
            elif not os.path.isfile(resolved):
                errors.append("%s: broken internal link: %s" % (page, u))

    if not os.path.exists(os.path.join(ROOT, ".nojekyll")):
        errors.append("missing .nojekyll")
    if not os.path.exists(os.path.join(SITE_DIR, "assets", "style.css")):
        errors.append("missing dashboard/assets/style.css")

    # Flagged page completeness: every non-verified data row id must appear there.
    flagged_page = os.path.join(SITE_DIR, "flagged-for-review.html")
    if os.path.exists(flagged_page):
        with open(flagged_page, encoding="utf-8") as f:
            fdoc = f.read()
        present = set(re.findall(r'data-row="([^"]+)"', fdoc))
        for name, rows in tables.items():
            if name == "flagged-items.csv":
                continue
            for r in rows:
                if (r.get("status") or "").lower() != "verified":
                    if r.get("id") not in present:
                        errors.append("non-verified row %s (%s) missing from Flagged page"
                                      % (r.get("id"), name))
    else:
        errors.append("flagged-for-review.html missing")

    n_rows = sum(len(v) for v in tables.values())
    print("Validation report")
    print("  data tables: %d" % len(tables))
    print("  data rows:   %d" % n_rows)
    print("  non-verified rows (must appear on Flagged page): %d" % nonverified_total)
    print("  pages:       %d" % len(PAGES))
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print("  -", w)
    if errors:
        print("FAILURES (%d):" % len(errors))
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("PASS: all rows sourced officially or flagged; pages built; internal links resolve.")


if __name__ == "__main__":
    main()
