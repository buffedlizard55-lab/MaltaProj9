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
| T1 | Repo review + audit of existing content; flag irregularities | **in progress** | `690e8271` | `COORDINATION.md`, `research/repo-review.md`, `data/flagged.json` |
| T2 | Federal law verification — P.L. 119-21 §71119, SSA §1902(xx), 42 CFR 435.550–435.563 | **in progress** | `690e8271` | `research/federal-law.md`, `data/federal-rules.json` |
| T3 | California implementation verification — DHCS, ACWDL 25-30, MEDIL I25-18, AB 2161, CA Welfare & Institutions Code | **unclaimed** | — | `research/california.md`, `data/california.json` |
| T4 | Coverage options for a CA resident with $0 earned income (Medi-Cal, Covered California, other) | **unclaimed** | — | `research/coverage-options.md`, `data/options.json` |
| T5 | Income-source classification (Kalshi event contracts, rental income, savings interest) vs. work requirement | **unclaimed** | — | `research/income-analysis.md`, `data/income.json` |
| T6 | Site build — GitHub Pages dashboard (landing + category subpages + tables) | **unclaimed** | — | `site/**` |
| T7 | "Flagged for Review" page | **unclaimed** | — | `site/flagged.html`, `data/flagged.json` |
| T8 | Final integration — merge, re-verify combined data line by line, link check, publish Pages, PR to `main`, merge | **unclaimed** | — | all shared outputs (`site/index.html`, `site/nav`), `COORDINATION.md` |

---

## Claim log (append-only)

| Timestamp (UTC) | Session | Action |
|---|---|---|
| 2026-10-18T19:11Z | `690e8271` | Created `COORDINATION.md`. Repo contained only `README.md` (12 bytes, `# MaltaProj9`). Claimed T1, T2, and — as no other session is registered — T3–T8. |

## Handoff log (append-only)

_None yet. If a claim is >60 minutes old with no commits, any session may take over and must note the handoff here._

## Conflict / incident log (append-only)

_None yet._

---

## Completion record (sources, verification performed, irregularities)

_Filled in per task as tasks are marked `done`. See `research/` for full source trails and `site/flagged.html` for the published "Flagged for Review" page._

## Pull request & merge record

_Pending — recorded here by the integration session after merge and GitHub Pages deployment confirmation._
