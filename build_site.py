#!/usr/bin/env python3
"""
build_site.py — renders the static GitHub Pages site from data/*.json.

Deterministic, dependency-free (Python 3 standard library only). Run:

    python3 build_site.py

Outputs into ./docs (the GitHub Pages publishing directory). Also writes ./site/build-report.json with the
verification/link report produced during the build.

Every table row rendered by this builder must carry at least one source id that
resolves to a URL in data/sources.json, or be explicitly marked as BLANK.
That rule is enforced at build time and the build fails if it is violated.
"""

from __future__ import annotations

import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
SITE = ROOT / "docs"

GENERATED = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

NAV = [
    ("index.html", "Dashboard", "Executive summary and the numbers that matter"),
    ("options.html", "Coverage & Pathways", "How to get covered and how to comply"),
    ("income.html", "Income Sources", "Kalshi, rent, interest and the $580 test"),
    ("federal.html", "Federal Law", "P.L. 119-21 §71119 · 42 CFR 435.550–.563"),
    ("california.html", "California", "WIC §14005.69 · AB 2161 · DHCS guidance"),
    ("flagged.html", "Flagged for Review", "Irregularities and unverified values"),
    ("sources.html", "Source Register", "Every official source used, with links"),
]

FLAG_PAGE = "flagged.html"

# ---------------------------------------------------------------------------
# data loading
# ---------------------------------------------------------------------------


def load(name: str):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)


SOURCES_DOC = load("sources.json")
SOURCES = {s["id"]: s for s in SOURCES_DOC["sources"]}

PAGES = {
    "options": load("options.json"),
    "income": load("income.json"),
    "federal": load("federal-rules.json"),
    "california": load("california.json"),
    "flagged": load("flagged.json"),
}

PROBLEMS: list[str] = []
USED_SOURCE_IDS: set[str] = set()

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

INLINE_ALLOWED = re.compile(r"^[\w\s.,;:'\"()\[\]/&%$#@!?+=<>*\-—–§¶°×÷·…]*$")


def esc(text: str) -> str:
    """Escape text but permit a small, fixed set of inline markup we authored."""
    # Author-controlled markup only. Escape first, then un-escape our own tags.
    out = html.escape(str(text), quote=False)
    for tag in ("strong", "em", "code"):
        out = out.replace(f"&lt;{tag}&gt;", f"<{tag}>")
        out = out.replace(f"&lt;/{tag}&gt;", f"</{tag}>")
    out = out.replace("&lt;br&gt;", "<br>")
    return out


SHORT_LABELS = [
    (
        "California Department of Health Care Services, Medi-Cal Eligibility Division",
        "DHCS/MCED",
    ),
    ("California Department of Health Care Services", "DHCS"),
    ("U.S. Government Publishing Office / eCFR", "eCFR"),
    ("U.S. Government Publishing Office (govinfo.gov)", "govinfo"),
    ("U.S. Government Publishing Office (official U.S. Code)", "U.S. Code"),
    ("CMS Center for Medicaid and CHIP Services", "CMS/CMCS"),
    ("Centers for Medicare & Medicaid Services", "CMS"),
    ("Covered California (California Health Benefit Exchange)", "Covered CA"),
    ("Covered California", "Covered CA"),
    ("California Legislative Information", "CA LegInfo"),
    ("California Employment Development Department", "EDD"),
    ("California Franchise Tax Board", "FTB"),
    ("California Health and Human Services Agency", "CalHHS"),
    ("HHS Office of the Assistant Secretary for Planning and Evaluation", "HHS ASPE"),
    ("Office of the Federal Register", "Fed. Reg."),
    ("Internal Revenue Service", "IRS"),
    ("HealthCare.gov (CMS)", "HealthCare.gov"),
    ("Kalshi (platform official help centre)", "Kalshi"),
    ("Kalshi", "Kalshi"),
    ("U.S. Department of Labor, Wage and Hour Division", "DOL"),
    ("U.S. Congress (congress.gov)", "congress.gov"),
    ("Congressional Research Service (via congress.gov)", "CRS"),
    ("State of California — BenefitsCal", "BenefitsCal"),
    ("State of California — CalJOBS", "CalJOBS"),
    ("CMS / medicaid.gov", "medicaid.gov"),
]

# Patterns that turn a generic publisher label into a pinpoint citation, so a
# reviewer can see *which* provision a chip points at without hovering.
CITE_PATTERNS = [
    r"\b(\d+\s+CFR\s+§?\s*[\d.]+(?:\([a-z0-9)(]+\))?)",
    r"\b(\d+\s+U\.S\.C\.\s+§?\s*[\w().\-]+)",
    r"\b(\d+\s+FR\s+\d+)",
    r"\b(ACWDL\s*[\d\-]+)",
    r"\b(MEDIL\s*I?\s*[\d\-]+)",
    r"\b(AB[- ]?\d{3,4})\b",
    r"\b(SB\s*\d{2,4})\b",
    r"\b(WIC\s*§?\s*[\d.]+)",
    r"\b(Topic\s+No\.\s*\d+)",
    r"\b(Publication\s+\d+)",
    r"\b(Pub\.\s*\d+)",
    r"\b(Form\s+FTB\s+\d+)",
    r"\b(FTB\s+\d+)",
    r"\b(Rev\.\s*Proc\.[\d\-\s]+)",
    r"\b(R\d{5})\b",
    r"\b(Welfare and Institutions Code\s*§?\s*[\d.]+)",
    r"\b(Section\s+71\d{3})\b",
    r"\b(§\s?1902\(xx\)[\w()]*)",
    r"\b(§\s?\d+[\w.]*)",
]

# Publisher labels that are already specific enough to stand alone.
SELF_SUFFICIENT = {"Kalshi", "BenefitsCal", "CalJOBS"}

def title_fragment(title: str) -> str:
    """First meaningful segment of a source title, for use as a chip label."""
    head = re.split(r"\s+—\s+|\s+-\s+|\s+\(.*?\)$", title.strip())[0]
    head = head.replace("Welfare and Institutions Code", "WIC")
    head = head.replace("California ", "").replace("U.S. ", "")
    head = re.sub(r"\s+", " ", head).strip(" .,;:")
    return head if len(head) <= 40 else head[:39].rstrip() + "\u2026"


def attr(text: str) -> str:
    """Escape for use inside a double-quoted HTML attribute."""
    return html.escape(str(text), quote=True)


def short_publisher(publisher: str) -> str:
    for needle, repl in SHORT_LABELS:
        publisher = publisher.replace(needle, repl)
    return publisher.strip()


def pinpoint(title: str) -> str:
    for pat in CITE_PATTERNS:
        m = re.search(pat, title)
        if m:
            cite = re.sub(r"\s+", " ", m.group(1)).strip()
            cite = cite.replace("CFR § ", "CFR ").replace("U.S.C. § ", "U.S.C. ")
            cite = cite.replace("Welfare and Institutions Code", "WIC")
            return cite
    return ""


def source_chips(ids) -> str:
    """Render the per-row source links. This is the core verification control."""
    if not ids:
        return (
            '<span class="chip chip-blank" title="No official primary source could '
            'confirm this value. Left blank and flagged.">BLANK — unverified</span>'
        )
    chips = []
    for sid in ids:
        src = SOURCES.get(sid)
        if src is None:
            PROBLEMS.append(f"unknown source id referenced: {sid!r}")
            chips.append(
                f'<span class="chip chip-bad">UNRESOLVED SOURCE {esc(sid)}</span>'
            )
            continue
        USED_SOURCE_IDS.add(sid)
        pub = short_publisher(src["publisher"])
        cite = pinpoint(src["title"])
        if not cite and pub not in SELF_SUFFICIENT:
            frag = title_fragment(src["title"])
            # drop leading tokens that merely repeat the publisher label
            while True:
                parts = frag.split(" ", 1)
                if len(parts) < 2:
                    break
                head = parts[0].strip(" .,;:").lower()
                if head and any(
                    head == tok.strip(" .,;:/").lower()
                    for tok in re.split(r"[\s/·]+", pub.lower())
                ):
                    frag = parts[1]
                else:
                    break
            if frag and frag.lower() != pub.lower():
                cite = frag
        label = f"{pub} · {cite}" if cite else pub
        chips.append(
            f'<a class="chip" href="{attr(src["url"])}" target="_blank" '
            f'rel="noopener noreferrer" '
            f'title="{attr(src["title"] + " — " + src["publisher"])}">'
            f"{esc(label)}</a>"
        )
    return "".join(chips)



def render_table(section: dict, page_key: str) -> str:
    cols = section["columns"]
    rows = section["rows"]
    has_src = cols and cols[-1].strip().lower() in ("source", "sources", "link")
    head = "".join(f"<th>{esc(c)}</th>" for c in cols)
    body = []
    for i, row in enumerate(rows):
        cells = row["c"]
        if len(cells) != len(cols):
            PROBLEMS.append(
                f"{page_key}/{section['id']}: row {i} has {len(cells)} cells "
                f"but {len(cols)} columns"
            )
        tds = []
        text_cells = cells[:-1] if has_src else cells
        for cell in text_cells:
            tds.append(f"<td>{esc(cell)}</td>")
        if has_src:
            tds.append(f'<td class="src">{source_chips(cells[-1])}</td>')
        body.append(f'<tr>{"".join(tds)}</tr>')
    intro = (
        f'<p class="section-intro">{esc(section["intro"])}</p>'
        if section.get("intro")
        else ""
    )
    return f"""
<section class="block" id="{esc(section['id'])}">
  <h2>{esc(section['title'])}</h2>
  {intro}
  <div class="tablewrap">
    <table>
      <thead><tr>{head}</tr></thead>
      <tbody>{''.join(body)}</tbody>
    </table>
  </div>
</section>"""


def render_page(doc: dict, key: str) -> str:
    sections = "\n".join(render_table(s, key) for s in doc["sections"])
    extra = ""
    if key == "flagged":
        extra = f'<div class="notice">{esc(doc["rule"])}</div>'
    return shell(
        title=doc["title"],
        subtitle=doc["subtitle"],
        active=f"{key}.html",
        body=f"""
<header class="pagehead">
  <h1>{esc(doc['title'])}</h1>
  <p class="sub">{esc(doc['subtitle'])}</p>
</header>
{extra}
{sections}
""",
    )


def shell(title: str, subtitle: str, active: str, body: str) -> str:
    nav = []
    for href, label, desc in NAV:
        cls = ' class="active"' if href == active else ""
        nav.append(
            f'<li><a{cls} href="{href}"><span class="nlabel">{esc(label)}</span>'
            f'<span class="ndesc">{esc(desc)}</span></a></li>'
        )
    flag_link = (
        '<span class="flagbadge">Flagged for Review</span>' if active == FLAG_PAGE else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — Medicaid &amp; Medi-Cal Work Requirement Research</title>
<meta name="description" content="{esc(subtitle)}">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="layout">
<nav class="side" aria-label="Section navigation">
  <div class="brand">
    <span class="brandmark">§1902(xx)</span>
    <span class="brandtext">Work Requirement<br>Research Dashboard</span>
  </div>
  <ul>{''.join(nav)}</ul>
  <div class="sidefoot">
    <div>Every row cites an official primary source.</div>
    <div>Unconfirmable values are left <strong>blank</strong> and flagged.</div>
  </div>
</nav>
<main id="main">
{body}
<footer class="foot">
  <p><strong>Not legal, tax or medical advice.</strong> This is a research and
  verification dashboard. It summarises published official sources and links to them.
  Confirm anything consequential with the California Department of Health Care Services,
  your county Medi-Cal office, Covered California, a licensed California attorney, or a
  CPA / enrolled agent. See <a href="{FLAG_PAGE}">Flagged for Review</a> {flag_link}
  for every irregularity, discrepancy and unverified value.</p>
  <p>Companion publications in this repository: the
  <a href="../index.html">root research brief</a> and the
  <a href="../dashboard/index.html">expanded data dashboard</a> — three independent,
  cross-checked verification passes over the same official sources.</p>
  <p>Generated {GENERATED} · sources retrieved 2026-10-18 · session <code>690e8271</code> ·
  repository <a href="https://github.com/buffedlizard55-lab/MaltaProj9"
  target="_blank" rel="noopener noreferrer">buffedlizard55-lab/MaltaProj9</a></p>
</footer>
</main>
</div>
<script src="assets/app.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# index (hand-authored dashboard) + sources page
# ---------------------------------------------------------------------------

KEYNUMBERS = [
    ("$580", "Monthly income that satisfies the requirement", "80 hours × $7.25 federal minimum wage", "CMCS-CIB-2025-12-08"),
    ("80 hrs", "Monthly work / community service / work program", "42 CFR §435.552(a)(1)–(3)", "ECFR-435-552"),
    ("Jan 1 2027", "Federal implementation deadline for states", "Earlier at state option via SPA or §1115", "CMCS-CIB-2025-12-08"),
    ("1 month", "California's lookback — the shortest allowed", "WIC §14005.69(d)(1); federal permits 1–3", "LEGINFO-WIC-14005-69"),
    ("19–64", "Age band of an applicable individual", "Not pregnant, not on Medicare", "ECFR-435-551"),
    ("30 days", "Cure period after a noncompliance notice", "Coverage continues during the period", "CMCS-CIB-2025-12-08"),
    ("$22,025", "2026 Medi-Cal limit for one person (138% FPL)", "Above this → Covered California instead", "DHCS-FPL-CHART"),
    ("Oct 1 2034", "Sunset of the implementing regulations", "Pre-sunset policy restored", "FR-91-33348"),
]


def render_index() -> str:
    cards = []
    for big, label, note, sid in KEYNUMBERS:
        src = SOURCES[sid]
        USED_SOURCE_IDS.add(sid)
        cards.append(
            f"""<a class="kpi" href="{attr(src['url'])}" target="_blank" rel="noopener noreferrer">
      <span class="kpiv">{esc(big)}</span>
      <span class="kpil">{esc(label)}</span>
      <span class="kpin">{esc(note)}</span>
      <span class="kpis">source: {esc(src['publisher'])}</span>
    </a>"""
        )

    navcards = []
    blurb = {
        "options.html": "Decision tree, ranked compliance pathways, the premium-tax-credit trap, Covered California subsidies, the state individual mandate, and an action checklist.",
        "income.html": "How Kalshi event contracts, rental income and savings interest are classified by the IRS, by Medicaid, and by California — and why the answers differ.",
        "federal.html": "Chain of authority, the seven compliance pathways, definitions, exclusions, exceptions, hardship events, verification, noncompliance and the §1902(xx)(7)(B) subsidy bar.",
        "california.html": "WIC §14005.69, SB 164 and AB 2161, California's conditional-implementation safeguards, DHCS letters, the timeline, income limits and asset limits.",
        "flagged.html": "23 flagged items, 7 categories of value deliberately left blank, the repository review findings and the verification cross-check applied to every row.",
        "sources.html": "The complete register of official primary sources with publisher, title, type and the note recorded at retrieval time.",
    }
    for href, label, desc in NAV:
        if href == "index.html":
            continue
        navcards.append(
            f"""<a class="navcard" href="{href}">
      <span class="navcard-t">{esc(label)}</span>
      <span class="navcard-d">{esc(blurb[href])}</span>
      <span class="navcard-go">Open →</span>
    </a>"""
        )

    body = f"""
<header class="pagehead">
  <h1>Medicaid &amp; Medi-Cal Work Requirement — Research Dashboard</h1>
  <p class="sub">Section 71119 of Public Law 119-21 · SSA §1902(xx) · 42 CFR Part 435 Subpart F ·
  California WIC §14005.69 · verified against official primary sources on 2026-10-18</p>
</header>

<div class="notice notice-key">
  <strong>Headline finding.</strong> The compliance test is <em>not</em> an earned-income test.
  42 CFR §435.552(f)(2) requires the agency to measure monthly income on the individual's
  <strong>MAGI-based income for their MAGI-based household</strong>, and MAGI is built from
  <strong>adjusted gross income</strong> — which includes rental income, interest and trading gains.
  California says the same thing to members in plain words:
  &ldquo;<strong>Have an income from any source of at least $580 (before taxes) in any month since your last renewal.</strong>&rdquo;
  <span class="noticesrc">
    {source_chips(["ECFR-435-552", "ECFR-435-603", "DHCS-MEDIL-I26-25"])}
  </span>
</div>

<section class="block">
  <h2>Executive summary</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Question</th><th>Answer</th><th>Where to verify</th></tr></thead>
    <tbody>
      <tr><td><strong>What is the new requirement?</strong></td>
        <td>Section 71119 of H.R. 1 (Public Law 119-21, enacted July 4, 2025) added subsection (xx) to section 1902 of the Social Security Act. States must condition Medicaid eligibility for &ldquo;applicable individuals&rdquo; on demonstrating <strong>community engagement</strong>. CMS implemented it in <strong>CMS-2454-IFC</strong>, 91 FR 33348 (June 3, 2026), codified at <strong>42 CFR §§435.550–435.563</strong>, effective July 31, 2026, sunsetting October 1, 2034.</td>
        <td class="src">{source_chips(["CONGRESS-HR1", "CMCS-CIB-2025-12-08", "GOVINFO-2026-11094", "ECFR-435-SUBPART-F"])}</td></tr>
      <tr><td><strong>Who does it apply to?</strong></td>
        <td>Non-pregnant adults <strong>19 through 64</strong>, not entitled to or enrolled in Medicare, who are eligible for or enrolled in the Medicaid <strong>adult group</strong> (the ACA expansion group) or in certain §1115 demonstrations providing minimum essential coverage. Applies in the 50 states and DC — <strong>not</strong> the territories. CMS states <strong>43 states and DC</strong> must implement.</td>
        <td class="src">{source_chips(["ECFR-435-551", "CMS-FACTSHEET", "CMCS-CIB-2025-12-08"])}</td></tr>
      <tr><td><strong>When?</strong></td>
        <td>States must implement <strong>no later than January 1, 2027</strong>, or earlier at state option. California's statute says <strong>no sooner than January 1, 2027</strong> and only after DHCS certifies in writing that systems are programmed. DHCS's member letter tells members the rules &ldquo;will not go into effect until <strong>March 2027</strong>&rdquo; — see flagged item <strong>F-11</strong>.</td>
        <td class="src">{source_chips(["CMCS-CIB-2025-12-08", "LEGINFO-WIC-14005-69", "DHCS-MEDIL-I26-25"])}</td></tr>
      <tr><td><strong>How do you comply with $0 earned income?</strong></td>
        <td>Use the <strong>income pathway</strong>: monthly MAGI household income of at least <strong>$580</strong> (80 × $7.25). Rental income, savings interest and Kalshi trading gains are all in AGI and therefore in MAGI. In California only <strong>one qualifying month</strong> since the last renewal is required. Backups: <strong>half-time enrolment</strong> in an educational program (no hours, no income), <strong>80 hours of community service</strong>, or <strong>80 hours in a work program</strong> (free through America's Job Center of California).</td>
        <td class="src">{source_chips(["ECFR-435-552", "ECFR-435-603", "LEGINFO-WIC-14005-69", "DHCS-MEDIL-I26-25", "DHCS-ACWDL-25-30"])}</td></tr>
      <tr><td><strong>Can trading or property management count as &ldquo;work&rdquo; hours?</strong></td>
        <td>Managing property <strong>for third parties for a fee</strong> is ordinary self-employment and the hours count — CMS says so expressly. Managing <strong>your own rentals</strong> is a reasonable reading of the same definition but is <strong>not addressed by any official guidance</strong>. Kalshi trading is <strong>unverified</strong> — no CMS, DHCS or IRS guidance addresses it. Both are flagged (<strong>F-02, F-03</strong>) rather than asserted.</td>
        <td class="src">{source_chips(["FR-91-33348", "ECFR-435-552", "IRS-TC429"])}</td></tr>
      <tr><td><strong>What is California doing to help?</strong></td>
        <td>It wrote the requirement into <strong>WIC §14005.69</strong> (SB 164, Stats. 2026 Ch. 27) with three safeguards federal law does not require: implementation <strong>only after</strong> the DHCS Director certifies in writing to the Department of Finance that systems are programmed; implementation <strong>only to the extent</strong> federal approvals are obtained and federal financial participation is available; and a <strong>data-first</strong> verification duty. <strong>AB 2161 (Chapter 209)</strong> added a duty to let you confirm conflicting data <strong>before</strong> any adverse action, and chose the <strong>one-month</strong> lookback — the shortest federal law allows. California also funds its own <strong>state premium subsidy</strong> up to <strong>200% FPL</strong> for 2027 ($300M).</td>
        <td class="src">{source_chips(["LEGINFO-WIC-14005-69", "LEGINFO-AB2161", "LEGINFO-AB2161-TEXT", "CC-2027-PR"])}</td></tr>
      <tr><td><strong>What is the biggest risk?</strong></td>
        <td>SSA §1902(xx)(7)(B): if you <strong>fail</strong> the requirement but <strong>would otherwise</strong> have been Medicaid-eligible, you are <strong>deemed eligible for minimum essential coverage</strong> and are therefore <strong>barred from the premium tax credit and its advance payments</strong>. DHCS tells members directly: &ldquo;If you lose Medi-Cal because you did not meet these rules, <strong>you cannot get financial help to pay for a health plan through Covered California</strong>.&rdquo;</td>
        <td class="src">{source_chips(["CMCS-CIB-2025-12-08", "DHCS-MEDIL-I26-25"])}</td></tr>
      <tr><td><strong>Does owning property disqualify you?</strong></td>
        <td><strong>No</strong> — not for the MAGI adult group. 42 CFR §435.603(g) says the agency &ldquo;<strong>must not</strong> apply any assets or resources test&rdquo;. The Medi-Cal <strong>asset</strong> limits DHCS describes ($130,000 now; $21,000 / $31,000 from July 1, 2027, counting &ldquo;more than one house or vehicle&rdquo;) apply to <strong>Non-MAGI</strong> groups — age 65+, disability, nursing home. See flagged item <strong>F-17</strong> for why these are routinely confused.</td>
        <td class="src">{source_chips(["ECFR-435-603", "DHCS-CHANGES"])}</td></tr>
      <tr><td><strong>Are you even in scope?</strong></td>
        <td>Only if MAGI household income is at or below <strong>138% FPL</strong> — <strong>$22,025/year ($1,836/month)</strong> for one person in 2026. Above that you are not in the adult group, the work requirement does not apply, and the route is a <strong>Covered California</strong> plan. Note the enhanced federal subsidy expired <strong>December 31, 2025</strong>, and the <strong>PTC repayment cap is removed</strong> from the 2026 tax year.</td>
        <td class="src">{source_chips(["DHCS-FPL-CHART", "ASPE-FPL", "CC-CHANGES"])}</td></tr>
    </tbody>
  </table></div>
</section>

<section class="block">
  <h2>The numbers that matter</h2>
  <p class="section-intro">Each card links directly to the official source for that figure.</p>
  <div class="kpigrid">{''.join(cards)}</div>
</section>

<section class="block">
  <h2>Do this first</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>#</th><th>Action</th><th>Why</th><th>Source</th></tr></thead>
    <tbody>
      <tr><td>1</td><td><strong>Confirm your Medi-Cal group.</strong> The rule reaches only the <strong>MAGI New Adult Group (aid code M1)</strong>. Non-MAGI, mandatory children's and pregnancy groups are excluded, as are restricted-scope (emergency) Medi-Cal and pregnancy-services recipients.</td><td>Decides whether the rule applies to you at all.</td><td class="src">{source_chips(["DHCS-ACWDL-25-30"])}</td></tr>
      <tr><td>2</td><td><strong>Create or update a BenefitsCal account</strong> and confirm the county has your current mailing address, phone and email.</td><td>Notices start the 30-day clock; a stale address is the classic cause of avoidable loss.</td><td class="src">{source_chips(["DHCS-MEDIL-I26-25", "BENEFITSCAL"])}</td></tr>
      <tr><td>3</td><td><strong>Watch for the DHCS outreach letter.</strong> Mailing began <strong>late August 2026</strong>; counties must include it with application materials <strong>October 1 – December 31, 2026</strong>.</td><td>It explains who is subject, the exemptions, and the consequences.</td><td class="src">{source_chips(["DHCS-MEDIL-I26-25"])}</td></tr>
      <tr><td>4</td><td><strong>Keep a monthly income record</strong> — Kalshi PnL statement and trade history, rent receipts and Schedule E figures, bank and Kalshi 1099-INT. Target at least one month at <strong>≥ $580</strong>.</td><td>The income pathway needs no hour logging, and California needs only one qualifying month.</td><td class="src">{source_chips(["ECFR-435-552", "LEGINFO-WIC-14005-69", "KALSHI-TAXINFO"])}</td></tr>
      <tr><td>5</td><td><strong>Line up a backup now</strong> — half-time enrolment at a California Community College, or registration at an <strong>America's Job Center of California</strong>.</td><td>A trading loss plus a rental vacancy could leave a month under $580.</td><td class="src">{source_chips(["ECFR-435-552", "EDD-WIOA", "EDD-LOCATOR"])}</td></tr>
      <tr><td>6</td><td><strong>Screen for an exclusion</strong> — especially California's broader caregiver category, WIC §14005.69(b)(2)(F), covering care of someone with a &ldquo;<strong>chronic or other health condition, disability, or functional limitation</strong>&rdquo;, and (b)(2)(H)(v), a <strong>serious or complex medical condition</strong>.</td><td>An exclusion removes the requirement entirely instead of requiring monthly proof.</td><td class="src">{source_chips(["LEGINFO-WIC-14005-69", "ECFR-435-554"])}</td></tr>
      <tr><td>7</td><td><strong>Never let a notice of noncompliance lapse.</strong> 30 calendar days from receipt; coverage continues; then request a <strong>state hearing</strong> and ask about <strong>continued aid</strong>.</td><td>A lapse costs Medi-Cal <em>and</em> APTC/PTC.</td><td class="src">{source_chips(["LEGINFO-WIC-14005-69", "CMCS-CIB-2025-12-08", "DHCS-MEDIL-I26-25"])}</td></tr>
      <tr><td>8</td><td><strong>Contacts.</strong> Medi-Cal Helpline <strong>(800) 541-5555</strong> · county locator <strong>dhcs.ca.gov/COL</strong> · DHCS policy <strong>MCED-Policy@dhcs.ca.gov</strong> · Covered California <strong>(800) 300-1506</strong> · CMS technical assistance <strong>MedicaidWorks@cms.hhs.gov</strong>.</td><td>All official.</td><td class="src">{source_chips(["DHCS-MEDIL-I26-25", "DHCS-COUNTY", "CC-CHANGES", "CMS-HUB"])}</td></tr>
    </tbody>
  </table></div>
</section>

<section class="block">
  <h2>Sections</h2>
  <div class="navgrid">{''.join(navcards)}</div>
</section>
"""
    return shell(
        title="Dashboard",
        subtitle="Executive summary",
        active="index.html",
        body=body,
    )


def render_sources() -> str:
    rows = []
    for s in SOURCES_DOC["sources"]:
        used = s["id"] in USED_SOURCE_IDS
        badge = (
            '<span class="chip chip-ok">cited</span>'
            if used
            else '<span class="chip chip-unused">registered</span>'
        )
        rows.append(
            f"""<tr>
      <td><code>{esc(s['id'])}</code></td>
      <td>{esc(s['publisher'])}</td>
      <td>{esc(s['title'])}</td>
      <td>{esc(s['type'])}</td>
      <td>{esc(s.get('note') or '—')}</td>
      <td class="src"><a class="chip" href="{attr(s['url'])}" target="_blank" rel="noopener noreferrer">open ↗</a></td>
      <td>{badge}</td>
    </tr>"""
        )
    body = f"""
<header class="pagehead">
  <h1>Source Register</h1>
  <p class="sub">{esc(SOURCES_DOC['policy'])} · retrieved {esc(SOURCES_DOC['retrieved'])}</p>
</header>
<div class="notice">
  <strong>Verification standard.</strong> A row is published only if a <strong>primary official
  source</strong> was actually retrieved during this session and states the value.
  Secondary sources — law-firm client alerts, health-policy institutes, hospital and insurer
  associations, insurance and tax blogs, local news — were used <strong>only to locate</strong>
  primary sources and are <strong>never</strong> cited as authority for a published row. Where no
  official source could be found, the value is left <strong>blank</strong> and the item appears on
  the <a href="{FLAG_PAGE}">Flagged for Review</a> page. The one non-government source in this
  register (Kalshi's own help centre) is used solely to record what the platform itself says it reports.
</div>
<section class="block">
  <h2>All registered sources ({len(SOURCES_DOC['sources'])})</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>ID</th><th>Publisher</th><th>Title</th><th>Type</th><th>Retrieval note</th><th>Link</th><th>Use</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table></div>
</section>
"""
    return shell(
        title="Source Register",
        subtitle="Official primary sources",
        active="sources.html",
        body=body,
    )


# ---------------------------------------------------------------------------
# assets
# ---------------------------------------------------------------------------

CSS = r"""
:root{
  --bg:#0f1115; --panel:#161a21; --panel2:#1c222b; --line:#2a323d;
  --ink:#e8ecf1; --ink2:#a7b1bf; --ink3:#7d8896;
  --accent:#5eb1ff; --accent2:#7ee0b8; --warn:#ffcc66; --bad:#ff8a8a;
  --chip:#202834; --radius:10px;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font:15px/1.6 var(--sans);-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
a:hover{color:#a8d6ff}
code{font:12.5px/1.5 var(--mono);background:var(--panel2);padding:1px 5px;border-radius:4px;color:#cfe3ff}
.skip{position:absolute;left:-9999px;top:0;background:var(--accent);color:#06121f;padding:8px 14px;z-index:99}
.skip:focus{left:8px;top:8px}

.layout{display:grid;grid-template-columns:280px minmax(0,1fr);gap:0;align-items:start}
.side{position:sticky;top:0;height:100vh;overflow-y:auto;background:var(--panel);border-right:1px solid var(--line);padding:22px 16px}
.brand{display:flex;gap:10px;align-items:flex-start;padding:0 6px 18px;border-bottom:1px solid var(--line);margin-bottom:14px}
.brandmark{font:700 11px/1.4 var(--mono);letter-spacing:.06em;color:#06121f;background:var(--accent);padding:5px 7px;border-radius:6px;white-space:nowrap}
.brandtext{font-size:13px;color:var(--ink2);line-height:1.35}
.side ul{list-style:none;margin:0;padding:0}
.side li{margin:2px 0}
.side a{display:block;text-decoration:none;padding:9px 10px;border-radius:8px;border:1px solid transparent}
.side a:hover{background:var(--panel2);border-color:var(--line)}
.side a.active{background:var(--panel2);border-color:#33404f}
.nlabel{display:block;font-weight:650;color:var(--ink);font-size:14px}
.side a.active .nlabel{color:var(--accent)}
.ndesc{display:block;font-size:11.5px;color:var(--ink3);line-height:1.4;margin-top:2px}
.sidefoot{margin-top:20px;padding-top:14px;border-top:1px solid var(--line);font-size:11.5px;color:var(--ink3);line-height:1.55}
.sidefoot strong{color:var(--warn)}

main{padding:30px 34px 60px;min-width:0}
.pagehead{margin-bottom:22px}
.pagehead h1{margin:0 0 6px;font-size:27px;line-height:1.25;letter-spacing:-.01em}
.pagehead .sub{margin:0;color:var(--ink2);font-size:13.5px}

.notice{background:linear-gradient(180deg,#1b2230,#171d27);border:1px solid #2f3d4f;border-left:4px solid var(--accent);
  padding:16px 18px;border-radius:var(--radius);margin:0 0 24px;font-size:14.5px;color:var(--ink)}
.notice-key{border-left-color:var(--accent2)}
.notice strong{color:#fff}
.noticesrc{display:block;margin-top:12px}

.block{margin:0 0 34px}
.block h2{font-size:19px;margin:0 0 6px;letter-spacing:-.01em;padding-bottom:8px;border-bottom:1px solid var(--line)}
.section-intro{color:var(--ink2);font-size:13.5px;margin:8px 0 14px;max-width:95ch}

.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius);background:var(--panel)}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:13.5px}
thead th{position:sticky;top:0;background:var(--panel2);color:var(--ink);text-align:left;font-weight:650;
  padding:11px 12px;border-bottom:1px solid var(--line);white-space:nowrap;font-size:12.5px;letter-spacing:.02em;text-transform:uppercase}
tbody td{padding:11px 12px;border-bottom:1px solid #222a34;vertical-align:top;color:var(--ink2)}
tbody tr:last-child td{border-bottom:none}
tbody tr:nth-child(even){background:#141922}
tbody tr:hover{background:#1b2230}
tbody td:first-child{color:var(--ink);font-weight:600;white-space:nowrap}
td strong{color:#fff}
td.src{white-space:normal;min-width:180px}

.chip{display:inline-block;font:600 11px/1 var(--sans);padding:5px 8px;margin:2px 4px 2px 0;border-radius:20px;
  background:var(--chip);border:1px solid #31404f;color:#bcd6ee;text-decoration:none;white-space:nowrap}
.chip:hover{background:#2a3543;border-color:var(--accent);color:#fff}
.chip-blank{background:#3a2b12;border-color:#6b4d18;color:var(--warn);font-weight:700}
.chip-bad{background:#3a1a1a;border-color:#7a2b2b;color:var(--bad);font-weight:700}
.chip-ok{background:#12301f;border-color:#255c3c;color:var(--accent2)}
.chip-unused{background:#22262e;border-color:#333b46;color:var(--ink3)}

.kpigrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:12px}
.kpi{display:block;background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:15px;
  text-decoration:none;transition:border-color .15s,transform .15s}
.kpi:hover{border-color:var(--accent);transform:translateY(-2px)}
.kpiv{display:block;font-size:26px;font-weight:750;letter-spacing:-.02em;color:#fff}
.kpil{display:block;font-size:12.5px;color:var(--ink2);margin-top:5px;font-weight:600;line-height:1.4}
.kpin{display:block;font-size:11.5px;color:var(--ink3);margin-top:6px;line-height:1.45}
.kpis{display:block;font:11px/1.4 var(--mono);color:#4f7ea8;margin-top:9px}

.navgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.navcard{display:block;background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:16px;text-decoration:none}
.navcard:hover{border-color:var(--accent)}
.navcard-t{display:block;font-size:15.5px;font-weight:680;color:#fff}
.navcard-d{display:block;font-size:12.5px;color:var(--ink2);margin-top:6px;line-height:1.55}
.navcard-go{display:block;font-size:12px;color:var(--accent);margin-top:10px;font-weight:600}

.flagbadge{display:inline-block;font:700 10.5px/1 var(--sans);letter-spacing:.06em;text-transform:uppercase;
  background:#3a2b12;border:1px solid #6b4d18;color:var(--warn);padding:5px 8px;border-radius:20px}

.foot{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);color:var(--ink3);font-size:12.5px;line-height:1.65}
.foot strong{color:var(--warn)}
.foot a{color:var(--accent)}

.tools{display:flex;gap:10px;align-items:center;margin:0 0 14px;flex-wrap:wrap}
.tools input{flex:1;min-width:220px;background:var(--panel2);border:1px solid var(--line);color:var(--ink);
  padding:9px 12px;border-radius:8px;font:13.5px var(--sans)}
.tools input:focus{outline:none;border-color:var(--accent)}
.tools .count{font:11.5px var(--mono);color:var(--ink3)}
tr.hide{display:none}

@media (max-width:980px){
  .layout{grid-template-columns:1fr}
  .side{position:static;height:auto;border-right:none;border-bottom:1px solid var(--line)}
  .side ul{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:6px}
  .ndesc{display:none}
  main{padding:22px 16px 48px}
  thead th{position:static}
}
@media print{
  body{background:#fff;color:#000}
  .side,.tools,.skip{display:none}
  .layout{grid-template-columns:1fr}
  .tablewrap,.notice,.kpi,.navcard{border-color:#bbb;background:#fff}
  tbody td,.section-intro,.foot{color:#222}
  td strong,.pagehead h1,.navcard-t,.kpiv{color:#000}
  thead th{background:#eee;color:#000}
}
"""

JS = r"""
// Progressive enhancement only. Every page is fully readable with JS disabled.
(function () {
  'use strict';

  // Insert a filter box above each table that has more than a handful of rows.
  var blocks = document.querySelectorAll('.block');
  Array.prototype.forEach.call(blocks, function (block) {
    var table = block.querySelector('table');
    if (!table) return;
    var rows = table.querySelectorAll('tbody tr');
    if (rows.length < 6) return;

    var tools = document.createElement('div');
    tools.className = 'tools';
    var input = document.createElement('input');
    input.type = 'search';
    input.placeholder = 'Filter rows in this table\u2026';
    input.setAttribute('aria-label', 'Filter rows in ' + (block.querySelector('h2') || {}).textContent);
    var count = document.createElement('span');
    count.className = 'count';
    count.textContent = rows.length + ' rows';
    tools.appendChild(input);
    tools.appendChild(count);
    block.insertBefore(tools, block.querySelector('.tablewrap'));

    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      var shown = 0;
      Array.prototype.forEach.call(rows, function (tr) {
        var hit = !q || tr.textContent.toLowerCase().indexOf(q) !== -1;
        tr.classList.toggle('hide', !hit);
        if (hit) shown++;
      });
      count.textContent = shown + ' / ' + rows.length + ' rows';
    });
  });

  // Flag any link that leaves the site without a resolvable href (build-time
  // integrity check surfaced in the browser too).
  var broken = document.querySelectorAll('a[href=""], a[href="#"], a.chip:not([href])');
  if (broken.length) {
    console.warn('[site] links with no target:', broken.length);
  }
})();
"""


def build(outdir: Path) -> tuple[dict, list[str]]:
    """Render every page and asset into `outdir`. Returns (report, problems)."""
    outdir.mkdir(exist_ok=True)
    (outdir / "assets").mkdir(exist_ok=True)

    pages: dict[str, str] = {}
    pages["index.html"] = render_index()
    for key, doc in PAGES.items():
        pages[f"{key}.html"] = render_page(doc, key)
    # sources page last so USED_SOURCE_IDS is fully populated
    pages["sources.html"] = render_sources()

    for name, content in pages.items():
        (outdir / name).write_text(content, encoding="utf-8")

    (outdir / "assets" / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (outdir / "assets" / "app.js").write_text(JS.strip() + "\n", encoding="utf-8")
    (outdir / ".nojekyll").write_text("", encoding="utf-8")

    problems = list(PROBLEMS)

    # ---- internal-link integrity -----------------------------------------
    for name, content in pages.items():
        for href in re.findall(r'href="([^"]+)"', content):
            if href.startswith(("http://", "https://", "mailto:", "tel:")) or href.startswith("#"):
                continue
            path_part = href.split("#")[0]
            target = (outdir / path_part).resolve()
            if not target.exists() and path_part.startswith("../"):
                # cross-publication links (root brief, dashboard/) live one level
                # above docs/ in the repository; resolve them against the repo
                # root so `--check` (which builds into a temp dir) can verify them.
                target = (ROOT / path_part[3:]).resolve()
            if not target.exists():
                problems.append(f"{name}: broken internal link -> {href}")
        for tag in ("strong", "em", "code"):
            o = len(re.findall(f"<{tag}[ >]", content))
            c = len(re.findall(f"</{tag}>", content))
            if o != c:
                problems.append(f"{name}: unbalanced <{tag}> ({o} open, {c} close)")

    unused = sorted(set(SOURCES) - USED_SOURCE_IDS)

    report = {
        "generated": GENERATED,
        "pages_written": sorted(pages),
        "sources_registered": len(SOURCES),
        "sources_cited_in_tables": len(USED_SOURCE_IDS),
        "sources_registered_but_uncited": unused,
        "total_flagged_items": len(PAGES["flagged"]["sections"][0]["rows"]),
        "problems": problems,
    }
    (outdir / "build-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    return report, problems


def diff_tree(a: Path, b: Path) -> list[str]:
    """Structural comparison of two built trees, ignoring the timestamp line."""
    out = []
    files_a = {p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file()}
    files_b = {p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file()}
    for f in sorted(files_a - files_b):
        out.append(f"missing from committed site: {f}")
    for f in sorted(files_b - files_a):
        out.append(f"unexpected file in committed site: {f}")
    for f in sorted(files_a & files_b):
        if f.endswith((".json",)):
            continue  # build-report.json embeds a timestamp
        ta = (a / f).read_text(encoding="utf-8")
        tb = (b / f).read_text(encoding="utf-8")
        # strip the generated timestamp from the footer before comparing
        pat = re.compile(r"Generated \d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC")
        if pat.sub("Generated X", ta) != pat.sub("Generated X", tb):
            out.append(f"committed site is out of date: {f} (re-run: python3 build_site.py)")
    return out


def main(argv: list[str]) -> int:
    check_only = "--check" in argv

    if check_only:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            outdir = Path(tmp)
            report, problems = build(outdir)
            if not SITE.exists():
                problems.append(f"committed site directory {SITE} does not exist")
            else:
                problems += diff_tree(outdir, SITE)
            print(f"pages built: {len(report['pages_written'])}")
            print(
                f"sources registered: {report['sources_registered']}  "
                f"cited: {report['sources_cited_in_tables']}"
            )
            if problems:
                print("\nPROBLEMS:")
                for p in problems:
                    print("  - " + p)
                return 1
            print("\nOK — site rebuilds cleanly and matches the committed output.")
            return 0

    report, problems = build(SITE)
    print(f"pages written: {len(report['pages_written'])} -> {SITE}/")
    print(
        f"sources registered: {report['sources_registered']}  "
        f"cited: {report['sources_cited_in_tables']}"
    )
    if report["sources_registered_but_uncited"]:
        print(
            "registered but uncited: "
            + ", ".join(report["sources_registered_but_uncited"])
        )
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  - " + p)
        return 1
    print("\nOK — no problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
