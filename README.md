# MaltaProj9 — Medicaid / Medi-Cal Work Requirement Research Dashboard

A verified research dashboard on the new federal Medicaid **"community engagement"**
(work) requirement, with a specific focus on **California** and on the situation of a
California resident whose income comes from **event-contract trading, rental property and
savings interest** rather than from wages.

**Live site:** see the GitHub Pages deployment for this repository (Settings → Pages), or open
[`docs/index.html`](docs/index.html) locally.

---

## What this is

Section 71119 of **Public Law 119-21** (H.R. 1, enacted July 4, 2025) added
**subsection (xx) to section 1902 of the Social Security Act**, requiring states to condition
Medicaid eligibility for certain adults on demonstrating "community engagement". CMS
implemented it in **CMS-2454-IFC**, 91 FR 33348 (June 3, 2026), codified at
**42 CFR §§ 435.550–435.563**. California implemented it in
**Welfare & Institutions Code § 14005.69** (SB 164, Stats. 2026 Ch. 27, as amended by
**AB 2161**, Ch. 209, Stats. 2026).

This repository records what those instruments actually say, verified line by line
against official primary sources.

## Pages

| Page | Contents |
|---|---|
| `docs/index.html` | Dashboard — executive summary, the numbers that matter, "do this first" checklist |
| `docs/options.html` | Coverage options and compliance pathways, ranked; the premium-tax-credit trap; Marketplace subsidies; the California individual mandate |
| `docs/income.html` | How trading gains, rental income and savings interest are classified by the IRS, by Medicaid and by California |
| `docs/federal.html` | Federal statute and regulation, in detail |
| `docs/california.html` | California statute, DHCS guidance, timeline, income and asset limits |
| `docs/flagged.html` | **Flagged for Review** — irregularities, discrepancies, unverified values and deliberate blanks |
| `docs/sources.html` | Source register — every official primary source used, with retrieval notes |

## Verification standard

1. **Every table row carries at least one link to an official primary source.** Publishers used:
   `congress.gov`, `govinfo.gov`, `federalregister.gov`, `ecfr.gov`, `medicaid.gov`, `cms.gov`,
   `dol.gov`, `irs.gov`, `healthcare.gov`, `aspe.hhs.gov`, and California state government
   (`leginfo.legislature.ca.gov`, `dhcs.ca.gov`, `ftb.ca.gov`, `edd.ca.gov`, `chhs.ca.gov`,
   `coveredca.com` / `hbex.coveredca.com`). The single non-government source is Kalshi's own
   help centre, used only to record what the platform itself says it reports.
2. **If a value cannot be confirmed officially, it is left BLANK** and the item appears on the
   Flagged for Review page. Values are never inferred, estimated, or filled in from secondary
   sources.
3. **Secondary sources are never cited as authority.** Law-firm alerts, policy institutes,
   hospital and insurer associations, insurance and tax blogs and local news were used only to
   *locate* primary sources.
4. **Analysis is labelled as analysis**, and quotations are labelled as quotations.
5. **Flagged items do not block publication.** They are published on `docs/flagged.html` with
   what was checked and what could not be confirmed.

## Repository layout

```
COORDINATION.md        shared task board (parallel-session protocol)
README.md              this file
build_site.py          deterministic site generator (Python 3 standard library only)
scripts/check_links.py external URL verifier (used by the non-blocking CI job)
data/
  sources.json         source register — id, publisher, title, url, type, retrieval note
  federal-rules.json   federal statute and regulation rows
  california.json      California statute, DHCS guidance and state programmes rows
  income.json          income-source classification rows
  options.json         coverage options and compliance pathway rows
  flagged.json         flag register, deliberate blanks, repository review findings
research/
  repo-review.md       line-by-line audit of the repository as found
  federal-law.md       full federal verification trail with verbatim quotations
  california.md        full California verification trail with verbatim quotations
  income-analysis.md   income-source analysis with verbatim quotations
  coverage-options.md  coverage-option analysis with verbatim quotations
  flagged-items.md     narrative version of the flag register
docs/                  generated site — COMMITTED deliberately (GitHub Pages directory)
.github/workflows/
  build-check.yml      blocking, offline: rebuilds the site and diffs against docs/
  link-check.yml       non-blocking: probes every cited external URL
```

## Building the site

No dependencies beyond Python 3. The site is **generated**, so `data/*.json` is the source of
truth and `docs/` is committed output.

```bash
python3 build_site.py           # regenerate docs/ from data/
python3 build_site.py --check   # verify docs/ matches a clean rebuild (CI gate)
python3 scripts/check_links.py  # probe every cited external URL (needs network)
```

`build_site.py` enforces the verification standard mechanically: a row whose source id does not
resolve in `data/sources.json` fails the build, an internal link that does not resolve fails the
build, and any row with no source at all renders a visible **BLANK — unverified** badge.

## Local preview

```bash
cd docs && python3 -m http.server 8000 --bind 0.0.0.0
# then open http://localhost:8000/
```

## Disclaimer

**This is not legal, tax or medical advice.** It is a research and verification dashboard that
summarises published official sources and links to them. Confirm anything consequential with the
California Department of Health Care Services, your county Medi-Cal office, Covered California, a
licensed California attorney, or a CPA / enrolled agent.

## Coordination

`COORDINATION.md` is the shared task board for parallel working sessions. Read it before
claiming work; record sources, verification performed and irregularities when a task is done.
