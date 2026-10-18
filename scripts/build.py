#!/usr/bin/env python3
"""Build the static GitHub Pages site for MaltaProj9.

Reads table data from data/*.csv (single source of truth) and page templates
from site_src/*.html, then writes the final pages to the repository root
(where GitHub Pages serves them from the main branch root).

Every table row carries a source link; the build renders statuses as badges.
Run scripts/validate.py afterwards to enforce the verification standard.
"""
import csv
import html
import os
import re
import sys
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
SRC_DIR = os.path.join(ROOT, "site_src")
OUT_DIR = os.path.join(ROOT, "dashboard")   # published at /dashboard/ (root hosts the companion brief)
ASSETS_SRC = os.path.join(ROOT, "assets", "style.css")
SNAPSHOT = "2026-10-18"

PAGES = OrderedDict([
    ("index.html", "Home"),
    ("executive-summary.html", "Executive Summary"),
    ("work-requirements.html", "Work Requirements"),
    ("medi-cal.html", "Medi-Cal"),
    ("covered-california.html", "Covered California"),
    ("income-treatment.html", "Income &amp; MAGI"),
    ("other-options.html", "Other Options"),
    ("flagged-for-review.html", "Flagged for Review"),
    ("sources.html", "Sources"),
])

# Which data tables belong to which page (for index cards and stats).
PAGE_TABLES = {
    "executive-summary.html": ["options-summary.csv"],
    "work-requirements.html": ["work-requirements-law.csv", "work-requirement-exemptions.csv", "california-implementation.csv"],
    "medi-cal.html": ["medi-cal-eligibility.csv"],
    "covered-california.html": ["covered-california.csv"],
    "income-treatment.html": ["income-treatment.csv"],
    "other-options.html": ["other-programs.csv"],
    "flagged-for-review.html": ["flagged-items.csv"],
}

PAGE_BLURBS = {
    "executive-summary.html": "Options, decision paths, the new law in plain English, and an action checklist.",
    "work-requirements.html": "The new federal work and community engagement law: hours, exemptions, the $580 income standard, and California's rollout.",
    "medi-cal.html": "Eligibility (138% FPL), MAGI rules, no asset test, how to apply, and what changes in 2027.",
    "covered-california.html": "Premium tax credits, the expired enhanced credits, state subsidies, cost-sharing reductions, and enrollment dates.",
    "income-treatment.html": "How Kalshi trading, rental income, and interest are counted for MAGI and for the work requirement.",
    "other-options.html": "EMTALA, hospital charity care, the short-term plan ban, COBRA, Medicare, and help resources.",
    "flagged-for-review.html": "Every unverified value and irregularity found, with sources, for manual review.",
    "sources.html": "The full source list and the verification methodology.",
}

STATUS_LABEL = {"verified": "Verified", "flagged": "Flagged", "unverified": "Unverified"}
COL_LABELS = [("item", "Item"), ("value", "Value / Rule"), ("detail", "Details"),
              ("status", "Status"), ("source", "Source"), ("notes", "Notes")]


def load_csv(name):
    path = os.path.join(DATA_DIR, name)
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def all_tables():
    tables = OrderedDict()
    for name in sorted(os.listdir(DATA_DIR)):
        if name.endswith(".csv"):
            tables[name] = load_csv(name)
    return tables


def esc(v):
    return html.escape(v or "", quote=True)


def status_badge(status):
    s = (status or "").strip().lower()
    cls = "b-verified" if s == "verified" else ("b-flagged" if s == "flagged" else "b-unverified")
    return '<span class="badge %s">%s</span>' % (cls, esc(STATUS_LABEL.get(s, s or "?")))


def render_source(row):
    url = (row.get("source_url") or "").strip()
    name = (row.get("source_name") or "").strip()
    if url:
        return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc(url), esc(name or url))
    return '<span class="blank">%s</span>' % esc(name) if name else '<span class="blank">&mdash;</span>'


def render_table(rows, caption=None):
    out = ['<div class="table-wrap">', "<table>"]
    if caption:
        out.append("<caption>%s</caption>" % esc(caption))
    out.append("<thead><tr>")
    for _, label in COL_LABELS:
        out.append("<th scope=\"col\">%s</th>" % label)
    out.append("</tr></thead><tbody>")
    for row in rows:
        cells = {
            "item": esc(row.get("item", "")),
            "value": ('<span class="blank">&mdash; blank (see notes) &mdash;</span>'
                      if not (row.get("value") or "").strip() else esc(row["value"])),
            "detail": esc(row.get("detail", "")),
            "status": status_badge(row.get("status")),
            "source": render_source(row),
            "notes": esc(row.get("notes", "")),
        }
        out.append('<tr data-row="%s">' % esc(row.get("id", "")))
        for key, _ in COL_LABELS:
            out.append("<td>%s</td>" % cells[key])
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_nav(current):
    links = []
    for fname, title in PAGES.items():
        cls = ' class="active" aria-current="page"' if fname == current else ""
        links.append('<a href="%s"%s>%s</a>' % (fname, cls, title))
    return '<nav class="topnav" aria-label="Primary">%s</nav>' % "".join(links)


def table_counts(tables):
    counts = {}
    for name, rows in tables.items():
        counts[name] = {
            "rows": len(rows),
            "verified": sum(1 for r in rows if (r.get("status") or "").lower() == "verified"),
            "flagged": sum(1 for r in rows if (r.get("status") or "").lower() != "verified"),
        }
    return counts


def render_cards(tables):
    counts = table_counts(tables)
    cards = []
    icons = {
        "executive-summary.html": "&#9656;", "work-requirements.html": "&#9881;",
        "medi-cal.html": "&#10010;", "covered-california.html": "&#9878;",
        "income-treatment.html": "&#8721;", "other-options.html": "&#9873;",
        "flagged-for-review.html": "&#9888;", "sources.html": "&#128279;",
    }
    for fname, title in PAGES.items():
        if fname in ("index.html",):
            continue
        rows = verified = 0
        for t in PAGE_TABLES.get(fname, []):
            c = counts.get(t)
            if c:
                rows += c["rows"]
                verified += c["verified"]
        if fname == "sources.html":
            stat = "Full source list"
        elif rows:
            stat = "%d rows &middot; %d verified" % (rows, verified)
        else:
            stat = ""
        cards.append(
            '<a class="card" href="%s"><div class="card-top"><span class="ico">%s</span>'
            "<h3>%s</h3></div><p>%s</p><p class=\"card-stat\">%s</p></a>"
            % (fname, icons.get(fname, ""), title, PAGE_BLURBS.get(fname, ""), stat))
    return '<div class="cards">%s</div>' % "".join(cards)


def collect_sources(tables):
    seen = OrderedDict()
    for name, rows in tables.items():
        for r in rows:
            url = (r.get("source_url") or "").strip()
            nm = (r.get("source_name") or "").strip()
            if url and url not in seen:
                host = re.sub(r"^https?://([^/]+).*$", r"\1", url)
                if host.endswith(".gov") or host == "gov.ca.gov":
                    typ = "Official (government)"
                elif host.endswith("coveredca.com"):
                    typ = "Official (state marketplace)"
                elif host.endswith("kalshi.com"):
                    typ = "Official (company)"
                else:
                    typ = "Trusted secondary"
                seen[url] = (nm or url, typ)
    # Narrative-only secondary sources cited on the pages.
    extras = [
        ("Justice in Aging - Medicaid Community Engagement Requirements FAQ (Oct 2026)", "https://justiceinaging.org/medicaid-community-engagement-requirements/"),
        ("Bipartisan Policy Center - Unpacking Tax Uncertainties for Prediction Markets (Aug 2026)", "https://bipartisanpolicy.org/issue-brief/unpacking-tax-uncertainties-for-prediction-markets/"),
        ("California Health Care Foundation - H.R. 1 Work Requirement Policy at a Glance (June 2026)", "https://www.chcf.org/resource/2026/06/05/hr1-work-requirement-affect-californians-medi-cal-policy-at-a-glance/"),
        ("KFF - An Early Look at Policy Decisions as States Get Ready to Implement Work Requirements (May 2026)", "https://www.kff.org/medicaid/an-early-look-at-policy-decisions-as-states-get-ready-to-implement-work-requirements/"),
        ("CalHHS Connect webinar - How Federal Policy Changes are Impacting a Healthy California (July 2026)", "https://www.chhs.ca.gov/wp-content/uploads/2026/07/CalHHS_Connect_Webinar_2026-07-08.pdf"),
        ("CRS Report R44425 - Health Insurance Premium Tax Credit and Cost-Sharing Reductions", "https://www.congress.gov/crs-product/R44425"),
        ("Epstein Becker Green - CMS Issues Interim Final Rule on Medicaid Work Requirements (quotes the IFC activity list)", "https://www.ebglaw.com/insights/publications/cms-issues-interim-final-rule-on-medicaid-work-requirements"),
        ("San Diego County - Medi-Cal Work Requirements", "https://www.sandiegocounty.gov/content/sdc/hhsa/programs/ssp/calfresh-medical-work-requirements/medi-cal-work-requirements.html"),
    ]
    for nm, url in extras:
        if url not in seen:
            seen[url] = (nm, "Trusted secondary")
    return seen


def render_sources(tables):
    srcs = collect_sources(tables)
    rows = []
    for url, (nm, typ) in srcs.items():
        cls = "b-verified" if typ.startswith("Official") else "b-flagged"
        rows.append('<tr><td>%s</td><td><span class="badge %s">%s</span></td>'
                    '<td><a href="%s" target="_blank" rel="noopener">%s</a></td></tr>'
                    % (esc(nm), cls, esc(typ), esc(url), esc(url)))
    return '<div class="table-wrap"><table><caption>All sources cited in tables and page narratives</caption>' \
           "<thead><tr><th scope=\"col\">Source</th><th scope=\"col\">Type</th><th scope=\"col\">Link</th></tr></thead>" \
           "<tbody>%s</tbody></table></div>" % "".join(rows)


def stats(tables):
    counts = table_counts(tables)
    total = sum(c["rows"] for k, c in counts.items() if k != "flagged-items.csv")
    verified = sum(c["verified"] for k, c in counts.items() if k != "flagged-items.csv")
    unverified = sum(c["flagged"] for k, c in counts.items() if k != "flagged-items.csv")
    flagged = counts["flagged-items.csv"]["rows"]
    nsrc = len(collect_sources(tables))
    return total, verified, unverified, flagged, nsrc


def build():
    os.makedirs(OUT_DIR, exist_ok=True)
    tables = all_tables()
    total, verified, unverified, flagged, nsrc = stats(tables)
    auto_flagged_rows = []
    for name, rows in tables.items():
        if name == "flagged-items.csv":
            continue
        for r in rows:
            if (r.get("status") or "").lower() != "verified":
                auto_flagged_rows.append(r)

    for fname in PAGES:
        src = os.path.join(SRC_DIR, fname + ".tmpl")
        if not os.path.exists(src):
            print("ERROR: missing template", src)
            sys.exit(1)
        with open(src, encoding="utf-8") as f:
            doc = f.read()

        def table_repl(m):
            name = m.group(1)
            cap = m.group(2)
            if name == "AUTO_FLAGGED":
                rows = auto_flagged_rows
                cap = cap or "All non-verified rows across this site's data tables (auto-generated)"
            else:
                if name not in tables:
                    print("ERROR: unknown table", name)
                    sys.exit(1)
                rows = tables[name]
            return render_table(rows, cap)

        doc = re.sub(r"\{\{TABLE:([A-Za-z0-9_.-]+)(?:::([^}]*))?\}\}", table_repl, doc)
        doc = doc.replace("{{NAV}}", render_nav(fname))
        doc = doc.replace("{{CARDS}}", render_cards(tables))
        doc = doc.replace("{{STAT_ROWS}}", str(total))
        doc = doc.replace("{{STAT_VERIFIED}}", str(verified))
        doc = doc.replace("{{STAT_UNVERIFIED}}", str(unverified))
        doc = doc.replace("{{STAT_FLAGGED}}", str(flagged))
        doc = doc.replace("{{STAT_SOURCES}}", str(nsrc))
        doc = doc.replace("{{SNAPSHOT}}", SNAPSHOT)
        doc = doc.replace("{{SOURCE_LIST}}", render_sources(tables))
        out = os.path.join(OUT_DIR, fname)
        with open(out, "w", encoding="utf-8") as f:
            f.write(doc)
        print("built", out)

    os.makedirs(os.path.join(OUT_DIR, "assets"), exist_ok=True)
    with open(ASSETS_SRC, encoding="utf-8") as f_in, \
         open(os.path.join(OUT_DIR, "assets", "style.css"), "w", encoding="utf-8") as f_out:
        f_out.write(f_in.read())
    print("wrote", os.path.join(OUT_DIR, "assets", "style.css"))

    nojekyll = os.path.join(ROOT, ".nojekyll")
    open(nojekyll, "w").close()
    print("wrote", nojekyll)
    print("tables:", {k: v["rows"] for k, v in table_counts(tables).items()})
    print("totals: rows=%d verified=%d unverified-blanks=%d flagged-registry=%d sources=%d"
          % (total, verified, unverified, flagged, nsrc))


if __name__ == "__main__":
    build()
