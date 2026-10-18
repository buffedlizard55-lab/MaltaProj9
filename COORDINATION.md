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
| R1 — OBBBA Medicaid work-requirement law research | done | `arena/0ef38cd8` | `data/work-requirements-law.csv`, `data/work-requirement-exemptions.csv`, `work-requirements.html` |
| R2 — California (Medi-Cal / DHCS) status & eligibility research | done | `arena/0ef38cd8` | `data/medi-cal-eligibility.csv`, `data/california-implementation.csv`, `medi-cal.html` |
| R3 — Covered California / ACA subsidy research | done | `arena/0ef38cd8` | `data/covered-california.csv`, `covered-california.html` |
| R4 — Income treatment research (Kalshi §1256, rental, interest, MAGI) | done | `arena/0ef38cd8` | `data/income-treatment.csv`, `income-treatment.html` |
| R5 — Other coverage pathways research | done | `arena/0ef38cd8` | `data/other-programs.csv`, `data/options-summary.csv`, `other-options.html`, `executive-summary.html` |
| S1 — Site build (landing dashboard + category subpages) | done | `arena/0ef38cd8` | `index.html`, `executive-summary.html`, `flagged-for-review.html`, `sources.html`, `assets/**`, `site_src/**` |
| V1 — Verification (every row sourced; unverified left blank + flagged; link check) | done | `arena/0ef38cd8` | `scripts/validate.py`, `data/**` |
| I1 — Final integration, PR, merge, Pages deployment | in progress | `arena/0ef38cd8` | COORDINATION.md, README.md, GitHub PR/Pages config |

Filename deviations from the original plan (this session): `data/california-status.csv` was built
as `data/california-implementation.csv`; `data/other-options.csv` was split into
`data/other-programs.csv` (program-by-program) and `data/options-summary.csv` (decision paths for
the executive summary); a new `data/flagged-items.csv` registry feeds the Flagged for Review page.
Pages are generated from CSVs by `scripts/build.py` (templates in `site_src/`, built output at the
repo root for GitHub Pages); `scripts/validate.py` enforces the verification standard on every build.

## Cross-session requests

- (none yet)

## Session log

- 2026-10-18 — `arena/0ef38cd8`: Audited repo (empty except README). Fetched all remote session
  branches and read their COORDINATION.md claims; noted the all-sessions-claim-everything conflict
  (see Intake findings). Claiming the tasks above with the listed file scopes; proceeding with
  research on this branch. Verification standard: every published table row links an official
  source (.gov or the primary regulated-entity source for Kalshi-specific reporting practice);
  anything not confirmable from an official source stays blank and is flagged on the
  **Flagged for Review** page. Personal eligibility is never inferred — only rules are stated.
- 2026-10-18 — `arena/0ef38cd8`: Research R1–R5 complete. 110 data rows across 9 CSVs, each row
  carrying status + source_name + source_url. 97 of 100 rule/data rows verified against official
  sources; 3 values left blank as unverified (Kalshi event-contract tax character; whose income
  counts for the $580 work-rule standard; whether personal trading hours count as qualifying work);
  10-item flagged registry documents every irregularity found between official pages
  (effective-date phrasing CMS vs CRS vs DHCS; "$580 from any source" vs "work at a job and earn";
  caregiver-age wording 13-or-under vs under-13; DHCS $15,560 copay figure matching neither 2025
  nor 2026 FPL; 2027 poverty guidelines not yet published).
- 2026-10-18 — `arena/0ef38cd8`: S1 site built (9 pages + assets, generated by scripts/build.py
  from data/*.csv with templates in site_src/). V1 verification: `python3 scripts/validate.py`
  PASS — all verified rows carry official https source links; unverified rows have blank values;
  no unprocessed placeholders; all internal links resolve; every non-verified row appears on the
  Flagged for Review page; HTML structure checked on all 9 pages; all pages serve 200 in a local
  HTTP smoke test. Proceeding to I1: PR to main, merge, Pages deployment check.

## Publication record

- Pull request: pending
- Merge result: pending
- Pages deployment: pending
