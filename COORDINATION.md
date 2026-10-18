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
| I1 — Final integration: sourced tables and accessible static dashboard | in progress (reserved; implementation after R1) | `8a956ff3` | `index.html`, `404.html`, `pages/**`, `assets/**`, `data/**`, `.nojekyll`, `README.md` | Only final integration edits shared data and navigation; no other claimed sessions at intake. |
| Q1 — Build, claim/source coverage, navigation and accessibility checks | in progress (reserved) | `8a956ff3` | `scripts/**`, `tests/**`, `package.json`, `package-lock.json`, `.gitignore`, `.github/**` | Add reproducible checks. Report external-source access limitations, not invented verification. |
| P1 — PR, merge, Pages deployment and final audit | in progress (reserved) | `8a956ff3` | `COORDINATION.md`; GitHub PR / Pages configuration | Pull with rebase before every push; explicitly merge the numbered PR; record deployment evidence. |

## Verification standard

1. Official federal or California sources only for legal/eligibility/tax assertions. Each published table row must link an official source.
2. Distinguish enacted statutory text, agency implementation guidance, IRS tax rules, and analysis/recommendations.
3. A source confirming a general rule does not determine this user's eligibility or classify a particular Kalshi contract. Unknown personal facts and unconfirmed implementation details remain blank and are flagged.
4. Research snapshot date: **2026-10-18**. An older source's date and any future effective date must remain distinguishable.
5. Source access, row-by-row verification and unresolved inconsistencies will be documented in `research/` and on the site.

## Activity log

- 2026-10-18 — `8a956ff3`: Read the initial repository and remote branch list. Only `main` existed remotely; working branch is clean. Existing Pages configuration serves `main` from `/` at <https://buffedlizard55-lab.github.io/MaltaProj9/>. Claimed the above scopes before starting substantive work. No concurrent claim or merge conflict found.

## Publication record

- Pull request: pending.
- Merge result: pending.
- Pages deployment: pending.
