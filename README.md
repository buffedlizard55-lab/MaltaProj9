# MaltaProj9 — Healthcare Options Research (California, $0 Earned Income)

Source-verified research dashboard, published with GitHub Pages at:
**https://buffedlizard55-lab.github.io/MaltaProj9/**

Built for the question: a U.S. citizen living in California (ages 19–64, assumed), with **$0
earned income** — money comes from **Kalshi trading**, **rental property**, and **savings
interest** — what healthcare coverage is available, what does the new federal Medicaid
work-requirement law actually require, and what does California do for people with no earned
income?

## Site pages

| Page | Contents |
|---|---|
| `index.html` | Dashboard: key findings, key numbers, timeline, links |
| `executive-summary.html` | Bottom line, decision paths, the new law in plain English, action checklist |
| `work-requirements.html` | OBBBA §71119 + CMS-2454-IFC: 80 hours, $580 income standard, exemptions, CA rollout |
| `medi-cal.html` | Eligibility (138% FPL), MAGI rules, no asset test, application channels, 2027 changes |
| `covered-california.html` | Premium tax credits, expired enhanced credits, state subsidy, CSRs, penalty |
| `income-treatment.html` | Kalshi trading, rental income, interest: taxes, MAGI, and the work rule |
| `other-options.html` | EMTALA, hospital charity care, STLDI ban, sharing ministries, COBRA, Medicare |
| `flagged-for-review.html` | Every unverified value (left blank) and irregularity between official sources |
| `sources.html` | Full source list with type labels + methodology |

## Repository layout

- `data/*.csv` — the single source of truth: 9 tables, 110 rows, every row with a status
  (`verified` / `flagged` / `unverified`), source name, and source URL.
- `site_src/*.html` — page templates (with `{{TABLE:…}}` placeholders).
- `scripts/build.py` — generates the site pages at the repo root from the CSVs.
- `scripts/validate.py` — enforces the verification standard (see below) and link checks.
- `assets/style.css` — dashboard styling. `.nojekyll` present so Pages serves files as-is.

## Verification standard

- Every table row must link an official source (`.gov`, Covered California, or Kalshi's official
  help center for Kalshi-specific reporting practice). `scripts/validate.py` fails the build
  otherwise.
- If a value cannot be confirmed from an official source, it is **left blank**, marked
  *unverified*, and published on the **Flagged for Review** page — never inferred.
- Personal eligibility is never determined; only rules and thresholds are stated.
- Trusted secondary sources (KFF, CHCF, Justice in Aging, CRS-linked, Bipartisan Policy Center)
  are labeled as such on the sources page and never used as a table row's sole source.

Research snapshot: **2026-10-18**. Rebuild with `python3 scripts/build.py`; verify with
`python3 scripts/validate.py`.

## Disclaimer

Informational research only — not legal, tax, or medical advice, and not an eligibility
determination. Rules change; verify current details with DHCS, your county Medi-Cal office,
Covered California, CMS, and the IRS, and consult qualified professionals before acting.

See `COORDINATION.md` for the multi-session task board and publication record.
