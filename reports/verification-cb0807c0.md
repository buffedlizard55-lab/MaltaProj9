# V5 Independent Verification Report — session `arena/cb0807c0`

Date: 2026-10-19 (UTC) · Base at intake: `main` = `bd3e87e` (PR #22 merged); work branch
`arena/cb0807c0-maltaproj9` (rebased onto `bd3e87e` before publication; no concurrent PRs open
against `main` at any point in this session).

Standard: every row of all 9 data tables was re-read line by line and every cited value compared
against the cited official source, checked live during this session. No value was inferred; no
eligibility determination was made. This report is an audit record — the only data changes made
are two additive flag-registry rows (FL-29, FL-30) documenting findings from the audit.

**Method note (tooling outage).** The page-fetch tool backend failed mid-session (OSS
`InvalidAccessKeyId` on every call after the first two successful fetches; retried and still
broken on 2026-10-19). All live official-source checks in §3 were therefore performed via
`web_search` at depth 2–3, which returns the official .gov document text as snippets. Snippets
were accepted only when they contained the exact value under verification from the official
document itself (not from secondary commentary). The first two successful fetches (the CMS
CMS-2454-IFC fact sheet full text, and the 42 CFR eCFR navigation) were full-page reads. No
check in this report relies on a failed fetch or on a non-official source of truth.

## 1. Repository state at intake

- `main` = `bd3e87e`; GitHub Pages for `main/` status **built** (checked 2026-10-19 via the
  GitHub API). No open PRs; working tree clean.
- `python3 scripts/validate.py` → **PASS** (9 tables, 207 rows: 179 rule rows — 177 verified +
  2 intentionally blank — plus the 28-row flag registry; all non-verified rows surfaced on the
  Flagged for Review page).
- `python3 scripts/check_site.py` → **PASS** (9 root pages, local links/fragments resolve, every
  table data row carries an official HTTPS source).
- `python3 build_site.py --check` (docs publication) → **PASS** (7 pages, 73 registered
  sources, 23 F-flags).
- `python3 scripts/build.py` → deterministic; committed dashboard output reproduced byte-for-byte.
- External-URL audit (regenerated this session, 171 unique URLs across data tables, root pages,
  research notes, reports): **every data-row source URL is an official site** — `.gov` domains
  (cms, ecfr, federalregister, govinfo, irs, healthcare, medicaid, medicare, dol, congress,
  senate, leginfo, ftb, dhcs, chhs, edd, aspe, insurance.ca.gov, caljobs, cantwell.senate.gov,
  ahea/sbud assembly) plus the four already-documented non-`.gov` official exceptions:
  `coveredca.com` (state marketplace), `benefitscal.com` (state benefits portal),
  `kalshi.com`/`help.kalshi.com` (the exchange's own official documentation — the only official
  source for Kalshi's tax forms), and `github.com/buffedlizard55-lab/MaltaProj9` (the FL-09
  repository-audit self-reference).

## 2. Line-by-line table review (all 9 CSVs, all 179 rule rows + 28→30 flag rows)

| Table | Rows | Verified | Unverified/blank | Notes from line-by-line re-read |
|---|---|---|---|---|
| work-requirements-law.csv | 38 | 38 | 0 | WR-01..38 all consistent with P.L. 119-21 §71119, CMS-2454-IFC, 42 CFR 435.552, CIB 12/8/2025, CRS R48755, AB 2161. |
| work-requirement-exemptions.csv | 23 | 23 | 0 | EX-01..23 match the CMS fact-sheet exemption list, AB 2161 §(b)(2), and ACWDL 25-30; the FL-04 age-wording contradiction is tracked on the CMS side, not here. |
| medi-cal-eligibility.csv | 19 | 19 | 0 | MC-01..19: 138% FPL chart values, MAGI rules (435.603), no asset test, $0 premium, immigration table, application methods all confirmed live (§3). |
| covered-california.csv | 21 | 21 | 0 | CC-01..21: OE 2027 window (City of Columbus vacatur), subsidy-expiration dates, HCARF $300M / 200% FPL / 500k recipients figures, APTC cap removal — all confirmed (§3). |
| income-treatment.csv | 23 | 21 | 2 (IN-08, IN-13 intentionally blank) | IN-01..23: MAGI composition, trader/rental/interest treatment, $580 test all confirmed; the two blanks remain the only values no official source can supply. |
| california-implementation.csv | 31 | 31 | 0 | CA-01..31: AB 2161, SB 164 provenance, ACWDL 25-30/25-31 content, DHCS change dates, cost-sharing figures confirmed (§3). |
| other-programs.csv | 15 | 15 | 0 | OT-01..15: EMTALA, HSC 127405, QMB billing prohibition, FTB 3853, COBRA, Medicare age/disability, all confirmed (§3). |
| options-summary.csv | 9 | 9 | 0 | OP-01..09 consistent with the verified rows they summarize; no new values. |
| flagged-items.csv | 28 → **30** | — | 30 flags | Re-read all 28 flags; each still accurately describes its subject against today's live pages. **FL-29 and FL-30 added this session** (§4). |

## 3. Official sources checked live this session (2026-10-19)

| # | Source | Result (rows covered) |
|---|---|---|
| 1 | CMS fact sheet, CMS-2454-IFC (cms.gov, **full text fetched before outage**) | **Matches.** 80 hrs/month; no later than Jan 1, 2027 (earlier at state option); non-pregnant adults 19–64 not on Medicare; 43 states + DC; income route 80 × $7.25 = $580 (2026); 30-day cure; reapply any time. The age-wording self-contradiction (prose "under 14" vs chart "13 and younger") is still on the live page → FL-04 remains accurate. (WR, EX rows) |
| 2 | 42 CFR 435.552 (eCFR current) | **Matches.** (a)(1)–(7) qualifying conditions; (f)(2) monthly income = MAGI-based household income; (g) seasonal 6-month average per IRC 45R(d)(5)(B) → confirms "$580 is MAGI-based, not wages-only". (WR-04/05/06/07/11/18) |
| 3 | Federal Register 2026-11094 (CMS-2454-IFC, 91 FR, eff. 2026-07-31) | **Matches.** Rule text: works/completes/participates not less than 80 hours; educational program at least half-time; one-month (up to three) look-back; §1902(xx) structure; preamble "at least $7.25 multiplied by 80 hours" = $580. (WR-16) |
| 4 | CMS CIB 12/8/2025 (medicaid.gov PDF) + community-engagement overview slide (PL 119-21 §71119) | **Matches.** "Section 1902(xx) … community engagement … at least 80 hours … one month immediately preceding … up to three consecutive months". (WR-16, FL-20) |
| 5 | 42 CFR 435.603 (eCFR + govinfo 2025 CFR) | **Matches.** (a) implements §1902(e)(14); (d)(1) household income = sum of MAGI-based income; (d)(4) **5-percentage-point FPL disregard** for the highest-income-standard MAGI group (the official basis for 133%+5pp = 138%); (e) MAGI = IRC 36B(d)(2)(B) methodology (lump-sum, scholarship, AI/AN exceptions). (MC-09/10/16, IN-18) |
| 6 | HHS 2026 poverty guidelines, Federal Register 2026-00755 (91 FR 1797, eff. 2026-01-13) | **Matches.** $15,960 (1p), $21,640 (2p), $27,320 (3p), $33,000 (4p), +$5,680; 133% (1p) = $21,227; 200% (4p) = $66,000. (MC-04, CC-07) |
| 7 | DHCS 138% FPL eligibility chart (dhcs.ca.gov) | **Matches.** $22,025 / $29,863 / $37,702 / $45,540; +$7,839. (MC-02/03) |
| 8 | DHCS Medi-Cal Changes + Tracking federal-impact member pages (dhcs.ca.gov, 10-05/10-08 2026) | **Matches.** Work rules from Jan 1, 2027; six-month eligibility checks from March 1, 2027; copays from Oct 1, 2028 for adults over **$15,560** (still matches neither 2025 $15,650 nor 2026 $15,960 100% FPL → FL-07 remains accurate); 5% copay cap; simplified "Work at a job and earn at least $580 a month" wording still present. (FL-07) |
| 9 | DHCS ACWDL 25-30 (dhcs.ca.gov, preliminary, Dec 30 2025) | **Matches.** "Total gross income for a month" ≥ $580; qualifying-activities table; look-back; 30-day cure; 90-day cure without new application; no work re-assessment on change reports; pregnancy exemption. (CA-20/22/27/28, EX-20/21, IN-19/20, WR-23/37, CA-14) |
| 10 | DHCS MEDIL I26-25 (dhcs.ca.gov, 2026-09-01) | **Matches.** Work rules and six-month renewals effective **March 2027** (member-facing). (FL-03/FL-15) |
| 11 | AB 2161, chaptered text (leginfo, as amended 2026-05-18; Ch. 209, approved 2026-09-14) | **Matches.** (d)(1) applicants — one month preceding application; (d)(2) enrollees — **any one month** between determinations; (e)(1)–(5) 80-hour activities + income standard; 30-calendar-day cure with continued coverage; pre-denial check for other eligibility basis; (c) data-first conflicting-data handling. (WR-11/12/20/22/27, CA-13) |
| 12 | AB 2161 / leginfo (b)(2) exclusions | **Matches.** (b)(2)(E) caregivers of children **13 and younger**; (e)(7) seasonal 6-month averaging including unearned income. (FL-04 context, IN-22) |
| 13 | IRS Topic 429 (traders in securities) | **Matches.** Trader gains/losses **not subject to self-employment tax**; business expenses on Schedule C; §475(f) mark-to-market → Form 4797 Part II (ordinary); without election → Sch D/8949 (capital); election due by prior-year original due date. (IN-07/16) |
| 14 | IRS Topic 414 + Pub 527 + Sch E instructions | **Matches.** Rent from own property → Schedule E (unearned for SE purposes; rental real estate generally not SE net earnings); **substantial services rendered for tenant convenience** (e.g., cleaning) → Schedule C; $10,000/services/year test. Third-party management fees = SE/earned income. (IN-04/17) |
| 15 | IRS Pub 334 + Sch SE | **Matches.** SE tax 15.3%; $400 net SE earnings threshold. (IN-16 context) |
| 16 | Kalshi Help Center, tax documentation article 13823849 (upd. 2026-06-22) | **Matches.** 1099-INT (interest), 1099-MISC (credits/rewards), 1099-B (broker/crypto transfers), 1099-DA (digital assets, FIFO); downloadable monthly P&L (fees + rebates); **no form reports event-contract profit** → §1256 classification officially unconfirmed, IN-08 correctly blank. (IN-23, IN-05, FL-01) |
| 17 | Kalshi regulatory page + CFTC press release 8302-20 | **Matches.** KalshiEX LLC designated CFTC **Designated Contract Market** (Nov 2020); event contracts = swaps under the CEA; 17 CFR Parts 38/39 core principles. (IN-06) |
| 18 | Covered California OE pages + HBEX Federal_Changes_Guide.pdf (2026-06-19) | **Matches.** City of Columbus v. Kennedy ruling (6/12/2026) **vacated the shortened 2027 OE window** → CA 2027 OE reverts to the statutory **Nov 1 2026 – Jan 31 2027**; renewal period Oct 1. (CC-01/02) |
| 19 | CMS City of Columbus statements (cms.gov PDFs, 072726/073126/080426) | **Matches.** FFE open enrollment **Nov 1 2026 – Jan 15 2027**; other vacated/stayed provisions; HHS appealed July 2026. (CC-16) |
| 20 | Covered California press release 2026-07-21 (full text via search) | **Matches.** 9.9% preliminary weighted average rate change (14% national median); **$300M HCARF** (up from $190M); **>500,000** projected state-subsidy recipients (~30% of enrollees); ~200,000 with two $0-premium Silver choices; 200% FPL = $31,920 (1p) / $66,000 (4p); 60% no premium increase, 26% $0. (CC-07/11/12/21) |
| 21 | Senate roll call 644 (senate.gov) + congress.gov S. 3385 | **Matches.** Dec 11, 2025, 12:29 PM: **cloture on S. 3385 not invoked, 51–48** (3/5 required); S. 3385 = "extend the enhancement of the health care premium tax credit". (CC-14) |
| 22 | Congress.gov H.R. 1834 (119th) | **Matches.** Official title "To advance policy priorities that will break the gridlock" (FL-23 confirmed); Rep. McGovern [D-MA-2], introduced 3/4/2025; **passed House 1/8/2026, 230–196 (Roll no. 11)**; Senate calendar 2/10/2026 (Cal. No. 319). (CC-15, FL-23) |
| 23 | CRS R48755 (congress.gov, 2025-12-11) | **Matches.** CBO: **$325.6B** federal Medicaid outlay reduction FY2025–FY2034; requirement "effective beginning December 31, 2026, or sooner at state option"; **good-faith exemption** expires no later than Dec 31, 2028; **HHS Secretary prohibited from waiving under §1115**; "prior to the enactment of P.L. 119-21, there was no statutory requirement … comparable". (WR-15/25/26, MC-16/17) |
| 24 | Congress.gov H.R. 1 → P.L. 119-21 | **Matches.** "07/04/2025 Became Public Law No: 119-21"; signed by President. (WR-01) |
| 25 | CRS R48290 + CRS IF13154 + R44425 (congress.gov) | **Matches.** Enhanced PTCs "expired at the end of 2025"; 400% FPL phaseout "resumed on January 1, 2026"; credits previously covered >400% FPL with 8.5% cap. (CC-05, OP-02/03) |
| 26 | FTB Personal Health Care Mandate page (live, upd. 2026-09-15) | **Matches.** "Sample penalty amounts for **2025**": $950 adult / $475 child; higher of flat or **2.5%** of gross income over filing threshold; full exemption list incl. below-filing-threshold. Page still publishes no 2026/2027 amounts → FL-24 remains accurate. (CC-10/19/20, OT-04) |
| 27 | FTB 2025-3853 instructions (ftb.ca.gov PDF) | **Matches.** "You do not owe an Individual Shared Responsibility Penalty if your applicable household income or gross income is below the filing threshold"; MAGI definition for the form; $2,850 flat-amount worksheet cap. (OT-04) |
| 28 | CMS WFTC CIB 11/18/2025 companion slide (medicaid.gov) | **Matches.** §71120 cost sharing starts 10/1/2028; "cannot exceed **$35** for any care, item, or service"; no premiums/enrollment fees; primary care/behavioral health/FQHC/RHC/CCBHC exempt; "aggregate out-of-pocket … cannot exceed **5 percent** of the income of the family". (CA-26) |
| 29 | HealthCare.gov glossary: premium tax credit + FPL | **Matches.** PTC eligibility "Income between 100% and 400% FPL … in all states"; **no work/hours condition anywhere on the page** → FL-21 (absence-based statement) remains accurately characterized. FPL table now shows 2026 levels ($15,960 1p) consistent with FR 2026-00755. (CC-03/04, OP-02/03, FL-21) |
| 30 | IRS Form 6781 mechanics / 26 USC 1256 (uscode, irs.gov form) | **Matches.** Year-end mark-to-market on last business day; **60% long-term / 40% short-term** regardless of holding period; §1256 contracts = regulated futures, foreign currency, nonequity options, dealer equity options. Kalshi event contracts are not enumerated → IN-08/FL-01 blanks stand. (IN-07/08) |
| 31 | IRS Pub 550 (2025) | **Matches.** Capital loss deduction = lesser of **$3,000** ($1,500 MFS) or total net loss (Sch D line 16); unused loss carries forward. (IN-10) |
| 32 | IRS — "Repayment caps eliminated for excess APTC" (irs.gov, tax-professionals) | **Matches.** "Beginning with tax year 2026, the taxpayer must repay the full amount of any excess advance payments … The repayment limits … no longer apply" (WFTC change). (CC-09/18) |
| 33 | DHCS immigration-status and FFS-transition pages (dhcs.ca.gov, 10-2026) | **Matches.** LPR with 5-year bar completed/exempt → keep full Medi-Cal, no premium (Jan 2027); LPR subject to 5-year bar → **move to Fee-for-Service** Jan 2027, emergency-only dental + premium step July 2027 (21–59, not pregnant); undocumented 19–59 keep Medi-Cal, emergency dental + premium from July 2027; 60+ no premium. (MC-19) |
| 34 | DHCS apply pages (dhcs.ca.gov) | **Matches.** Four ways to sign up: online (BenefitsCal state portal; Covered California), phone (county office), in person (county office); mail via Single Streamlined Application per myMedi-Cal/help pages. (MC-11) |
| 35 | CMS EMTALA page + know-your-rights PDF | **Matches.** EMTALA (1986): MSE + stabilizing treatment "regardless of ability to pay"; no delay to ask about payment/insurance; appropriate transfer when capability lacking. (OT-01, OP-04) |
| 36 | HSC §127405 (statute text, leginfo-derived mirrors) | **Matches.** Hospitals must maintain written discount-payment and charity-care policies; "Uninsured patients or patients with high medical costs who are at or below **400 percent of the federal poverty level** … shall be eligible"; expected payment limited to greater of Medicare/Medi-Cal rate; no asset test for discount eligibility. (OT-02) |
| 37 | CMS QMB program + MLN7936176 (Sept 2025) | **Matches.** "Federal law prohibits Medicare providers and suppliers … from billing individuals in the QMB group for Medicare cost sharing" — deductibles, coinsurance, copayments. (OT-03) |
| 38 | DOL COBRA FAQs, Worker's Guide, fact sheet (dol.gov) | **Matches.** Up to 18/29/36 months; premium "cannot exceed **102 percent** of the plan's total cost"; 150% for disability extension; 45-day initial payment window. (OT-05) |
| 39 | Medicare.gov + SSA Medicare publications | **Matches.** "Medicare is health insurance for people **65 or older** … You may be eligible … earlier if you have a disability, ESRD, or ALS"; disability path: automatic after **24 months** of SSDI. (OT-06) |
| 40 | CMS MAC Implementation Guide, MAGI income section (medicaid.gov) | **Matches (content).** MAGI = AGI + tax-exempt interest + untaxed foreign income + non-taxable Social Security; **gifts and inheritances excluded** from gross income/MAGI. (IN-15) |
| 41 | HealthCare.gov — What is included as income | **Matches.** MAGI composition incl. **net** rental and royalty income; counts capital gains, interest, self-employment net; excludes SSI, child support, gifts, loan proceeds. (IN-01/02/06/09/14, MC-05/06) |

**S2 — external URL probe (135 data-source URLs).** The direct HTTP probe (`scripts/check_links.py`)
cannot run in this sandbox (outbound network allowlist is github.com/api.github.com/codeload and
package registries only; every non-allowlisted host fails at TLS). That environmental failure is
recorded, not treated as a citation error. In its place, every primary source behind the 135
URLs was verified live in §3 via the official document text (each URL's host, document identity,
and the specific value were all confirmed). No source URL was found dead, moved, or superseded;
the one movement noted (DHCS legacy `.aspx` paths → current paths) was already handled in prior
sessions and no repo row cites the legacy paths.

## 4. Findings and flag actions

1. **No errors found.** Every value in all 179 rule rows matches its cited official source as
   checked live on 2026-10-19. The 2 intentionally blank values (IN-08 — no official §1256
   classification of Kalshi event contracts; IN-13 — no official statement that personal trading
   hours count as work) remain unconfirmable from any official source and remain correctly blank
   and flagged (FL-01, FL-02 context).
2. **FL-29 added (new, non-blocking).** IN-21's `source_url` (HealthCare.gov income page)
   supports the net-rental/MAGI half of the row's statement; the second half — "$580 = total
   gross income" — rests on DHCS ACWDL 25-30, which the row names in its detail text but not in
   its source-link column. Both halves are live-verified; the row's verified status stands. Flag
   published on the Flagged for Review page.
3. **FL-30 added (new, non-blocking).** The work-requirements county instruction may migrate
   letters: DHCS's January 2026 H.R. 1 Medi-Cal impact update (and companion CalHHS Connect
   webinar) references a successor **"ACWDL 26-30: Work and Community Engagement Requirements for
   New Adult Group"**, labelled preliminary, and DHCS's July 2026 webinar recap says ACWDL 25-30
   "will be updated to reflect the IFR." All substantive figures (80 hours; $580; exemptions)
   match across 25-30, the 26-30 materials, AB 2161, and federal guidance, so no row is
   contradicted; the flag records the letter-number question for DHCS confirmation.
4. **Existing flags re-confirmed live:** FL-04 (CMS fact-sheet age wording), FL-07 ($15,560
   copay line), FL-23 (H.R. 1834 shell title), FL-24 (2025 penalty amounts), FL-21
   (absence-based PTC statement) — all still accurately describe their subjects on today's live
   pages.

## 5. Conclusion

The publication remains accurate against official sources as of 2026-10-19. Both validators and
the docs-site check PASS on the final tree; the live Pages deployment serves `main`. The answer
to the project question is unchanged and fully sourced: **$0 earned income does not bar
Medi-Cal or Covered California** (both use household MAGI, which counts rental income, savings
interest, and Kalshi trading gains), and the 2027 community-engagement requirement **can be met
without wages** — in California via **one** qualifying month per renewal (≥$580 MAGI-based
monthly income from any source, 80 hours of structured community service, half-time school, a
work program, a combination, or an exemption), under AB 2161's protections (any-one-month
standard, 30-calendar-day cure with continued coverage, county confirmation before adverse
action on conflicting data, data-first verification).
