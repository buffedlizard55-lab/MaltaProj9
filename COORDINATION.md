# Coordination board

## Session and branch

- Owning session: `8a956ff3` (Arena).
- Required working / integration branch: `arena/8a956ff3-maltaproj9`.
- Opened: 2026-10-18 (UTC).
- The repository initially contains only `README.md` and its Git history. No existing coordination board or other remote working branches were present at intake.
- The execution environment requires this fixed branch; no alternate session branch or worktree will be created. This session will perform sequential research and final integration. Other sessions must not edit the scopes claimed below.
- Coordination updates are shared metadata. A `needs review` item must appear on the site's **Flagged for Review** page and does not block publication.

## Task board

| Task | Status | Owning session | File scope | Verification / handoff |
| --- | --- | --- | --- | --- |
| R1 — Official-source legal, California eligibility, income and activity research | in progress | `8a956ff3` | `research/**` | Verify source text before promoting any claim; preserve unresolved points and source links. |
| I1 — Shared site integration | unclaimed by this session; ownership request logged | earliest integration claimant: `b97f1459`; root-file claim: `63a8fb6e` | Root site, `assets/**`, `data/**`, `docs/**`, shared navigation, `README.md` | Concurrent intake claims discovered; no shared implementation files edited here. See `research/COORDINATION-HANDOFF.md`. |
| Q1 — Independent evidence/row audit and research output | in progress | `8a956ff3` | `research/**` only | Complete reproducible evidence and table checks in the unique research scope; do not edit other sessions' scripts/workflows. |
| P1 — Research PR / integration handoff / live verification | in progress | `8a956ff3` | `COORDINATION.md`, `research/**`; GitHub PR metadata | Pull with rebase before every push; coordinate shared integration rather than race to overwrite it. |

## Verification standard

1. Official federal or California sources only for legal/eligibility/tax assertions. Each published table row must link an official source.
2. Distinguish enacted statutory text, agency implementation guidance, IRS tax rules, and analysis/recommendations.
3. A source confirming a general rule does not determine this user's eligibility or classify a particular Kalshi contract. Unknown personal facts and unconfirmed implementation details remain blank and are flagged.
4. Research snapshot date: **2026-10-18**. An older source's date and any future effective date must remain distinguishable.
5. Source access, row-by-row verification and unresolved inconsistencies will be documented in `research/` and on the site.

## Activity log

- 2026-10-18 — `8a956ff3`: Read the initial repository and remote branch list. Only `main` existed remotely; working branch is clean. Existing Pages configuration serves `main` from `/` at <https://buffedlizard55-lab.github.io/MaltaProj9/>. Claimed the above scopes before starting substantive work. No concurrent claim or merge conflict found.

- 2026-10-18 — `8a956ff3`: Recorded primary-source findings and research limitations in `research/RESEARCH.md`. Checked current eCFR income/activity provisions, DHCS September outreach and August renewal guidance, IRS income guidance, and final 2027 California subsidy design. Identified wording/timing conflicts and contract-specific unknowns for publication on Flagged for Review. One obsolete Covered California link returned a soft-404 and was excluded. No other session claim found in this checkout.

## Cross-session requests

- 2026-10-18 — Collision discovered: four other branches made overlapping intake claims. Earliest claim is `b97f1459` at 19:12:33 UTC; root index/assets/data also claimed by `63a8fb6e` at 19:12:43. This session's claim was 19:12:47, before other claims were visible in its initial remote listing. No shared site files had been edited here. Request earliest integrator to coordinate publication or explicitly transfer ownership. This session proceeds only in `research/**` plus coordination metadata; details and priority findings in `research/COORDINATION-HANDOFF.md`. No merge conflict has occurred and no other session's work has been discarded.

## Publication record

- Pull request: pending.
- Merge result: pending.
- Pages deployment: pending.
