# MaltaProj9 — California healthcare eligibility research

A source-linked, static research project explaining California Medi-Cal and Covered California
options for a U.S. citizen resident with no earned wages but possible rental, trading
(Kalshi), and savings-interest income. It covers the federal Medicaid community-engagement law
scheduled for 2027, California implementation materials, application routes, income treatment,
and unresolved items.

The repository contains **three complementary publications** built by parallel research sessions,
all verified against official sources on **October 18, 2026**:

## 1. Research brief (site root) — session `arena/63a8fb6e`

- [Executive summary](index.html)
- [Medi-Cal eligibility](eligibility.html)
- [2027 community-engagement requirements](work-rules.html)
- [Income and assets](income.html)
- [Coverage options and application](options.html)
- [Flagged for Review](flagged.html)
- [Sources and repository audit](sources.html)

Plain HTML and CSS, no build dependencies. `.github/workflows/pages.yml` runs the
dependency-free link/source-table validation (`scripts/check_site.py`) on pushes and pull
requests targeting `main`.

## 2. Expanded data dashboard (`dashboard/`) — session `arena/0ef38cd8`

- [Dashboard home](dashboard/index.html) — key findings, key numbers, timeline
- [Executive summary](dashboard/executive-summary.html) — decision paths, plain-English law, action checklist
- [Work requirements](dashboard/work-requirements.html) — OBBBA §71119 + CMS-2454-IFC details
- [Medi-Cal](dashboard/medi-cal.html) — 138% FPL rules, MAGI, no asset test, 2027 changes
- [Covered California](dashboard/covered-california.html) — PTC, expired enhanced credits, state subsidy, CSRs, penalty
- [Income & MAGI](dashboard/income-treatment.html) — Kalshi/rental/interest treatment
- [Other options](dashboard/other-options.html) — EMTALA, charity care, STLDI ban, COBRA, Medicare
- [Flagged for Review](dashboard/flagged-for-review.html) — all unverified values (left blank) + irregularities
- [Sources & methodology](dashboard/sources.html) — 54 cited sources with type labels

Generated from `data/*.csv` (9 tables, 120 rows — 108 rule/data rows, 106 verified and 2 blank-unverified, plus a 12-item flagged registry — each row with a status and source URL; counts after the 2026-10-18 re-verification sessions, incl. `arena/da6d01ac`) by
`scripts/build.py` (templates in `site_src/*.tmpl`); `scripts/validate.py` enforces the
verification standard (official https source link on every verified row; blank values on
unverified rows; link and placeholder checks).

All three publications cross-link and follow the same verification standard: every
factual table row links an official source (or is explicitly flagged); unknown or
unresolvable values are left blank and published on a Flagged for Review page; no personal
eligibility is inferred. Research snapshot: **2026-10-18**.

## 3. Verification dashboard (`docs/`) — session `arena/690e8271`

- [Dashboard home](docs/index.html) — executive summary, the numbers that matter, action checklist
- [Coverage & pathways](docs/options.html) — decision tree, ranked compliance pathways, the premium-tax-credit trap
- [Income sources](docs/income.html) — Kalshi, rental income and savings interest vs the $580 test
- [Federal law](docs/federal.html) — P.L. 119-21 §71119, SSA §1902(xx), 42 CFR §§435.550–435.563 in detail
- [California](docs/california.html) — WIC §14005.69, SB 164, AB 2161, AB 2208 status, DHCS letters, timeline
- [Flagged for Review](docs/flagged.html) — 23 flags plus 7 categories of value deliberately left blank
- [Source register](docs/sources.html) — 73 official primary sources with retrieval notes

Generated from `data/*.json` (5 row files plus a 73-entry source register) by `build_site.py`
(Python 3 standard library only, no CDN or external runtime dependency). Every table row carries a
pinpoint source chip — e.g. `eCFR · 42 CFR 435.552`, `CA LegInfo · WIC § 14005.69`,
`DHCS/MCED · MEDIL I 26-25`, `Fed. Reg. · 91 FR 33348` — linking straight to the provision the row
rests on. A row that has no official source renders a visible **BLANK — unverified** badge instead
of a value.

`.github/workflows/build-check.yml` is a **blocking, network-free** gate: it validates the JSON,
checks that every cited source id resolves, and rebuilds the site into a temp directory and diffs
it against the committed `docs/` (`python3 build_site.py --check`), so CI proves the published site
is current. `.github/workflows/link-check.yml` probes every cited external URL with retries and
reports OK/WARN/FAIL; it is deliberately **non-blocking**, because eCFR, the Federal Register,
leginfo and DHCS endpoints commonly reject non-browser clients — which is not evidence that a
citation is wrong. `scripts/check_links.py` runs the same probe locally.

This publication adds the verbatim regulatory and statutory text behind the conclusions in the two
sites above (42 CFR §§435.551–435.557, WIC §14005.69 in both its SB 164 and AB 2161 wordings), the
full California conditional-implementation safeguards, AB 2208's **not-enacted** status taken from
the official legislative history, and 11 flags not previously recorded — including that CMS-2454-IFC
was **corrected on 2026-06-29**, and that **two versions** of WIC §14005.69(e)(6) are in circulation.

## Research and limitations

Research was checked against official federal and California sources. Unknown personal figures
and unresolved classifications are intentionally blank or flagged, especially Kalshi contract
tax treatment, how specific rental/interest amounts fit the separate 2027 gross-income test,
and whether particular property-management/trading hours qualify. This is an informational
research brief, not a personal eligibility decision or legal/tax advice. See the three Flagged for Review pages —
[root](flagged.html) · [dashboard](dashboard/flagged-for-review.html) · [docs](docs/flagged.html) —
and the three source registers: [root](sources.html) · [dashboard](dashboard/sources.html) ·
[docs](docs/sources.html).

GitHub Pages publishes this repository from `main` at the repository root; `.nojekyll` keeps all
three sites served as plain static files. The verification dashboard is reachable at
https://buffedlizard55-lab.github.io/MaltaProj9/docs/.

See `COORDINATION.md` for the multi-session task board and publication record.
