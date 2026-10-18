# MaltaProj9 — California healthcare eligibility research

A source-linked, static research project explaining California Medi-Cal and Covered California
options for a U.S. citizen resident with no earned wages but possible rental, trading
(Kalshi), and savings-interest income. It covers the federal Medicaid community-engagement law
scheduled for 2027, California implementation materials, application routes, income treatment,
and unresolved items.

The repository contains **two complementary publications** built by parallel research sessions,
both verified against official sources on **October 18, 2026**:

## 1. Research brief (site root) — session `arena/63a8fb6e`

- [Executive summary](index.html)
- [Medi-Cal eligibility](eligibility.html)
- [2027 community-engagement requirements](work-rules.html)
- [Income and assets](income.html)
- [Coverage options and application](options.html)
- [California's help with $0 earned income](california-help.html) — AB 2161 protections, no-wages compliance routes, where to get help
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
- [Sources & methodology](dashboard/sources.html) — 62 cited sources with type labels

Generated from `data/*.csv` (9 tables, **204 rows** — 177 rule/data rows, 175 verified and 2 blank-unverified, plus a 27-item flagged registry — each row with a status and source URL; counts after the 2026-10-18 re-verification passes) by `scripts/build.py` (templates in `site_src/*.tmpl`); `scripts/validate.py` enforces the verification standard (official https source link on every verified row; blank values on unverified rows; link and placeholder checks).

As of that snapshot the dashboard holds **204 data rows** across 9 tables — **175 verified**, **2 rows with intentionally blank unverified values** (IN-08 Kalshi section 1256 character, IN-13 trading hours as work) — plus a **27-entry flagged registry** of official-source inconsistencies and unverifiable claims, and **62 distinct cited sources**. Sessions `arena/da6d01ac` and `arena/cbb12598` both ran independent verification passes; where their new rows collided on ID the conflict was resolved by renumbering one session's rows into the free range so **no row from either session was discarded** (see `COORDINATION.md`).

## 3. Verification dashboard (`docs/`) — session `arena/690e8271` (integrated by `arena/5c4d1423`)

- [Verification dashboard home](docs/index.html) — 73 registered official sources, pinpoint citations on every row
- [Federal law](docs/federal.html) — verbatim 42 CFR §§ 435.551–435.557 text, P.L. 119-21 §71119, CMS-2454-IFC
- [California](docs/california.html) — WIC § 14005.69 in both SB 164 and AB 2161 wordings, DHCS letters
- [Income](docs/income.html) · [Options](docs/options.html) — Kalshi/rental/interest analysis, coverage pathways
- [Flagged for Review](docs/flagged.html) — 23 items (F-01…F-23), incl. the 06/29/2026 Federal Register correction to CMS-2454-IFC
- [Sources](docs/sources.html) — the 73-source register with retrieval notes

Generated deterministically from `data/*.json` by `build_site.py`; CI verifies the committed
output with `python3 build_site.py --check` (`.github/workflows/build-check.yml`). Research
notes behind it live in `research/*.md`. This publication was built on a parallel session
branch (PR #11); because that branch's tree had diverged from later-merged corrections, its
additive content was integrated by session `arena/5c4d1423` without regressing `main`
(see `COORDINATION.md`).

All three sites cross-link to each other, and all follow the same verification standard: every
factual table row links an official source (or is explicitly flagged); unknown or
unresolvable values are left blank and published on a Flagged for Review page; no personal
eligibility is inferred. Research snapshot: **2026-10-18**.

## Research and limitations

Research was checked against official federal and California sources. Unknown personal figures
and unresolved classifications are intentionally blank or flagged, especially Kalshi contract
tax treatment, how specific rental/interest amounts fit the separate 2027 gross-income test,
and whether particular property-management/trading hours qualify. This is an informational
research brief, not a personal eligibility decision or legal/tax advice. See
[Flagged for Review](flagged.html) / [dashboard Flagged for Review](dashboard/flagged-for-review.html)
and the two sources pages: [root](sources.html) · [dashboard](dashboard/sources.html).

GitHub Pages publishes this repository from `main` at the repository root; `.nojekyll` keeps
both sites served as plain static files.

See `COORDINATION.md` for the multi-session task board and publication record.
