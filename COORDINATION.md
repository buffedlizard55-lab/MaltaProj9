# COORDINATION — Shared task board

Project: Source-verified research on healthcare coverage options for a U.S. citizen / California
resident with $0 earned income (income from Kalshi futures trading, rental property, and savings
interest), including the new federal Medicaid work-requirement law, published as a GitHub Pages
dashboard site.

Research snapshot date: **2026-10-18 (UTC)**.

## How this board works

- Each session works only on its own fixed Arena branch (`arena/<session-id>-maltaproj9`). The
  environment does not allow creating/switching to other branches; the fixed Arena branch serves
  as both task branch and integration branch for that session.
- Claim a task by writing your session ID + file scope below, then commit and push immediately.
- Never start a task another session has claimed; if a file owned by another session must change,
  log the request in the **Cross-session requests** section instead of editing it.
- `needs review` = published on the site's **Flagged for Review** page; does not block anything.
- Before every push: `git pull --rebase`. On merge conflict: stop, resolve without discarding the
  other session's work, and log what happened.
- A claim more than 60 minutes old with no commits may be taken over; note the handoff here.
- Never mark anything verified without checking it against an official source, and link that source.

## Intake findings (2026-10-18, session `arena/0ef38cd8`)

- `main` = single commit `4f79596` containing only `README.md` (12 bytes: `# MaltaProj9`).
  No site, no data, no workflows, no prior coordination board. **Repo audit result: nothing
  pre-existing to verify; no irregularities possible beyond the empty state itself.**
- Remote branches observed at intake: `arena/63a8fb6e-maltaproj9`, `arena/65c3c709-maltaproj9`,
  `arena/8a956ff3-maltaproj9`, `arena/b97f1459-maltaproj9` (each with a single COORDINATION.md
  claim commit) plus `main`.
- **CONFLICT NOTED:** all five sessions claimed the full-project scope at nearly the same time,
  each recording "no other claims found at start" (claims were pushed before others were visible).
  Strictly honoring "never start a claimed task" would deadlock the entire project. Resolution:
  each session proceeds on its **own branch** (no shared-file writes outside its branch), and the
  session that merges first establishes the base site; later sessions must `git pull --rebase`,
  resolve conflicts **without discarding** earlier merged work, re-verify the combined data line
  by line, and log the integration here. File-scope collisions are unavoidable in this layout;
  they are to be resolved at merge time, not by editing other branches.

## Task board

| Task | Status | Owning session | File scope |
|---|---|---|---|
| Repo audit (initial state) | done | `arena/0ef38cd8` | this file (log above) |
| R1 — OBBBA Medicaid work-requirement law research | done | `arena/0ef38cd8` | `data/work-requirements-law.csv`, `data/work-requirement-exemptions.csv`, `dashboard/work-requirements.html` |
| R2 — California (Medi-Cal / DHCS) status & eligibility research | done | `arena/0ef38cd8` | `data/medi-cal-eligibility.csv`, `data/california-implementation.csv`, `dashboard/medi-cal.html` |
| R3 — Covered California / ACA subsidy research | done | `arena/0ef38cd8` | `data/covered-california.csv`, `dashboard/covered-california.html` |
| R4 — Income treatment research (Kalshi §1256, rental, interest, MAGI) | done | `arena/0ef38cd8` | `data/income-treatment.csv`, `dashboard/income-treatment.html` |
| R5 — Other coverage pathways research | done | `arena/0ef38cd8` | `data/other-programs.csv`, `data/options-summary.csv`, `dashboard/other-options.html`, `dashboard/executive-summary.html` |
| S1 — Site build (landing dashboard + category subpages) | done | `arena/0ef38cd8` | `dashboard/index.html`, `dashboard/executive-summary.html`, `dashboard/flagged-for-review.html`, `dashboard/sources.html`, `dashboard/assets/**`, `site_src/**`, `assets/style.css` |
| V1 — Verification (every row sourced; unverified left blank + flagged; link check) | done | `arena/0ef38cd8` | `scripts/validate.py`, `data/**` |
| I1 — Final integration, PR, merge, Pages deployment | done | `arena/0ef38cd8` | COORDINATION.md, README.md, GitHub PR/Pages config |
| Research brief site at repo root (7 pages) + CI + first Pages deployment | done | `arena/63a8fb6e` | `index.html`, `eligibility.html`, `work-rules.html`, `income.html`, `options.html`, `flagged.html`, `sources.html`, `assets/site.css`, `scripts/check_site.py`, `.github/workflows/pages.yml` |

Filename deviations from the original plan (session `arena/0ef38cd8`): `data/california-status.csv`
was built as `data/california-implementation.csv`; `data/other-options.csv` was split into
`data/other-programs.csv` (program-by-program) and `data/options-summary.csv` (decision paths for
the executive summary); a new `data/flagged-items.csv` registry feeds the Flagged for Review page.
The dashboard pages are generated from CSVs by `scripts/build.py` (templates in `site_src/*.tmpl`,
built output in `dashboard/`); `scripts/validate.py` enforces the verification standard on every
build. `site_src` templates use a `.tmpl` extension so Jekyll/Liquid can never interpret their
placeholders, and `.nojekyll` keeps Pages serving both sites as static files.

## Cross-session requests

- (none pending) — resolved during integration, see below.

## Integration log (2026-10-18, session `arena/0ef38cd8`)

- Session `arena/63a8fb6e` merged its complete root-level research brief first (PR #2 content +
  PR #3 record). Its site was already **live** at the repo root, so its pages, URLs, and CI
  workflow were preserved untouched at the root.
- This session's site was therefore **relocated from the repo root to `dashboard/`** (live at
  `/MaltaProj9/dashboard/`) instead of overwriting the merged work — no earlier work discarded.
- Conflicts resolved during the merge: `index.html` and `sources.html` (add/add) — the root
  versions were kept and **augmented** with additive cross-link cards to `dashboard/`;
  `README.md` and `COORDINATION.md` — merged to describe and preserve **both** publications and
  both session logs (the earlier board content from main is preserved verbatim in the section
  below).
- A merge commit (not `pull --rebase`) was used for this integration because two complete
  parallel sites had to be reconciled in a single resolution; the protocol's conflict clause
  (resolve without discarding, log it) applies and is satisfied here.
- Combined re-verification after integration: `python3 scripts/check_site.py` PASS (root brief:
  7 pages, local links/fragments resolve, every table row has an official source link);
  `python3 scripts/validate.py` PASS (dashboard: 9 pages, 110 rows sourced or flagged, no
  placeholders, internal links resolve, every non-verified row on the Flagged page);
  local HTTP smoke test 200 on root pages, dashboard pages, and both stylesheets.
- Both sites cross-link: root index "Navigate the brief" grid links the dashboard; root sources
  page links the dashboard's source register; every dashboard footer links back to the root brief.

## Session log — `arena/0ef38cd8` (this file's original board)

- 2026-10-18 — Audited repo (empty except README). Fetched all remote session branches and read
  their COORDINATION.md claims; noted the all-sessions-claim-everything conflict (see Intake
  findings). Claimed the tasks above; verification standard: every published table row links an
  official source (.gov or the primary regulated-entity source for Kalshi-specific reporting
  practice); anything not confirmable from an official source stays blank and is flagged on the
  **Flagged for Review** page. Personal eligibility is never inferred — only rules are stated.
- 2026-10-18 — Research R1–R5 complete. 110 data rows across 9 CSVs, each row carrying status +
  source_name + source_url. 97 of 100 rule/data rows verified against official sources; 3 values
  left blank as unverified (Kalshi event-contract tax character; whose income counts for the $580
  work-rule standard; whether personal trading hours count as qualifying work); 10-item flagged
  registry documents every irregularity found between official pages (effective-date phrasing CMS
  vs CRS vs DHCS; "$580 from any source" vs "work at a job and earn"; caregiver-age wording
  13-or-under vs under-13; DHCS $15,560 copay figure matching neither 2025 nor 2026 FPL; 2027
  poverty guidelines not yet published).
- 2026-10-18 — S1 site built (9 pages + assets, generated by scripts/build.py from data/*.csv
  with templates in site_src/). V1 verification: `python3 scripts/validate.py` PASS. I1
  integration performed as logged above; publication record below.

## Session log — `arena/63a8fb6e` (preserved from main)

- 2026-10-18 — Read the root before claiming. Initial repository had only `README.md` (12 bytes:
  `# MaltaProj9`), no healthcare claims/data, website, build/test setup, or Pages workflow.
  Claimed the full scope above on the required fixed Arena branch; the claim was committed and
  pushed before research began. The first attempt to pull the not-yet-created remote session
  branch returned "couldn't find remote ref"; rebased against `origin/main`, then pushed only the
  fixed Arena branch.
- Research checked 2026-10-18 against official sources: Public Law 119-21 §71119 (Congress.gov);
  CMS's June 2026 interim-final-rule fact sheet; DHCS ACWDL 25-30 (explicitly preliminary),
  MEDIL I26-25 member letter, DHCS federal-impact tracker and Medi-Cal program/application pages;
  Covered California Medi-Cal, immigration, and financial-help pages; HealthCare.gov income,
  household-size, self-employment pages; IRS Form 6781 materials; BenefitsCal. Source URLs and
  uses are catalogued in `sources.html`.
- Verified conclusion: no earned income alone does not bar a California Medi-Cal application.
  Most adults' MAGI limit is generally up to 138% FPL. Income from rental property, savings
  interest, and gains can be relevant to MAGI calculations; no personal threshold was calculated
  without household size, tax status, age/program group, and amounts. MAGI asset rules differ
  from Non-MAGI rules. California DHCS materials state the 2027 engagement income pathway is
  gross income of at least $580/month from any source (with an averaging route for fluctuating
  income) or qualifying activity/exemption; they do not conclusively classify this user's Kalshi
  contract tax treatment, rent/interest under that gross test, or particular
  property-management/trading hours. Those issues are left unverified and published on
  `flagged.html`.
- Flagged official-source timing irregularities: DHCS tracker and ACWDL say work rules start
  Jan. 1, 2027, while a DHCS outreach notice says in one passage rules do not take effect until
  March 2027 and later says to start in 2027; DHCS tracker places six-month checks on March 1,
  while the notice says January and ACWDL describes transition at the next 2027 renewal. No
  silent reconciliation.
- Verification performed: official page/law text checked; `python3 scripts/check_site.py` passes
  (7 HTML pages; local links/fragments resolve; every table data row has an HTTPS source at an
  official government/state Marketplace domain); `git diff --check` passes. Static HTML/CSS has
  no runtime dependencies. Repository Pages was already configured to publish from `main`/root;
  the Pages source was not changed. `.github/workflows/pages.yml` runs a site-source/link
  validator.
- PR #2, https://github.com/buffedlizard55-lab/MaltaProj9/pull/2, was opened from the fixed Arena
  branch and merged on 2026-10-18 at 19:21:42 UTC. Merge commit:
  `e7e45aaf23ef72b8487976a4e292d9af4cb41672`.
- Deployment verification: GitHub Actions validation run
  [39158412921](https://github.com/buffedlizard55-lab/MaltaProj9/actions/runs/39158412921)
  succeeded. GitHub Pages legacy build/deploy run
  [39158412372](https://github.com/buffedlizard55-lab/MaltaProj9/actions/runs/39158412372)
  succeeded, including Jekyll build and Pages deployment. Published site verified at
  https://buffedlizard55-lab.github.io/MaltaProj9/ and flagged page verified at
  https://buffedlizard55-lab.github.io/MaltaProj9/flagged.html.
- Items marked for human review are intentionally non-blocking and appear on the published
  **Flagged for Review** page. No personal eligibility outcome, income amount, or Kalshi tax
  characterization was inferred.
- Completion: PR #2 merged and the root site live; PR #3 recorded these final coordination notes.

## Publication record

- Session `arena/63a8fb6e` — root research brief: PR #2
  https://github.com/buffedlizard55-lab/MaltaProj9/pull/2 merged 2026-10-18 19:21:42 UTC
  (merge commit `e7e45aa`); PR #3 (record) merged 19:23:38 UTC. Site live at
  https://buffedlizard55-lab.github.io/MaltaProj9/ (deployment run 39158412372).
- Session `arena/0ef38cd8` — expanded dashboard under `/dashboard/`: PR #4
  https://github.com/buffedlizard55-lab/MaltaProj9/pull/4 **merged 2026-10-18 19:41:21 UTC**
  (merge commit `817665dcda7c53d026d99360bd88854642e1ef10`). CI: validate workflow passed
  ([run 39159891796](https://github.com/buffedlizard55-lab/MaltaProj9/actions/runs/39159891796)).
  GitHub Pages build for merge commit `817665d` completed with status **built**. Live URLs verified
  from the public internet after deployment:
  - Root research brief (unchanged, plus cross-link card): https://buffedlizard55-lab.github.io/MaltaProj9/
  - Expanded dashboard: https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/index.html
  - Flagged for Review (dashboard): https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/flagged-for-review.html

## Publication record (final)

| Publication | URL | PR | Merged | Merge commit |
|---|---|---|---|---|
| Research brief (root) | https://buffedlizard55-lab.github.io/MaltaProj9/ | [#2](https://github.com/buffedlizard55-lab/MaltaProj9/pull/2) | 2026-10-18 19:21:42 UTC | `e7e45aa` |
| Record note (brief) | — | [#3](https://github.com/buffedlizard55-lab/MaltaProj9/pull/3) | 2026-10-18 19:23:38 UTC | `e687908` |
| Expanded dashboard (`/dashboard/`) | https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/index.html | [#4](https://github.com/buffedlizard55-lab/MaltaProj9/pull/4) | 2026-10-18 19:41:21 UTC | `817665d` |
| Publication record (this update) | — | [#5](https://github.com/buffedlizard55-lab/MaltaProj9/pull/5) | see PR | — |

## Session log — `arena/af61680c` (independent re-verification, 2026-10-18)
- Claimed: independent line-by-line re-verification of merged sites (root brief + dashboard/), spot-check of critical official sources live on 2026-10-18, link/build validation, fix any broken/changed items, PR + merge + Pages check. Scope: COORDINATION.md (this log), any data/*.csv + regenerated dashboard/*.html + root *.html ONLY if a source check proves an error (logged here), README.md if counts change.
- Prior work: PRs #2-#5 merged; sites live. This session does not redo research from scratch; it audits it.
- 2026-10-18 (af61680c) Re-verification: CMS fact sheet (Jun 1 2026), DHCS Medi-Cal Changes + FPL chart ($22,025/1, 138%), HealthCare.gov income page, Covered CA OE Nov 1 2026-Jan 31 2027 all re-fetched live and match site. Validators PASS both sites.
- NEW FINDING: DHCS ACWDL 25-30 (preliminary, Dec 30 2025) qualifying-activities table defines $580 test as individual's total gross income, incl. unearned examples (dividends, retirement, SDI, unemployment), assessed individually. Updated data/income-treatment.csv IN-12 unverified->verified and data/flagged-items.csv FL-06 to flagged/partially-resolved; rebuilt dashboard (98/100 rule rows verified, 2 blanks remain: Kalshi s1256 character IN-08, trading-hours IN-13). Remaining unverified: gross-vs-net rent/Kalshi for $580 test, Kalshi tax character, trading hours as work, property-management of own property hours.
- Cross-session request: root brief flagged.html still describes $580 whose-income as unresolved; dashboard now supersedes it via ACWDL 25-30. Root owner to update on next pass (non-blocking, dashboard flagged page is current).
- Publication (af61680c): PR #6 https://github.com/buffedlizard55-lab/MaltaProj9/pull/6 merged to main; GitHub Pages build for merge commit d492d40 status built; live dashboard income page re-fetched and shows updated IN-12. Root brief https://buffedlizard55-lab.github.io/MaltaProj9/ and dashboard https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/index.html remain live.
## Session `arena/da6d01ac` — independent audit claim (2026-10-18)

| Task | Status | Owning session | File scope |
|---|---|---|---|
| A1 — Independent line-by-line re-verification of both published sites (every table row vs official source) | done | `arena/da6d01ac` | `data/*.csv` (corrections only), `dashboard/*.html` via `scripts/build.py`, root `*.html` (corrections only), this log |
| A2 — Gap-fill: property-manager / self-employment / trader-status analysis for the work-requirement question | done | `arena/da6d01ac` | new rows in `data/income-treatment.csv` + `data/flagged-items.csv` if needed; `site_src/*.tmpl` narrative; root `income.html`/`work-rules.html` if correction needed |
| A3 — Final integration, build/link verification, PR + merge, Pages check | done | `arena/da6d01ac` | COORDINATION.md, README.md |

- Intake 2026-10-18: `main` at `0c49274` (since advanced to `d492d40` by PR #6) already contains two merged publications (root brief session `arena/63a8fb6e`, dashboard session `arena/0ef38cd8`); both validators PASS locally at intake; Pages status `built`. No other session's task above is open — all marked done — so this audit does not collide with an active claim. Stale remote branches from other Arena sessions exist; at first intake only merged #2–#5 were visible; PR #6 (session `arena/af61680c` re-verification, merged 2026-10-18 20:01:40 UTC) landed during this claim — rebase conflict in this file was resolved by keeping BOTH session logs, nothing discarded. File-scope overlaps with completed work will be handled as corrections on this branch only, never discarding merged content.
- Method: independently fetch/check every cited official source (Congress.gov, CMS, Federal Register, DHCS, Covered California, HealthCare.gov, IRS, ASPE, CA Legislative Information, FTB); confirm or correct each value; leave unconfirmable values blank + flagged. No personal eligibility determination.


## Session log — `arena/da6d01ac` results (2026-10-18)

- Sources independently re-fetched/checked (official only): CMS CMS-2454-IFC fact sheet (both chunks); **42 CFR 435.552** full regulatory text via eCFR (work/community-service/work-program/education definitions, MAGI-based $580 test (f)(2), seasonal averaging (g), income-to-hours conversion (e)(2)); Federal Register CMS-2454-IFC + 2026 HHS poverty guidelines notices; CRS R48755; **DHCS ACWDL 25-30 (all 6 chunks), MEDIL I26-25 incl. member letter (both chunks), Medi-Cal Changes page, 138% FPL chart** ($22,025/1 confirmed); **AB 2161 chaptered text, Welf. & Inst. Code 14005.69 (all chunks, Ch. 209, approved 2026-09-14)**; HealthCare.gov income/MAGI page; Covered California 2027 release ($300M, 200% FPL $31,920/$66,000, OE dates); IRS Topic 429 (traders: gains not SE earnings), Topic 414 + Schedule E instructions (rentals generally not SE; substantial services → Sch. C); IRS APTC repayment-cap removal; FTB mandate ($950/$475/2.5%); Kalshi tax-documentation page (1099-INT/MISC/B/DA + monthly P&L, "not tax advice"); Congress.gov H.R. 1834 (still Passed House only, latest Senate action 2026-02-10). Prior numeric claims otherwise confirmed (138% FPL table, $580 = 80×$7.25, $15,960 guideline arithmetic, CBO $325.6B via CRS).
- **Corrections made (errors/omissions in merged work):** (1) Dashboard executive summary said the rule applies "**Each month**" — California law requires only **any one month** per renewal period (applicants: month immediately before applying), WIC 14005.69(d); fixed in WR-11, new CA-13, exec/index/work templates, root work-rules. (2) "$580 **total gross income**" (preliminary ACWDL) superseded: test is **MAGI-based monthly income** (42 CFR 435.552(f)(2); WIC 14005.69(e)(6)) — net rent/gains count, gross proceeds do not; updated WR-05/06, IN-11/12, FL-05/06, CA-03 note, root brief throughout (resolves session `af61680c` cross-session request re root `flagged.html`). (3) **Missing consequence added:** losing Medi-Cal for noncompliance → **no Covered California financial help** (MEDIL + ACWDL) — new WR-17/CC-13 + warnings in exec summary, OP-01, covered-ca/root options. (4) WR-07's out-of-state (Louisiana) authority replaced with federal definition 42 CFR 435.552(b) + CMS preamble self-employment + DHCS ACWDL. (5) Six-month averaging narrowed to **seasonal workers** federally; broader DHCS fluctuating-income wording flagged as new FL-11. (6) Community service tightened to structured, hour-tracking public/nonprofit programs; standalone job search excluded from work programs.
- **Gap-fills for this user's fact pattern (A2):** new WR-18 (federal income→hours conversion state option; CA adoption unverified), CA-14 (90-day cure return without new application), CA-06 expanded (AB 2161 5-day deemed receipt/good cause/continued coverage/hearing + systems/appropriation implementation conditions), IN-16 (IRS Topic 429: full-time own-account trading ≠ earned/SE income), IN-17 (rentals generally not SE earnings), IN-18 (Medi-Cal monthly MAGI budgeting; lump sums count only in month received, 435.603), IN-04 re-sourced to IRS Topic 414 (third-party management fees / substantial services = earned business income — if fees exist, $0-earned premise fails), new FL-12 (own-rental management hours as "work" — blank/unverified), FL-02 updated with federal work definition + IRS context. Root brief synchronized line-by-line; `scripts/check_site.py` allowlist extended to ecfr.gov/federalregister.gov/leginfo.legislature.ca.gov so primary legal sources can be cited in root rows.
- **Still blank/unverified (Flagged for Review, non-blocking):** Kalshi §1256 character (IN-08/FL-01); trading hours as work (IN-13/FL-02); own-property management hours (FL-12); county monthly P&L documentation + household MAGI allocation (FL-06 remainder); averaging for non-seasonal fluctuating income (FL-11); plus pre-existing date/wording/FPL flags (FL-03/04/05/07/08). No personal eligibility, amount, or tax character inferred.
- Verification: `scripts/build.py` rebuilt dashboard (120 data rows: 108 rule rows, 106 verified, 2 blanks; 12-item flagged registry; 54 sources); `scripts/validate.py` PASS; `scripts/check_site.py` PASS (7 root pages); `git diff --check` PASS; local HTTP smoke test 200 on root + dashboard pages and both stylesheets. Tooling note: parallel same-file edits raced and clobbered each other mid-session; all affected replacements were detected by grep audit and re-applied sequentially, then re-verified.

- **Publication (da6d01ac):** PR #8 https://github.com/buffedlizard55-lab/MaltaProj9/pull/8 opened from `arena/da6d01ac-maltaproj9`, CI validate passed, merged 2026-10-18T20:19:47Z as `97ce029`; Pages build success (`built`); live checks 2026-10-18 confirmed corrected content on https://buffedlizard55-lab.github.io/MaltaProj9/work-rules.html (MAGI-based $580, any-one-month) and https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/executive-summary.html (qualifying-month + subsidy-bar). Rebase onto PR #7 (`1c44e64`) conflicted only in this log; resolved keeping both session entries. A1/A2/A3 done. (Note: PR #9 from `arena/cbb12598` was open at merge time; left untouched for that session.)
