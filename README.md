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
- [Sources & methodology](dashboard/sources.html) — 50 cited sources with type labels

Generated from `data/*.csv` (9 tables, 110 rows, each row with a status and source URL) by
`scripts/build.py` (templates in `site_src/*.tmpl`); `scripts/validate.py` enforces the
verification standard (official https source link on every verified row; blank values on
unverified rows; link and placeholder checks).

Both sites cross-link to each other, and both follow the same verification standard: every
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
