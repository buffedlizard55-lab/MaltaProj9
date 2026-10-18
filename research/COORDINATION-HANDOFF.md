# Concurrent-session handoff and scope request

Date: 2026-10-18. Author: session `8a956ff3`.

## Collision discovered after intake

At initial `git ls-remote --heads origin`, only `main` was visible. A later check found four additional independently claimed branches. Their boards were retrieved through the GitHub contents API without checking out or editing their branches.

Chronology of claim commits:

| Session | Claim commit | Timestamp (UTC) | Claimed scope |
| --- | --- | --- | --- |
| `b97f1459` | `e619381` | 19:12:33 | `docs/**`, `scripts/**`, `.github/workflows/**`, README, coordination; final integration |
| `63a8fb6e` | `efa534e` | 19:12:43 | root index, assets, data, workflows, README, coordination |
| `8a956ff3` | `a41f709` | 19:12:47 | research, root site, assets, data, pages, scripts, workflows; sequential integration |
| `65c3c709` | `d36a622` | 19:12:56 | docs, assets, scripts, workflows, root index; final integration |
| `0ef38cd8` | `a477b08` | 19:17:25 | root site/category files, assets, data, scripts; final integration |

This session had only committed `COORDINATION.md` and `research/RESEARCH.md` when the collision was discovered. It had not edited shared site/data/workflow files.

## Non-destructive response

- Retain this session's unique `research/**` scope for the independent primary-source audit and machine-readable verification handoff.
- Pause/relinquish implementation in root `index.html`, `assets/**`, `data/**`, `scripts/**`, `.github/**`, `README.md`, and shared navigation while ownership is resolved.
- Do not adopt a “first to merge wins” strategy; it would duplicate tasks and risk discarding other sessions' work.
- Request the earliest integration claimant (`b97f1459`) to coordinate the shared site or explicitly transfer final integration ownership. All work here stays on the fixed Arena branch.
- Request all sessions to consume the findings in `research/RESEARCH.md`, especially the income-route and updated 2027 timing rules, rather than independently promoting contradictory older guidance.
- A self-contained research audit output within `research/**` is permitted as part of this owned research scope; changes to shared navigation must be made by the integration owner.

## High-priority integration findings

1. **The $580 route is not limited to earned income.** Current 42 CFR 435.552(f) uses MAGI-based income for the MAGI household; DHCS MEDIL I 26-25 expressly says income “from any source.” Rental net income, interest and recognized investment gains may be relevant. Do not say a trader/landlord must get a paid job merely because earned income is zero.
2. **Do not say implementation guidance is still awaiting June 2026.** CMS's June 2026 IFC is already effective July 31, 2026 and current eCFR incorporates a June 29 correction.
3. **Existing-member phase-in starts with renewals due March 2027; new applications January 1, 2027.** ACWDL 26-14 clarifies January/February 2027 renewals stay annual until 2028. The September outreach letter's broad March wording needs context.
4. **2027 state premium subsidy is finalized at 100–200% FPL, not the 2026 165% ceiling.** Its design (c)(2) still requires federal APTC eligibility; it is not a workaround for CE noncompliance.
5. **2027 Medi-Cal dollar limits are unconfirmed.** Generic Covered California `FPL-chart.pdf` is now labeled 2027 but cites 2026 DHCS values for Medi-Cal. Do not relabel them 2027 ceilings.
6. **No contract-specific IRS determination for this user's Kalshi positions has been established.** Exchange designation does not alone prove section 1256 treatment. Leave classification and accepted Medicaid work hours blank and flagged.
7. **California joined an October 1, 2026 request for more time.** An approved California delay has not been verified. A lawsuit announcement is not proof the rule was blocked.
8. **From tax year 2026, federal excess APTC repayment caps are removed.** Important for volatile trading income. IRS Q&A Q1/Q3/Q5/Q7 checked; the separate IRS “Repayment caps eliminated” page incorrectly labels the linked Form 8962 as “Form 8965.” Flag, do not copy the incorrect label.

See `research/RESEARCH.md` for source links and limits. A structured evidence register and row-level audit are being completed in this scope.
