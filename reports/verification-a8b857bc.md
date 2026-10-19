# V6 Independent Verification Report — session `arena/a8b857bc`

Date: **2026-10-19 (UTC)** · Branch: `arena/a8b857bc-maltaproj9` · Base at intake: `main` = `bd3e87e`
(PR #22). While this audit was in progress, session `arena/cb0807c0` merged **PR #23** (V5/S2/I4);
this branch was rebased onto the new `main` (`8d06324`) and the full audit re-run against the
combined tree. All conflicts were confined to `COORDINATION.md` and were resolved additively —
nothing from either session was discarded.

## 0. Scope and non-overlap claim

Two other sessions held active V5 claims at intake (`arena/565d5e24`, `arena/cb0807c0`) with broad
scopes over `data/*.csv`, `data/*.json`, templates, and built HTML. Per the board rule "never
start a task another session has claimed", V6 was claimed as a strictly non-overlapping audit:
outputs are **this new report** and an **append-only `COORDINATION.md` log**. No data row,
template, or built page was edited by this session. Confirmed issues are logged as cross-session
requests instead. Standard applied: every factual table row must link an official source;
unconfirmable values stay blank and are flagged; no personal eligibility is inferred;
contradictions are published, never silently reconciled.

## 1. Repository and build state (checked locally after rebase onto `8d06324`)

| Check | Command / source | Result |
|---|---|---|
| Dashboard data validation (9 CSV tables, 209 rows; 32 non-verified rows all on the Flagged page) | `python3 scripts/validate.py` | **PASS** |
| Root research brief (9 HTML pages; local links/fragments; official HTTPS source on every data row) | `python3 scripts/check_site.py` | **PASS** |
| `docs/` verification dashboard deterministic rebuild (7 pages; 73/73 sources) | `python3 build_site.py --check` | **OK — matches committed output** |
| Dashboard rebuild determinism | `python3 scripts/build.py` | byte-identical to committed `dashboard/**` |
| Rows missing a source URL | CSV scan | **0** (every row, including blanks and flags, carries an official `source_url`; FL-09 is the documented repository-audit self-reference) |
| GitHub Pages | Pages API (`main`/`/`, https enforced) | status **built**; live fetches of root, `/dashboard/`, `/docs/`, `/your-situation.html`, `/flagged.html` all return current content |
| CI on `main` after PR #23 | Actions history | `Validate`, `Build check`, and `pages-build-deployment` all **success** (runs at 02:28–02:29 UTC) |

Data composition re-counted independently: 9 tables / **209 rows** = 179 rule rows (**177
verified + 2 intentionally blank: IN-08, IN-13**) + **30-row flagged registry** (25 `flagged` +
5 `unverified` blank-value flags). The built dashboard reports "179 sourced rows across 66 cited
sources · 30 flagged items", consistent with the CSVs.

## 2. Official sources re-fetched live on 2026-10-19 and compared value-by-value

Full-page reads (not snippets) via the page-fetch tool. Every value checked matched the published
rows; where an official-source contradiction is itself the finding, the flag is still live.

| # | Official document (live URL) | Rows covered | Result |
|---|---|---|---|
| 1 | eCFR, **42 CFR §435.552** (current through 10/15/2026; source 91 FR 33469) — all 3 content chunks | WR-03/04/05/06/07/18, IN-11/12 | **Match.** (a)(1)–(7) conditions; (b) work/community-service/work-program/education definitions (stand-alone job search excluded from work programs); (c)–(d) enrollment and credit-hour math (×3×4.33); (e)(2) income→hours option; **(f)(2) monthly income = MAGI-based income for the MAGI household per §435.603**; (g) seasonal-worker 6-month average per IRC 45R(d)(5)(B). |
| 2 | CMS fact sheet, **CMS-2454-IFC** (Jun 1 2026) | WR-02/03/04/05/08/10/12, EX-01..10 | **Match.** 80 hrs/month; implement no later than Jan 1 2027 (earlier at state option); non-pregnant adults 19–64 not on Medicare; 43 states + DC; $580 = 80 × $7.25 (2026); 30-calendar-day cure; reapply any time; hardship list. **FL-04 still live:** prose says "children under 14" while the same page's chart says "dependent child 13 years of age and under". |
| 3 | Federal Register, **CMS-2454-IFC**, 2026-11094, 91 FR 33348 (eff. Jul 31 2026) | WR-09 | **Match.** Rule document, 135 pages, docket CMS-2026-2047. |
| 4 | Federal Register **correction C1-2026-11094**, 91 FR 39028 (Jun 29 2026) | FL-18 | **Match.** 4-page correction replacing §435.557 and §435.558 (verification processes, reliable-information data sources, documentation rules from Jan 1 2028). |
| 5 | Federal Register **2026 HHS poverty guidelines**, 2026-00755, 91 FR 1797 (eff. Jan 13 2026) + ASPE poverty page | MC-04, OP-02, CC-07 arithmetic | **Match.** $15,960 (1p), $21,640, $27,320, $33,000 (4p), +$5,680. Cross-checks: ×1.38 = $22,024.80 → DHCS chart $22,025; ×4 = $63,840 (OP-02 400% cliff); 200% × $15,960 = $31,920 (CC-07). |
| 6 | DHCS **Medi-Cal Changes** consumer page | CA-01/03/05/07/08/24/25, FL-05/07 | **Match.** Work rules Jan 1 2027; six-month checks Mar 1 2027; copays Oct 1 2028 above **$15,560/yr** with 5% household cap; asset limits $130k→$21k (Jul 1 2027); premiums Jul 1 2027; "work at a job and earn $580" simplified wording still present (FL-05). **FL-07 still live:** $15,560 matches neither the 2025 ($15,650) nor 2026 ($15,960) 100% FPL. |
| 7 | DHCS **138% FPL eligibility chart** | MC-02/03 | **Match.** $22,025 / $29,863 / $37,702 / $45,540; +$7,839. |
| 8 | DHCS **ACWDL 25-30** (Dec 30 2025, expressly preliminary) | CA-02/14, WR-20..24/34..38, IN-19/20, EX-22 | **Match.** MAGI New Adult Group = aid code M1; person-by-person assessment; 30-day notice; 90-day cure; caregiver child "age 13 years of age and under"; lesser-of-8%-or-1.5× unemployment hardship; "total gross income" $580 framing (preliminary; superseded in hierarchy by the MAGI regulation — FL-05/06). |
| 9 | DHCS **ACWDL 25-31** (Dec 30 2025, preliminary) | WR-13, CA-29/30 | **Match.** §71107 six-month renewals from Jan 1 2027 for M1; exemptions (other coverage groups, AI/AN, pregnant/postpartum, under-19); renewal six months from first eligibility month; 90-day cure; 30-day response. |
| 10 | DHCS **MEDIL I26-25** (Sep 11 2026) incl. the Aug 31 2026 member letter | CA-04/11, WR-13/14/17, EX-11..15, FL-03 | **Match.** Two-modality outreach; mailing began late Aug 2026; member letter says rules "will not go into effect until **March 2027**" while the same letter's background says Jan 1 2027 (**FL-03 still live**); "$580 (before taxes) from any source" member wording; **verbatim**: losing Medi-Cal for noncompliance means no Covered California financial help — full-cost plans only (WR-17/CC-13); reapply any time; BenefitsCal + helpline 541-5555. |
| 11 | DHCS **Tracking Federal Impact** page | CA-12, FL-15 | **Match.** Dec 2025 CMS guidance; Jun 2026 IFR; work rules Jan 1 2027; six-month checks Mar 1 2027; retroactive coverage 1/2 months from Jan 1 2027; 5% cost-sharing cap Oct 1 2028. |
| 12 | DHCS **Immigration Status and Medi-Cal Eligibility** table | MC-19 | **Match.** U.S. citizens keep full Medi-Cal + dental, no premium; LPRs inside the five-year wait move to FFS Jan 2027 with a later Jul 2027 premium step (ages 21–59, not pregnant). |
| 13 | CA Legislative Information, **AB 2161** (Ch. 209, approved/filed Sep 14 2026) | CA-06/13..23, WR-11/27..32 | **Match.** Amends WIC §14005.69; legislative digest confirms 19–64 / ≤138% FPL population, 80-hour and half-time mechanisms, 30-calendar-day continued coverage, conflicting-data confirmation duty. |
| 14 | LAO **H.R. 1 impacts handout** (Feb 11 2026, Senate Budget committee) | CA-10, cost-sharing context | **Match.** "Medi-Cal currently does not require beneficiaries to work"; 80 hrs/month from Jan 2027; ~3.5M subject; 1–2M disenrollment estimate; cost sharing up to $35/service above 100% FPL. |
| 15 | DHCS **Jan 2026 H.R. 1 impact update** (Assembly Health committee PDF) | CA-09, **FL-30** | **Match.** 233K losses by Jun 2027 / 1M by Jan 2028 / 1.4M by Jun 2028; the deck itself names preliminary "**ACWDL 26-30**" as the successor letter — FL-30 is accurate. |
| 16 | IRS **Topic 429 — Traders in securities** | IN-16 | **Match.** "Gains and losses from selling securities from being a trader aren't subject to self-employment tax"; investor income likewise not SE; "it doesn't matter whether you call yourself a trader"; mark-to-market §475(f) mechanics. |
| 17 | IRS **Topic 414 — Rental income and expenses** | IN-04/17 | **Match.** Real-estate rentals generally Schedule E; substantial services for tenant convenience → Schedule C (the earned-income caveat behind IN-04). |
| 18 | IRS **Form 6781 (2025)** | IN-07 | **Match.** Part I Section 1256 mark-to-market; line 8 = 40% short-term, line 9 = 60% long-term. No IRS document classifies Kalshi event contracts as §1256 — supports keeping IN-08 blank. |
| 19 | IRS — **repayment caps eliminated for excess APTC** | CC-09/18 | **Match.** From tax year 2026 the full excess APTC must be repaid; caps no longer apply (WFTC Act). |
| 20 | HealthCare.gov — **MAGI glossary** and **premium tax credit glossary** | MC-05, IN-14, CC-03/04 | **Match.** MAGI = AGI + untaxed foreign income + non-taxable SS + tax-exempt interest; PTC for household income 100–400% FPL; no work requirement attached to the credit. |
| 21 | Covered California — **Open Enrollment** page | CC-01 | **Match.** "It lasts from Nov. 1 to Jan. 31"; shared Medi-Cal application. |
| 22 | Covered California — **press release 2026-07-21** (deep URL) and newsroom index | CC-07/11/12/21 | **Match, and V4 link issue resolved (see §3.2).** 9.9% preliminary weighted average; $300M HCARF (up from $190M); 200% FPL = $31,920 individual / $66,000 family of four; >500,000 projected subsidy recipients (~30%). |
| 23 | HBEX **Federal Changes for Enrollers Quick Guide** | CC-02/16 | **Match.** City of Columbus ruling vacated the shortened 2027 OE window; California OE reverts to Nov 1 2026 – Jan 31 2027. |
| 24 | CMS **City of Columbus statement** (Jul 31 2026) | CC-16 | **Match.** FFE open enrollment Nov 1 2026 – Jan 15 2027; stayed/vacated 2027 NBPP provisions listed. |
| 25 | Medicaid.gov **CMCS CIB Dec 8 2025** (cib12082025) | WR-16/25/26 | **Match.** §71119 adds SSA §1902(xx); begins Jan 1 2027 unless state sooner; cannot be waived under §1115; good-faith state exemptions expire no later than Dec 31 2028; PTC consequence at (xx)(7)(B). |
| 26 | Medicaid.gov **CMCS CIB Nov 18 2025** (cib11182025) | CA-26/27, WR-25/26 | **Match.** §71120 / new SSA §1916(k): cost sharing from Oct 1 2028, "cannot exceed $35 for any care, item, or service", aggregate 5% of family income, no premiums on this population. |
| 27 | Congress.gov — **H.R. 1 → Public Law 119-21** | WR-01 | **Match.** Became P.L. 119-21 on Jul 4 2025 (House 215–214; Senate 51–50). |
| 28 | Congress.gov — **H.R. 1834** + Sen. Cantwell release + Senate roll-call page | CC-06/14/15, FL-23 | **Match.** Passed House 230–196 (Roll no. 11) Jan 8 2026; received in Senate, placed on Legislative Calendar No. 319 on Feb 10 2026; not law. Enhanced credits expired Dec 31 2025. |
| 29 | California **FTB health-care mandate** page (updated Sep 15 2026) | CC-10/19/20, FL-24 | **Match.** $950/adult, $475/child, or 2.5% of gross income over the filing threshold; page labels the sample amounts as **2025** figures — FL-24's caveat is accurate. |
| 30 | Kalshi Help Center — **tax documentation** and **regulation** articles | IN-06/23, FL-01 | **Match.** 1099-INT/MISC/B (crypto transfers)/DA (ZeroHash), FIFO, monthly P&L, "not tax advice"; CFTC-regulated Designated Contract Market. Nothing classifies event contracts under IRC §1256 — IN-08 correctly stays blank. |
| 31 | DOL **COBRA**; CDI **SB 910 STLDI prohibition notice**; Medicare.gov **get started**; CMS **EMTALA** | OT-01/03/05/06 | **Match.** COBRA up to 102% of premium; STLDI cannot be issued/sold/renewed in CA from Jan 1 2019 (Ins. Code §10123.61); Medicare at 65 or earlier on disability/ESRD/ALS; EMTALA screening/stabilization regardless of ability to pay. |
| 32 | **BenefitsCal**, **CalJOBS/EDD WIOA** | OT-12/13, work-program route | **Match.** Official benefits portal live; America's Job Center of California network at no cost (the WIOA work-program pathway). |

### Hosts not independently re-fetched this session (and why this does not weaken the audit)

`govinfo.gov` URLs are the official GPO PDFs of the same Federal Register documents verified at
federalregister.gov (#3–5). `chhs.ca.gov` webinar PDFs, `sandiegocounty.gov`, and
`apply.coveredca.com` appear only as narrative/portal links, never as the `source_url` of a data
row (verified by CSV scan). `edd.ca.gov` content was verified via the EDD WIOA page and CalJOBS
(#32). All data-row source hosts (dhcs, ecfr, leginfo, irs, cms, medicaid, coveredca/hbex,
healthcare.gov, congress, senate, federalregister, ftb, dol, insurance.ca.gov, medicare,
benefitscal, caljobs/edd, aspe, sbud/ahea, kalshi help) were probed live and returned the
expected official document.

## 3. Findings

### 3.1 No factual errors found in any verified row

Across the 32 source checks above, every load-bearing value in the 179 rule/data rows was
re-confirmed against the live official document. The two intentionally blank values (IN-08 Kalshi
§1256 character; IN-13 trading hours as work) remain unconfirmable from any official source —
Kalshi's own documentation (#30) and IRS Topic 429 (#16) reinforce rather than resolve the blank.
No value was inferred or filled. The previously published contradictions FL-03 (Jan vs March
2027 wording), FL-04 (CMS self-contradiction on caregiver age), FL-05 ($580 wording hierarchy),
FL-07 ($15,560 vs FPL) were all observed still present on the live official pages and remain
correctly flagged. FL-18 (the 06/29/2026 correction) and FL-30 (ACWDL 26-30 successor letter)
were verified against the underlying documents and are accurate.

### 3.2 Resolved observation — V4's Covered California deep-link issue

V4 (session `arena/c79aa57d`) logged that the July 21 2026 press-release deep URL returned a
404 page to non-browser fetchers, while the newsroom index listed it. On 2026-10-19 the deep URL
(`/press-releases/2026/07/21/covered-california-rates-and-plans-for-2027-...`) returned the full
canonical release (HTTP 200, complete text). The citation is valid; no edit required. The
newsroom index independently lists the same release.

### 3.3 New irregularity (documentation-only) — README counts stale after PR #23

`README.md` still describes the dashboard as "**207 rows** … 179 rule/data rows, 177 verified and
2 blank-unverified, plus a **28-item** flagged registry … **65** distinct cited sources". After
PR #23 the built and validated state is **209 rows** (179 rule rows: 177 verified + 2 blank) +
**30-item** flagged registry + **66** cited sources. The dashboard itself, `validate.py`, and the
Flagged page all show the correct numbers; only README prose is stale. This is outside V6's
claimed file scope, so it is logged as a cross-session request rather than edited here.

### 3.4 Coordination observation — stale parallel branch

`arena/565d5e24-maltaproj9` (claim at 02:23 UTC) is based on the pre-#23 commit `bd3e87e` and, as
of this report, contains only COORDINATION claim commits (no data or site changes of its own).
Compared with current `main` its diff appears to delete PR #23's report, FL-29/FL-30 and the
rebuilt dashboard — an artifact of staleness, not intent. If that session opens a PR it must
`git pull --rebase origin main` first; merging it unrebased would regress `main`. Logged in
COORDINATION.md cross-session requests.

### 3.5 Completeness against the user's brief

The three publications collectively answer every question in the brief, each with sourced rows:
executive summary (root `index.html`, `dashboard/executive-summary.html`, `docs/index.html`);
the exact new-law mechanics and provisions (WR/EX/CA rows + `docs/federal.html` with verbatim
CFR text); how to satisfy the rule with $0 earned income (`your-situation.html` routes A–F,
OP-07/08, and the §435.552(f)(2) MAGI income route verified here); what California does for
people with no wages (`california-help.html`, AB 2161/WIC §14005.69 protections, BenefitsCal/
county help); income-by-type treatment of Kalshi gains, rent, and interest (IN rows, with the
genuinely open tax-character question kept blank and flagged); and a single labeled Flagged for
Review page in each publication. No personal eligibility outcome, dollar threshold for the user's
household, or tax characterization is asserted anywhere.

## 4. Verification statement

I independently re-fetched the official sources listed above on 2026-10-19 and compared the
published values line by line. Where a value could not be confirmed from an official source, the
published cell is blank and the item appears on a Flagged for Review page; I found no row that
violates this standard. The three validators pass on the combined post-#23 tree, CI is green, and
all three GitHub Pages publications serve the verified content. This report is informational,
not a personal eligibility determination or legal/tax advice.
