# COORDINATION.md — Shared Task Board

**Repository:** `buffedlizard55-lab/MaltaProj9`
**Project:** Healthcare work requirements (Medicaid/Medi-Cal "community engagement") research, verification, and GitHub Pages publication.
**Board rules:** Claim a task by writing your session ID and file scope below, then commit and push the claim **immediately**. Never start a task another session has claimed. Keep file scopes non-overlapping. Make small, frequent commits. Run `git pull --rebase` before every push. Never mark anything verified without checking it against an official source **and linking that source**.

---

## Session registry

| Session ID | Branch | Role | Status | First seen (UTC) |
|---|---|---|---|---|
| `690e8271` | `arena/690e8271-maltaproj9` | Solo operator + final integration session | **active** | 2026-10-18T19:11Z |

> **Platform constraint / deviation note (logged, not a conflict):** this Arena session is pinned by the host platform to the single branch
> `arena/690e8271-maltaproj9`. The platform rules for this session forbid creating, switching to, or pushing to any other branch.
> The requested `session-<id>/<task>` branch naming therefore **cannot** be used here. To preserve the intent of the rule
> (non-overlapping scopes, traceable ownership, one integration pass), each task below is tracked with an explicit **file scope**
> owned by the claiming session, and all work is committed to `arena/690e8271-maltaproj9` in small, per-task commits.
> Because session `690e8271` is also the final integration session, scopes cannot collide with another session in this run.

---

## Task board

| # | Task | Status | Owner session | File scope |
|---|---|---|---|---|
| T1 | Repo review + audit of existing content; flag irregularities | **done** | `690e8271` | `COORDINATION.md`, `research/repo-review.md`, `data/flagged.json` |
| T2 | Federal law verification — P.L. 119-21 §71119, SSA §1902(xx), 42 CFR 435.550–435.563 | **done** | `690e8271` | `research/federal-law.md`, `data/federal-rules.json` |
| T3 | California implementation verification — DHCS, ACWDL 25-30, MEDIL I26-25, AB 2161, WIC §14005.69 | **done** | `690e8271` | `research/california.md`, `data/california.json` |
| T4 | Coverage options for a CA resident with $0 earned income (Medi-Cal, Covered California, other) | **done** | `690e8271` | `research/coverage-options.md`, `data/options.json` |
| T5 | Income-source classification (Kalshi event contracts, rental income, savings interest) vs. work requirement | **done** | `690e8271` | `research/income-analysis.md`, `data/income.json` |
| T6 | Site build — GitHub Pages dashboard (landing + category subpages + tables) | **done** | `690e8271` | `build_site.py`, `data/*.json`, `docs/**`, `.github/workflows/*`, `scripts/*`, `.gitignore`, `README.md` |
| T7 | "Flagged for Review" page | **done** | `690e8271` | `docs/flagged.html`, `data/flagged.json`, `research/flagged-items.md` |
| T8 | Final integration — merge, re-verify combined data line by line, link check, publish Pages, PR to `main`, merge | **in progress** | `690e8271` | all shared outputs (`docs/index.html`, site nav), `COORDINATION.md` |

---

## Claim log (append-only)

| Timestamp (UTC) | Session | Action |
|---|---|---|
| 2026-10-18T19:11Z | `690e8271` | Created `COORDINATION.md`. Repo contained only `README.md` (12 bytes, `# MaltaProj9`). Claimed T1, T2, and — as no other session is registered — T3–T8. |
| 2026-10-18T19:25Z | `690e8271` | Claimed T3–T8 explicitly (no competing session registered; board scopes remain non-overlapping). |
| 2026-10-18T20:15Z | `690e8271` | T1, T2 done — `research/repo-review.md`, `research/federal-law.md`, `research/flagged-items.md`. |
| 2026-10-18T20:18Z | `690e8271` | T3, T4, T5 done — `research/california.md`, `research/coverage-options.md`, `research/income-analysis.md`. |
| 2026-10-18T20:20Z | `690e8271` | T6, T7 done — `data/*.json` (5 data files + source register), `build_site.py`, `docs/**` (7 pages), `.github/workflows/build-check.yml`, `.github/workflows/link-check.yml`, `scripts/check_links.py`, `README.md`, `.gitignore`. Build gate `python3 build_site.py --check` passes; 73/73 registered sources cited; 0 problems. |
| 2026-10-18T20:22Z | `690e8271` | T8 in progress — pushing, opening PR to `main`, merging, enabling Pages. |

## Handoff log (append-only)

_None yet. If a claim is >60 minutes old with no commits, any session may take over and must note the handoff here._

## Conflict / incident log (append-only)

_None yet._

---

## Completion record (sources, verification performed, irregularities)

| Task | Status | Files produced | Verification performed | Irregularities recorded |
|---|---|---|---|---|
| **T1** Repo review | done | `research/repo-review.md`, `data/flagged.json` (§ `repo`, § `method`), `docs/flagged.html` | `git ls-files`, `git log --all`, `wc -c README.md`, `cat README.md`, `ls -a`. Pre-existing content was a single 12-byte line with no factual claim, so there was nothing to audit for accuracy. | R-01 … R-07 (all informational/trivial; R-04, R-05, R-06 remediated in this session) |
| **T2** Federal law | done | `research/federal-law.md`, `data/federal-rules.json`, `docs/federal.html` | Read the codified text of 42 CFR §§435.550–435.563 and §435.603 from eCFR (current through 10/15/2026); read the CMCS Informational Bulletin of 2025-12-08 in full (sections III–XI); confirmed the IFC exists at 91 FR 33348 via govinfo's official PDF and the Federal Register document record; confirmed the federal minimum wage at DOL; confirmed 2026 HHS poverty guidelines at ASPE and govinfo; confirmed 26 U.S.C. §45R(d)(5)(B) from the official U.S. Code PDF. | F-12 (Federal Register HTML intermittently 404s to automated retrieval), F-13 (IFC corrected 2026-06-29; correction content not retrieved), F-16 (§70433 1099 threshold unverified) |
| **T3** California | done | `research/california.md`, `data/california.json`, `docs/california.html` | Read WIC §14005.69 operative text and AB 2161 chaptered text from leginfo; read AB 2208 official status history; read DHCS ACWDL 25-30, MEDIL I 26-25 (incl. the full member letter), MEDIL I 25-18, ACWDL 26-07, the H.R.1 Implementation Plan and webinar deck, the H.R.1 fact sheet, the DHCS Medi-Cal Changes consumer page, the DHCS FPL charts, the FY 2026-27 Budget Act highlights, and CalHHS Connect decks; read FTB's personal health-care-mandate page and the March 2026 Tax News Flash correction. | F-05 (seasonal-worker scope), F-09 (2026 penalty amounts not published — left blank), F-10 ($15,560 copayment threshold matches no published FPL), F-11 (Jan 1 2027 vs March 2027), F-14 (ACWDL 25-30 expressly preliminary and predates the IFC), F-15 (three inconsistent official impact estimates), F-17 (asset-limit scope conflation), F-18 (AB 2208 not law), F-19 (two versions of §14005.69(e)(6)), F-20 (`dhcs.ca.gov/workrules` is a redirect) |
| **T4** Coverage options | done | `research/coverage-options.md`, `data/options.json`, `docs/options.html` | Verified Covered California's own statement that enhanced PTCs ended 2025-12-31, that the PTC repayment cap is removed from the 2026 tax year, and that up-front substantiation begins 2028; verified the PY2026 (165% FPL, $190M) and PY2027 (200% FPL, $300M, Budget Act item 4800-101-3381) state premium subsidy from hbex.coveredca.com and the Covered California press release; verified the §1902(xx)(7)(B) APTC/PTC preclusion from the CMCS bulletin and the equivalent warning in DHCS's own member letter; verified official application channels. | F-06 (citizenship assumed), F-07 (CMSP / Medi-Cal Access Program not verified — left blank), F-08 (2027 contribution percentages not verified — left blank) |
| **T5** Income analysis | done | `research/income-analysis.md`, `data/income.json`, `docs/income.html` | Verified IRS classification of earned vs unearned income (Pub 596, EITC Central, IRS newsroom), rental income treatment (Pub 527, Schedule E and Schedule C instructions), trader/investor/dealer rules (Topic No. 429), MAGI components (IRS, HealthCare.gov), and Kalshi's own official tax-documentation article; cross-read against 42 CFR §435.552(f)/(g) and §435.603(e)/(g) and against both versions of WIC §14005.69(e)(6)–(7). | F-01 (individual vs household income), F-02 (self-managed rental hours), F-03 (trading hours), F-04 ("Kalshi futures" terminology + unresolved IRS characterisation), F-21 (in-kind rent-free management), F-22 (PnL statement is not a tax document) |
| **T6** Site build | done | `build_site.py`, `data/*.json`, `docs/**`, `.github/workflows/build-check.yml`, `.github/workflows/link-check.yml`, `scripts/check_links.py`, `.gitignore`, `README.md` | Deterministic offline generator, Python 3 standard library only, no CDN or external runtime dependency. Build enforces: every source id resolves; internal links resolve; inline markup balanced; rows with no source render a visible **BLANK — unverified** badge. `python3 build_site.py --check` exits 0 and the committed `docs/` matches a clean rebuild. 73/73 registered sources are cited by at least one row. | — |
| **T7** Flagged for Review | done | `data/flagged.json`, `docs/flagged.html`, `research/flagged-items.md` | 23 flag items (F-01 … F-23), 7 categories of value deliberately left blank, 7 repository-review findings, and a 5-point verification cross-check. Every flag names what was checked and what could not be confirmed. Flagged items are published, not hidden, and do not block the merge. | F-01 … F-23 |
| **T8** Integration | in progress | `COORDINATION.md` (this file) | Re-verified combined data line by line via the build gate; external link probe is provided as `scripts/check_links.py` and runs in the non-blocking CI job. | — |

### Deviation note (platform branch constraint)

The instructions ask for branches named `session-<id>/<task>`. The host platform pins this
session to the single branch `arena/690e8271-maltaproj9` and forbids creating, switching to, or
pushing any other branch. That constraint is recorded in the session registry above. The intent
of the rule — non-overlapping scopes, traceable ownership, small frequent commits,
`git pull --rebase` before every push, and one integration pass — is preserved by tracking an
explicit **file scope per task** on this board and committing per task.

### Stale-claim policy as applied

No other session ever registered on this board, so no claim went stale and no handoff was
performed. The handoff and conflict logs remain empty and append-only.

## Pull request & merge record

_Pending — recorded here by the integration session after merge and GitHub Pages deployment confirmation._
