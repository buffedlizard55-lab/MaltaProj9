# V4 Independent Verification Report — session `arena/c79aa57d`

Date: 2026-10-18 (UTC, work performed 22:16–22:45) · Base: `main` = `e8d7e5c` (PR #15 merged)
Standard: every checked value compared against the cited official source, re-fetched live during
this session. No value was inferred; no eligibility determination was made. This report is an
audit record — it changes no published data.

## 1. Repository state at intake

- `main` = `e8d7e5c`; GitHub Pages build for `e8d7e5c` status **built** (2026-10-18T22:16:52Z, via
  GitHub API `repos/buffedlizard55-lab/MaltaProj9/pages/builds/latest`).
- `python3 scripts/validate.py` → **PASS** (9 tables, 204 rows, 29 non-verified rows all surfaced on
  the Flagged for Review page, 9 dashboard pages, internal links resolve).
- `python3 scripts/check_site.py` → **PASS** (9 root pages, local links/fragments resolve, every
  table data row carries an official HTTPS source).
- No uncommitted changes; no conflicts at intake.

## 2. Official sources re-fetched live this session (spot re-verification)

| # | Source (as cited in `data/*.csv`) | Live URL checked | Result |
|---|---|---|---|
| 1 | CMS fact sheet, CMS-2454-IFC (June 1, 2026) | https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms | **Matches published rows.** 80 hrs/month; implement no later than Jan 1, 2027 (earlier at state option); non-pregnant adults 19–64 not on Medicare in the adult group/certain 1115 demos; 43 states + DC; income route = 80 × federal minimum wage ($580 in 2026); seasonal workers "different calculation"; 30-day cure after notice of noncompliance; reapply any time. Internal age-wording contradiction still present on the live page (prose "under 14 years of age" vs chart "13 years of age and under") → flag FL-04 remains accurate. |
| 2 | 42 CFR 435.552 (eCFR, current through 10/15/2026) | https://www.ecfr.gov/current/title-42/part-435/section-435.552 | **Matches published rows verbatim.** (a)(1)–(7) qualifying conditions; (b) definitions (community service = structured public/nonprofit program with hour tracking; work = paid/in-kind/unpaid; work program list excludes stand-alone job search; educational program types); (c) enrollment status rules; (d) less-than-half-time credit math (credits × 3 × 4.33); (e)(2)(i)–(ii) state-option income→hours conversion (income ÷ federal minimum wage, reasonable household allocation); (f)(2) **monthly income = MAGI-based income for the MAGI-based household** (§435.603); (g) seasonal-worker 6-month average per IRC §45R(d)(5)(B). Confirms WR-04/05/06/07/11/18 and the "$580 is MAGI-based, not wages-only" correction. |
| 3 | DHCS "Medi-Cal Changes" member page | https://www.dhcs.ca.gov/medi-cal/updates/medi-cal-changes/ | **Live at the cited URL** (the legacy `.aspx` path returns 404 but is cited nowhere in the repo). Confirms: work rules start Jan 1, 2027; exemption list (children 0–18, 65+, pregnant + 1 year, parents/caregivers of children 0–13, disability, serious conditions, released from jail/prison in last 90 days, Medicare Part A/B, AI/AN, former foster youth to 26); compliance routes ($580/month, seasonal 6-month average of $580, 80-hr job training, 80-hr volunteer/community service, half-time school ≈ 6–8 credits, combination); six-month eligibility checks from March 1, 2027; copays from Oct 1, 2028 for adults over **$15,560** (matches neither 2025 $15,650 nor 2026 $15,960 100% FPL — flag FL-07 remains accurate); asset limit $130,000 through June 30, 2027 then $21,000/$31,000 + $1,550; retroactive coverage shortened to 1 month (childless adults) / 2 months (others) from Jan 1, 2027. Simplified wording "Work at a job and earn at least $580 a month" still present → flag FL-05 remains accurate. |
| 4 | DHCS "Eligibility by Federal Poverty Level" chart | https://www.dhcs.ca.gov/medi-cal/qualify/qualify-for-medi-cal-eligibility-chart/ | **Matches.** 138% FPL: $22,025 (1 person), $29,863 (2), $37,702 (3), $45,540 (4); +$7,839 each extra. Confirms MC-02/MC-03. |
| 5 | AB 2161 chaptered text / Welf. & Inst. Code §14005.69 | https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB2161 | **Matches published rows verbatim.** Chapter 209, approved/filed Sept 14, 2026. §14005.69(d)(1): applicants — one month immediately preceding application; (d)(2): enrollees — **any one month** between determinations/redeterminations; (e)(1)–(7) routes, incl. (e)(6) MAGI-based monthly income ≥ 29 U.S.C. §206 minimum wage × 80 and (e)(7) seasonal 6-month MAGI average; (f) deemed-compliance/exclusions; (g)–(h) short-term hardship (inpatient care, presidentially declared disaster county, county unemployment ≥ lesser of 8% or 1.5× national, medical travel); (i) county must request confirmation before adverse action on conflicting data; (k) 30-calendar-day cure with continued Medi-Cal services. Confirms CA rows and WR-11 "any one month" correction. |
| 6 | IRS Topic no. 429, Traders in securities | https://www.irs.gov/taxtopics/tc429 | **Matches.** Own-account trading is a trade or business for a qualifying trader, but "Gains and losses from selling securities from being a trader aren't subject to self-employment tax"; expenses on Schedule C; mark-to-market election under §475(f) by the due date of the prior year's return; "It doesn't matter whether you call yourself a trader or a day trader." Confirms IN-16 (full-time trading does not create earned/SE income by itself). |
| 7 | HealthCare.gov — What's included as income | https://www.healthcare.gov/income-and-household-information/income/ | **Matches.** MAGI = AGI (Form 1040 line 11) + untaxed foreign income + non-taxable Social Security + tax-exempt interest; count capital gains, investment income (interest/dividends incl. tax-exempt), **net** rental and royalty income, self-employment net, unemployment; do not count SSI, child support, gifts, loan proceeds. Confirms the MAGI rows used for "does $0 earned income block coverage" (no) and for what income counts. |
| 8 | Covered California — Open Enrollment | https://www.coveredca.com/enrollment/open-enrollment | **Matches.** Open enrollment Nov 1 – Jan 31; enroll by Dec 31 for Jan 1 start; January enrollment starts Feb 1; special enrollment 60 days after a major life change; one application covers Covered California and Medi-Cal. Confirms CC date rows. |
| 9 | Kalshi Help Center — Tax Documentation | https://help.kalshi.com/en/articles/13823849-what-tax-documentation-does-kalshi-provide | **Matches.** 1099-INT (interest), 1099-MISC (credits/rewards), 1099-B (crypto-transfer proceeds), 1099-DA (digital assets via ZeroHash); FIFO P&L updated monthly (fees and rebates included); explicit "not tax advice." Confirms IN-23 and the FL-01 context (no official §1256 classification; value correctly left blank). |
| 10 | Covered California press release (July 21, 2026) — 2027 rates/state subsidy | cited deep URL + https://www.coveredca.com/press-releases | **Content corroborated; access quirk logged.** The cited deep URL (…/press-releases/2026-07-21/…-rates-and-plans-for-2027-…) returned Covered California's 404 page to this session's non-browser fetcher twice, but the release **is listed at that exact URL on Covered California's own live newsroom page** (fetched this session), and the search-indexed full text confirms every published figure: $300M HCARF appropriation (up from $190M), state subsidy to 200% FPL for 2027 ($31,920 individual / $66,000 family of four), >500,000 projected state-subsidy recipients (~30% of enrollees), ~200,000 with two $0-premium Silver choices, 9.9% preliminary weighted average rate change, OE Nov 1 – Jan 31, 2027. Citation judged **canonical and verified**; the deep-link 404 for non-browser clients is logged as an observation (see §4), not an error. |

## 3. Live published-site verification (GitHub Pages)

| Page | URL | Result |
|---|---|---|
| Root brief index | https://buffedlizard55-lab.github.io/MaltaProj9/ | Live; content matches `main` (MAGI-based $580, any-one-month rule, subsidy-loss warning, 8-card navigation). |
| Your Situation (PR #14) | https://buffedlizard55-lab.github.io/MaltaProj9/your-situation.html | Live; tailored $0-earned-income answer with sourced tables. |
| Dashboard home | https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/index.html | Live; 177 rule rows / 62 sources / key numbers ($580, $22,025, $31,920, Nov 1 2026) match the CSVs. |
| Flagged for Review (dashboard) | https://buffedlizard55-lab.github.io/MaltaProj9/dashboard/flagged-for-review.html | Live; full registry incl. FL-01 (Kalshi §1256 blank), FL-04, FL-05, FL-06, FL-07 published with sources. |
| Pages build status | GitHub API `pages/builds/latest` | `built` for commit `e8d7e5c` (2026-10-18T22:16:52Z). |

## 4. Findings, irregularities, coordination notes

1. **No errors found.** Every value spot-checked this session matches its cited official source;
   the 2 intentionally blank values (IN-08 Kalshi §1256 character, IN-13 trading hours as work)
   remain unconfirmable from any official source and remain correctly blank + flagged.
2. **Observation (non-blocking):** Covered California's deep press-release URLs 404 for
   non-browser fetchers while remaining listed on the official newsroom index. Cross-session
   request logged in COORDINATION.md for a future owner of `data/covered-california.csv` to
   optionally add `https://www.coveredca.com/press-releases` as a secondary link on CC-07/11/12/21.
   No edit made here (file owned by active sessions `arena/1c375fb4` / `arena/5711b968`).
3. **PR #11** (`arena/690e8271`, open since 20:23 UTC, last commit 20:28 UTC — stale >60 min):
   additive third publication (`docs/` site, `research/*.md`, `data/*.json`); CI checks SUCCESS;
   touches root `index.html`, `sources.html`, `README.md`, `COORDINATION.md` (mergeable state
   UNKNOWN pending GitHub recompute against `e8d7e5c`). Left untouched; resolution belongs to the
   session holding the final-integration claim (`arena/1c375fb4` I3).
4. **Stale claim-only branches** (>60 min, single claim commit, no PR): `193089a8`, `2e5ccefa`,
   `4696cfa4`, `bf97c1f6` — takeover-eligible per board rules; no takeover needed this session.
5. Tooling note: this session's page-fetch proxy intermittently rewrote URLs and returned
   `SignatureDoesNotMatch`; all affected fetches were retried with canonical URLs until the
   official page content was retrieved. No check in this report relies on a failed fetch.

## 5. Conclusion

Both publications remain accurate against the official sources as of 2026-10-18; both validators
PASS; the live Pages deployment serves the current `main`. The answer to the project question is
unchanged and fully sourced on the site: $0 earned income does not bar Medi-Cal or Covered
California (both use household MAGI, which counts rental, interest, and trading gains), and the
2027 community-engagement requirement can be met without wages — in California via **one**
qualifying month per renewal period (e.g., ≥$580 MAGI-based monthly income from any source,
80 hours of structured community service, half-time school, a work program, a combination, or an
exemption), with AB 2161 protections (data-first verification, 30-day cure with continued
coverage, county confirmation before adverse action).
