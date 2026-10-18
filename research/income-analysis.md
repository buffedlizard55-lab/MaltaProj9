# Income-Source Analysis — Kalshi Event Contracts, Rental Income, Savings Interest

Task: T5 · Owner session: `690e8271` · Verification date: 2026-10-18 (UTC)

**Question being answered:** with **$0 earned income**, can this person satisfy the Medicaid/Medi-Cal
community-engagement ("work") requirement using income from Kalshi event-contract trading, rental
income, and savings-account interest?

**Short answer: YES — under both federal regulation and California statute, the income pathway is
measured by total MAGI-based household income, not by earned income.** Details and exact citations below.
Two separate questions must be kept apart, because the answers differ:

| Question | Answer |
|---|---|
| Does this income count as **"earned income"** for tax/benefit purposes? | **No.** Interest, rents, and capital gains are **unearned** income. |
| Does this income count toward the **$580/month community-engagement income test**? | **Yes** — the test is MAGI-based household income, which includes unearned income. |
| Can the hours spent trading or managing rentals count as **"work"** hours? | **Probably for property management (self-employment is expressly covered by CMS); unverified for trading** — no official CMS, DHCS or IRS guidance addresses prediction-market/event-contract trading. **Flagged.** |

---

## 1. "Earned income" vs "unearned income" — official IRS definitions

| Income type | IRS classification | Official source |
|---|---|---|
| Wages, salaries, tips, other **taxable employee pay** | **Earned income** | [IRS EITC Central — Earned income, self-employment income and business expenses](https://www.irs.gov/tax-professionals/eitc-central/earned-income-self-employment-income-and-business-expenses); [IRS Pub 596 (2025)](https://www.irs.gov/publications/p596) |
| **Net earnings from self-employment** | **Earned income** | Same |
| Union strike benefits; long-term disability benefits received prior to minimum retirement age; gross income received as a statutory employee | **Earned income** | Same |
| **Interest, dividends, capital gains, rents, royalties** | **Unearned income** — IRS states verbatim: "*Unearned income.* This is investment-type income and includes **interest, dividends and capital gains, rents, royalties**, etc." | [IRS Newsroom — Who needs to file a tax return](https://www.irs.gov/newsroom/who-needs-to-file-a-tax-return) |
| **Rental real estate income** | "generally **isn't included in net earnings from self-employment** subject to self-employment tax and is generally subject to the passive activity limits"; reported on **Schedule E (Form 1040)** | [IRS Pub 527, Residential Rental Property](https://www.irs.gov/publications/p527); [Instructions for Schedule E (Form 1040)](https://www.irs.gov/pub/irs-pdf/i1040se.pdf); [Instructions for Schedule C](https://www.irs.gov/instructions/i1040sc) ("Schedule E … to report rental real estate and royalty income or (loss) that is **not subject to self-employment tax**") |
| **Exception:** rental activity where you provide **substantial services** to tenants, or you are a **real estate dealer** | Reported on **Schedule C** as a business and subject to self-employment tax | [IRS Pub 527](https://www.irs.gov/publications/p527) |
| **Investment income** (investor) | "Investment income **isn't subject to self-employment tax**." | [IRS Topic No. 429 — Traders in securities](https://www.irs.gov/taxtopics/tc429) |
| **Trader in securities** — gains/losses | "Gains and losses from selling securities from being a trader **aren't subject to self-employment tax**." Business **expenses** are reported on Schedule C. | Same |

## 2. "Trader" vs "investor" under IRS rules (why full-time trading still isn't earned income)

IRS Topic No. 429 sets out the official test. To be a **trader in securities** (a trade or business) you must meet **all** of:
1. You seek to profit from **daily market movements** in prices, not from dividends, interest or capital appreciation;
2. Your activity must be **substantial**; and
3. You carry on the activity with **continuity and regularity**.

Facts and circumstances considered: typical holding periods; frequency and dollar amount of trades; the extent to which you pursue the activity **to produce income for a livelihood**; and the amount of time you devote to the activity.

Even when a taxpayer **does** qualify as a trader, "**Gains and losses from selling securities from being a trader aren't subject to self-employment tax.**" Traders report business **expenses** on Schedule C; without a §475(f) mark-to-market election, gains and losses stay on Schedule D / Form 8949 as capital gains and losses; with a valid election they are ordinary and go on Form 4797 Part II.

Source: [IRS Topic No. 429](https://www.irs.gov/taxtopics/tc429)

**Analysis (not a quote):** the "trader" label is a *tax* classification. It does **not** convert trading
gains into earned income or self-employment income. It is nevertheless evidence of a **trade or business**,
which is what the *Medicaid* rule cares about — see §4 below.

## 3. Kalshi's own official tax documentation

Verified directly from Kalshi's help centre article **"What Tax Documentation Does Kalshi Provide?"**:

| Document Kalshi issues | What Kalshi says it contains |
|---|---|
| **1099-INT** | "contains interest payments from Kalshi" |
| **1099-MISC** | "contains credit/rewards from Kalshi" |
| **1099-B** | "contains transaction proceeds from broker transactions (**crypto transfers**)" |
| **1099-DA** | "contains **digital asset transaction reporting from ZeroHash**" |
| **Profit and Loss (PnL) statement** | "summarizes your trading activity including profits, losses, and fees." Access: Kalshi → Account → **Tax Info** → select year → download. Updated on the first of each month; uses **FIFO** accounting. |

Kalshi also states verbatim: "This information and the information included in the Profit and Loss statement are **not tax advice**, and Kalshi cannot give members advice on their taxes… each member should consult with a tax professional for any questions and is responsible for ensuring the accuracy of all returns." And: "**If no 1099 forms appear in your account, it is likely because you did not meet the IRS thresholds required for issuance.**" Tax forms are delivered electronically by **Zenwork**.

Source: [Kalshi Help Center — What Tax Documentation Does Kalshi Provide?](https://help.kalshi.com/en/articles/13823849-what-tax-documentation-does-kalshi-provide) (retrieved 2026-10-18)

**Verified observations:**
- **Kalshi does not list any 1099 that reports event-contract trading gains and losses.** The four forms it lists cover interest, credits/rewards, crypto-transfer broker proceeds, and digital-asset transactions. The trading result is delivered as a **PnL statement**, which Kalshi itself says is not tax advice and is not an IRS information return.
- Therefore the trading profit is **self-reported** by the taxpayer. This is a compliance risk and a documentation point, not an exemption.
- **Terminology irregularity (flagged):** the user describes "**Kalshi futures** trading contracts." Kalshi is a CFTC-regulated **event-contract** exchange; its products are event contracts, not exchange-traded futures. Kalshi's own documentation does not describe them as futures. This matters because **§1256 "regulated futures contract" treatment (Form 6781, 60/40, mark-to-market) turns on the contract being one of the types listed in §1256(b)**. See `research/flagged-items.md` item F-04.
- **No official IRS guidance** (Revenue Ruling, Notice, or regulation) was located in this session that classifies Kalshi/CFTC event-contract gains. Third-party practitioner commentary proposes four competing characterisations (Section 1256; capital asset; ordinary income on Schedule 1 line 8z; gambling income). **All four are unofficial. Left blank / flagged as UNVERIFIED — do not rely on any single characterisation without a tax professional.**

## 4. The Medicaid/Medi-Cal income test — why $0 earned income still works

### Federal rule (verbatim)

**42 CFR § 435.552(a)(6):** "The individual has a monthly income that is not less than the applicable minimum wage requirement under section 6 of the Fair Labor Standards Act of 1938 (29 U.S.C. 206(a)(1)(C)), multiplied by 80 hours."

**42 CFR § 435.552(f)(2):** "The agency must determine the monthly income based on the individual's **MAGI-based income, for their MAGI-based household**, as defined at § 435.603…"

**42 CFR § 435.603(e):** "**MAGI-based income** means income calculated using the same financial methodologies used to determine **modified adjusted gross income as defined in section 36B(d)(2)(B) of the Code**…"

Sources: [42 CFR § 435.552 (eCFR)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) · [42 CFR § 435.603 (eCFR)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603)

### Federal rule — self-employment expressly counts as "work" (verbatim, IFC preamble)

> "At new § 435.552(b), we define work to mean: work in exchange for money, work in exchange for goods or services ('in-kind' work), and unpaid work other than community service… **Many individuals work for themselves by being self-employed** due to starting a business, owning a business, or as an independent contractor, and **these activities meet the definition of work at § 435.552(b)**. Under our definition of work at § 435.552(b), **the hours the individual spends performing these duties would count toward meeting the 80-hour requirement.**"

Source: [Federal Register, 91 FR 33348 (June 3, 2026), CMS-2454-IFC, section II.C.1 "Work"](https://www.federalregister.gov/documents/2026-06-03/2026-11094/medicaid-program-community-engagement-requirement-for-certain-individuals) · [official PDF on govinfo](https://www.govinfo.gov/content/pkg/FR-2026-06-03/pdf/2026-11094.pdf)

### California statute (verbatim)

**WIC § 14005.69(e)(6)** (as added by SB 164, Stats. 2026, Ch. 27):
> "The individual has a **total monthly income, including, but not limited to, earned income, unemployment benefits, state disability insurance, retirement income, or dividends**, that is no less than the applicable minimum wage requirement under Section 206 of Title 29 of the United States Code, multiplied by 80 hours."

**WIC § 14005.69(e)(6)** (as amended by **AB 2161**, Ch. 209, Stats. 2026):
> "The individual has a **total monthly income, using modified adjusted gross income (MAGI)-based financial methods, as specified in Section 1396a(e)(14) of Title 42 of the United States Code, for their individual MAGI-based household budget**, that is no less than the applicable minimum wage requirement under Section 206 of Title 29 of the United States Code, multiplied by 80 hours."

**WIC § 14005.69(e)(7)** (AB 2161 version) — seasonal/fluctuating income:
> "The individual had an **average monthly income over the preceding six months, based on the individual's MAGI-based household budget**, as described in paragraph (6), that is no less than the applicable minimum wage requirement … multiplied by 80 hours, and is a **seasonal worker**, as described in Section 45R(d)(5)(B) of the federal Internal Revenue Code of 1986."

Sources: [current code text (leginfo)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=14005.69) · [AB 2161 chaptered text (leginfo)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB2161)

### California's own member-facing explanation (verbatim, DHCS)

> "you can meet this rule by any one or a combination of the items below:
> ● **Have an income from any source of at least $580 (before taxes) in any month since your last renewal.**
>  ○ People whose hours change frequently or who have seasonal jobs can **average at least $580 per month from any source over 6 months**."

Source: [MEDIL I 26-25 member outreach letter (DHCS, Sept 11, 2026)](https://www.dhcs.ca.gov/wp-content/uploads/2026/09/MEDIL-I26-25.pdf)

> Criteria: "Income equivalent to at least 80 hours at federal minimum wage (currently $7.25 per hour x 80 hours). Currently, this amount is **$580 a month**."
> Definition: "An individual's **total gross income** for a month must meet or exceed this amount (**including earned income, unemployment benefits, State Disability Insurance, retirement income, dividends, etc.**)"
> Criteria: "At least 80 hours of work" — Definition: "Have a job (working at least 80 hours a month) **including self-employment**."

Source: [ACWDL 25-30 (DHCS, Dec 30, 2025)](https://www.dhcs.ca.gov/wp-content/uploads/2026-04-25-30.pdf)

## 5. Income-source mapping — does each source count?

| Income source | Counts in **AGI/MAGI**? | Counts toward the **$580/month** income pathway? | Counts as **"earned income"**? | Official source |
|---|---|---|---|---|
| Savings-account **interest** | Yes — taxable interest, Form 1040 line 2b; AGI line 11 | **Yes** (MAGI-based) | **No** — IRS lists interest as *unearned* | [IRS — MAGI](https://www.irs.gov/credits-deductions/modified-adjusted-gross-income); [IRS Newsroom — who needs to file](https://www.irs.gov/newsroom/who-needs-to-file-a-tax-return) |
| **Tax-exempt** (municipal bond) interest | Yes — added back to AGI to reach MAGI | **Yes** | No | [IRS — MAGI](https://www.irs.gov/credits-deductions/modified-adjusted-gross-income); [HealthCare.gov — MAGI glossary](https://www.healthcare.gov/glossary/modified-adjusted-gross-income-magi/) |
| **Rental income** (net, Schedule E) | Yes — Schedule E flows to Schedule 1 → Form 1040 line 8 → AGI line 11 | **Yes** (MAGI-based) | **No** — "Rental real estate income generally isn't included in net earnings from self-employment"; IRS lists rents as *unearned* | [IRS Pub 527](https://www.irs.gov/publications/p527); [IRS Newsroom](https://www.irs.gov/newsroom/who-needs-to-file-a-tax-return) |
| **Kalshi event-contract gains** (however characterised: Schedule D capital gain, Form 4797 ordinary, or Schedule 1 line 8z other income) | Yes — every one of those lines flows into AGI | **Yes** (MAGI-based) | **No** — IRS: investment income and trader gains "aren't subject to self-employment tax" | [IRS Topic No. 429](https://www.irs.gov/taxtopics/tc429); [IRS Pub 550](https://www.irs.gov/forms-pubs/about-publication-550) |
| **Kalshi 1099-INT** (interest on Kalshi cash balance) | Yes | **Yes** | No | [Kalshi tax documentation](https://help.kalshi.com/en/articles/13823849-what-tax-documentation-does-kalshi-provide) |
| **Kalshi 1099-MISC** (credits/rewards) | Yes — box 3 "other income" generally goes to Schedule 1 line 8; the IRS form instructions add "If it is trade or business income, report this amount on Schedule C or F" | **Yes** | **Only if** reported as trade-or-business income on Schedule C | [Form 1099-MISC box 3 instructions (IRS)](https://www.irs.gov/pub/irs-prior/f1099msc--2024.pdf); [Instructions for Forms 1099-MISC and 1099-NEC (Rev. Dec 2026)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) |
| **Property-management fees** paid by third-party owners (if the user is paid to manage other people's property) | Yes — Schedule C if a trade or business | **Yes**, and the **hours** also count as work | **Yes** — net earnings from self-employment | [IRS EITC Central](https://www.irs.gov/tax-professionals/eitc-central/earned-income-self-employment-income-and-business-expenses); [CMS IFC preamble, section II.C.1](https://www.federalregister.gov/documents/2026-06-03/2026-11094/medicaid-program-community-engagement-requirement-for-certain-individuals) |
| **W-2 wages** (if any) | Yes | **Yes** | **Yes** | [IRS Pub 596](https://www.irs.gov/publications/p596) |
| Unemployment benefits | Yes | **Yes** — expressly named in the pre-AB 2161 CA statute and ACWDL 25-30 | No (unearned) | [WIC §14005.69(e)(6)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=WIC&sectionNum=14005.69); [ACWDL 25-30](https://www.dhcs.ca.gov/wp-content/uploads/2026-04-25-30.pdf) |
| CA **State Disability Insurance** | Yes | **Yes** — expressly named | No | Same |
| Retirement income / dividends | Yes | **Yes** — expressly named | No | Same |
| **SSI** | **No** — "MAGI doesn't include Supplemental Security Income (SSI)" | No | No | [HealthCare.gov — MAGI glossary](https://www.healthcare.gov/glossary/modified-adjusted-gross-income-magi/); [IRS PTC Q&A](https://www.irs.gov/affordable-care-act/individuals-and-families/questions-and-answers-on-the-premium-tax-credit) |
| **Lump sum** | Counted as income **only in the month received** (Medicaid-specific modification) | Yes, in that month | — | [42 CFR § 435.603(e)(1) (eCFR)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603) |
| Scholarships/fellowships used for **education**, not living expenses | **Excluded** from Medicaid MAGI income | No | — | [42 CFR § 435.603(e)(2)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603) |

## 6. Whose income counts? Household, and how it is allocated

| Item | Verified rule | Source |
|---|---|---|
| Federal | The agency must determine monthly income based on the individual's MAGI-based income **for their MAGI-based household**, as defined at § 435.603. | [42 CFR § 435.552(f)(2)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) |
| California | AB 2161 changed the state text to "**for their individual MAGI-based household budget**". | [AB 2161 text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB2161) |
| MAGI household = | For a taxpayer who expects to file and not be claimed as a dependent: the taxpayer **plus everyone they expect to claim as a tax dependent**. Married couples living together are each included in the other's household regardless of filing status. | [42 CFR § 435.603(f)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603) |
| Budget period | **Applicants**: current **monthly** household income and family size. **Current beneficiaries**: state may elect current monthly **or** projected annual income for the rest of the calendar year. | [42 CFR § 435.603(h)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603) |
| ⚠ Conflict flagged | ACWDL 25-30 states compliance is assessed **individually**: "All individuals must independently meet the participation criteria; **one individual's compliance cannot be used to satisfy another's requirement**," with a worked example in which a partner's 100 work hours cannot satisfy the applicant's requirement. That example is about **hours**, and the same ACWDL defines the income criterion as the individual's "**total gross income for a month**." Yet both 42 CFR § 435.552(f)(2) and AB 2161 measure the income test on the **household** MAGI budget, and CMS's own IFC deck says an agency "must use a reasonable method to **allocate work hours between members of the household**." **How a county applies household MAGI income against an individual-level compliance determination is not spelled out in the ACWDL. FLAGGED — see `research/flagged-items.md` item F-01.** | [ACWDL 25-30](https://www.dhcs.ca.gov/wp-content/uploads/2026-04-25-30.pdf) · [42 CFR § 435.552(f)(2)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) · [CMS IFC deck](https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf) |
| No asset test | For MAGI-determined individuals the agency "**must not apply any assets or resources test**". So owning rental property, a Kalshi account balance or savings does **not** disqualify a person from MAGI adult-group Medi-Cal. | [42 CFR § 435.603(g)(1)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603) |

## 7. Converting income to hours when income is below $580

| Step | Verified rule | Source |
|---|---|---|
| When available | "**If the monthly income is less than** the applicable Federal minimum wage requirement … multiplied by 80 hours, **and the agency does not have documentation regarding the number of hours worked**, the agency **may** calculate the hours for work … based on the monthly income as determined under paragraph (f)(2) … provided that the agency **must use a reasonable method to allocate work hours between members of the household**." | [42 CFR § 435.552(e)(2)(i)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) |
| Formula | "the agency **must calculate the hours for work by dividing the monthly income** as determined under paragraph (f)(2) … **by the applicable Federal minimum wage requirement** under 29 U.S.C. 206(a)(1)(C)." | [42 CFR § 435.552(e)(2)(ii)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) |
| Worked arithmetic | $400 ÷ $7.25 = **55.17 hours**. Those hours may then be combined with community service, a work program, or less-than-half-time education hours to reach 80. | Calculation from the cited formula; minimum wage from [DOL](https://www.dol.gov/agencies/whd/minimum-wage) |
| Combination rule | "After the agency determines an applicable individual's hours for work, completing community service, participating in a work program, and less than half-time enrollment in an educational program, **the hours must be added together.**" | [42 CFR § 435.552(e)(4)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) |
| Limit | Hours for work, community service and work program "**must be determined separately and based on the time spent on the specific activity in such month.**" | [42 CFR § 435.552(e)(2)](https://www.ecfr.gov/current/title-42/part-435/section-435.552) |

## 8. Can trading hours or property-management hours count as "work" hours?

| Scenario | Assessment | Confidence & source |
|---|---|---|
| **Managing rental property you own** — collecting rent, arranging repairs, screening tenants | "Work" is defined as "**work in exchange for money**", "work in exchange for goods or services ('in-kind' work)" and "**unpaid work** (other than community service)". CMS's preamble states self-employment — "starting a business, **owning a business**, or as an independent contractor" — meets the definition and that "the hours the individual spends performing these duties would count toward meeting the 80-hour requirement." | **Reasonable reading, but not squarely addressed.** No official CMS/DHCS document uses the words "landlord", "rental property" or "property manager". **FLAGGED — item F-02.** Sources: [42 CFR § 435.552(b)](https://www.ecfr.gov/current/title-42/part-435/section-435.552); [91 FR 33348, section II.C.1](https://www.federalregister.gov/documents/2026-06-03/2026-11094/medicaid-program-community-engagement-requirement-for-certain-individuals) |
| **Managing property for a fee, for third-party owners** | This is ordinary self-employment / a trade or business. Hours count as work; the fee income is **earned** income and self-employment income. | **Well supported.** Same sources plus [IRS EITC Central](https://www.irs.gov/tax-professionals/eitc-central/earned-income-self-employment-income-and-business-expenses) |
| **Full-time Kalshi event-contract trading** | No official federal or California Medicaid guidance, and no IRS ruling, addresses prediction-market or event-contract trading in the community-engagement context. Two independent obstacles: (a) it is unclear whether event contracts are "securities" for §475(c)(2) purposes, so the IRS **trader** framework may not even apply; and (b) even if it did, trader gains are **not** self-employment income. | **UNVERIFIED — cannot be confirmed from any official source. Left blank / flagged — item F-03.** Sources checked: [IRS Topic No. 429](https://www.irs.gov/taxtopics/tc429), [Kalshi help center](https://help.kalshi.com/en/articles/13823849-what-tax-documentation-does-kalshi-provide), [42 CFR § 435.552](https://www.ecfr.gov/current/title-42/part-435/section-435.552), [ACWDL 25-30](https://www.dhcs.ca.gov/wp-content/uploads/2026-04-25-30.pdf) |

**Practical conclusion:** the **income pathway** is the reliable route and does not depend on
characterising any hours at all. The **hours** routes are a backup and carry interpretation risk.

## 9. Volatility risk specific to trading and rental income

| Risk | Verified basis | Practical consequence |
|---|---|---|
| **Loss months** | The federal income test is applied to "a month in the period under § 435.556(a)". California requires compliance in **any one month** since the last renewal (WIC §14005.69(d)(2)) and DHCS tells members they can meet it by having the income "**in any month since your last renewal**". | A single qualifying month is enough in California. **This is materially protective for someone with volatile trading income.** |
| **MAGI spikes above 138% FPL** | Medi-Cal adult-group financial eligibility is MAGI ≤138% FPL. Budget period may be current monthly or projected annual at state election ([42 CFR § 435.603(h)](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-G/section-435.603)). | A large trading gain can push MAGI over the Medi-Cal limit → Medi-Cal ends → Covered California special enrollment. **Analysis, flagged as a scenario rather than a quoted rule.** |
| **PTC repayment cap removed** | Covered California (official): "Beginning with the **2026 tax year (filed in 2027)**, people who get too much financial help **may need to pay back the full amount they owe. It will no longer be capped based on income.**" | Under-estimating MAGI when trading gains are volatile now carries **unlimited** repayment exposure. Source: [Covered California — Important Changes](https://www.coveredca.com/important-changes) |
| **Up-front proof of subsidy eligibility from 2028** | Covered California (official): "**Effective Date: Jan. 1, 2028** — You'll need to prove that you qualify for financial help before you get it. Financial help won't be applied while your information is being reviewed or updated. If you don't confirm or update your information, you won't be automatically re-enrolled with financial help for the next plan year." | Source: [Covered California — Important Changes](https://www.coveredca.com/important-changes) |
| **Seasonal-worker averaging is narrow** | §435.552(a)(7)/(g) requires the person to be "a **seasonal worker**, as described in section 45R(d)(5)(B) of the Internal Revenue Code of 1986". **26 U.S.C. §45R(d)(5)(B) (official U.S. Code text):** "The term '**seasonal worker**' means a worker who **performs labor or services on a seasonal basis as defined by the Secretary of Labor**, including workers covered by **section 500.20(s)(1) of title 29, Code of Federal Regulations** and **retail workers employed exclusively during holiday seasons**." | **The 6-month averaging route is probably NOT available to a full-time trader or full-time property manager** — neither performs labor "on a seasonal basis" as defined by the Secretary of Labor. Do **not** rely on the averaging rule; rely on the single-month test (California only requires **any one month** since the last renewal). **FLAGGED — item F-05.** Sources: [26 U.S.C. §45R (official U.S. Code, govinfo PDF)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/pdf/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartD-sec45R.pdf); [42 CFR § 435.552(g)](https://www.ecfr.gov/current/title-42/part-435/section-435.552); [ACWDL 25-30](https://www.dhcs.ca.gov/wp-content/uploads/2026-04-25-30.pdf) |
