# Research and verification notebook

Research snapshot: **2026-10-18 (UTC)**. Session: `8a956ff3`.

This is a review of the provisions relevant to a U.S. citizen who reports California residency, no earned income, property-management activity, Kalshi trading, rental income, and savings interest. It is not an eligibility determination, tax return, or exhaustive review of every provision of Public Law 119-21. No age, household size, income amount, medical condition, contract classification, or county has been assumed.

## Method

- Search was used to discover primary sources. Claims are checked against retrieved text on official government or Covered California websites, not search snippets or commercial summaries.
- Sources were accessed with the research retrieval tool. Direct network access from the build sandbox to government websites is restricted; a local HTTP crawler cannot independently certify those sites. The source register will distinguish source-content access from local link/build tests.
- PDFs are reviewed only for the relevant accessible pages, not presumed fully reviewed. The complete federal rule is 135 pages; the eCFR sections and CMS guidance provide accessible operative text. eCFR is a government-maintained, authoritative but unofficial legal edition; the Federal Register page links the official GovInfo PDF.
- Every final data row will have an official source, locator, and specific evidence references. Unknown values will be empty strings, not zeroes or estimates. Interpretation and recommendations will be labeled separately from verified general rules.
- Dynamic pages can change. Snapshot date, source dates, effective dates, and a row-level verification log will be retained. Re-running tests does not re-verify the law.

## Principal findings checked so far

1. **No earned income is not the same as no MAGI-based income.** 42 CFR 435.552(a)(6), (f) permits the income alternative, using MAGI-based income for the MAGI household; this is not a wages-only test. The July 2026 CMS deck, slide 13, explicitly describes the household methodology. California's September 11, 2026 MEDIL I 26-25 enclosure says “income from any source” of at least $580 in a month since the last renewal. This phrase must be read with the federal MAGI rules, not as including every bank deposit or gift.
   - <https://www.ecfr.gov/current/title-42/section-435.552>
   - <https://www.medicaid.gov/medicaid/downloads/ce-requirement-ifc-deck.pdf>
   - <https://www.dhcs.ca.gov/wp-content/uploads/2026/09/MEDIL-I26-25.pdf>
2. **Paid employment is not the only route.** Section 435.552 confirms 80 hours of work, structured community service, a qualifying work program, combinations, or at least half-time enrollment. Work includes paid, in-kind, and unpaid work. School determines half-time status. The federal six-month income-average alternative explicitly requires seasonal-worker status.
3. **The general California start remains January 1, 2027 in the current guidance reviewed.** DHCS ACWDL 26-14 (August 27, 2026), pp. 3–6, clarifies the existing-member renewal transition beginning with renewals due March 2027. January/February 2027 annual renewals stay annual until 2028. Do not equate the March renewal rollout with a universal delay of new-application rules.
   - <https://www.dhcs.ca.gov/wp-content/uploads/2026/09/ACWDL-26-14.pdf>
   - <https://www.dhcs.ca.gov/medi-cal/updates/medi-cal-changes/>
4. **Ordinary financial eligibility still matters.** The community-engagement income floor is distinct from the Medi-Cal income ceiling. MAGI Medicaid has no asset/resource test under 435.603(g). Its applicant budget period is current monthly household income under 435.603(h). Non-MAGI asset rules must not be applied to MAGI expansion adults.
   - <https://www.ecfr.gov/current/title-42/section-435.603>
5. **Rental income and investment interest generally count.** HealthCare.gov lists net rental income, capital gains, investment interest and tax-exempt interest. IRS Topic 414 addresses rental expenses and limitations; Topic 403 addresses interest. Tax rules do not themselves adjudicate Medicaid work hours.
   - <https://www.healthcare.gov/income-and-household-information/income/>
   - <https://www.irs.gov/taxtopics/tc414>
   - <https://www.irs.gov/taxtopics/tc403>
6. **Kalshi classification remains unverified for this user's actual contracts.** The CFTC designation establishes exchange status, not an IRS determination that each contract is section 1256. IRS Form 6781 describes qualifying contracts and exclusions. IRS Topic 429 concerns securities traders and is not a Kalshi-specific ruling. Do not assume section 1256, Schedule C earned income, a 60/40 split, or accepted Medicaid trading hours.
   - <https://www.cftc.gov/PressRoom/PressReleases/8302-20>
   - <https://www.irs.gov/pub/irs-pdf/f6781.pdf>
   - <https://www.irs.gov/taxtopics/tc429>
7. **Covered California is an alternative when eligible, not an automatic subsidy escape after work-rule noncompliance.** MEDIL I 26-25 warns of loss of financial help in that circumstance. The final 2027 California Premium Subsidy Program Design, (c)(2), requires all federal APTC eligibility requirements. It expands state premium assistance to eligible filers at 100–200% FPL, not a universal $0-earned-income exception.
   - <https://hbex.coveredca.com/data-research/Final-2027-California-Premium-Subsidy-Program-Design.pdf>
8. **California is helping with administration and subsidies and seeking changes, not providing a confirmed blanket exemption.** The October 1 Oregon governor's official release confirms California joined a request for more implementation time. The DHCS tracking page confirms California's lawsuit. Neither proves an approved delay or a court order invalidating the requirement.
   - <https://apps.oregon.gov/oregon-newsroom/OR/GOV/Posts/Post/governor-kotek-pushes-for-more-time-to-protect-medicaid-coverage>
   - <https://www.dhcs.ca.gov/tracking-federal-impact-medi-cal-eligibility/>

## Irregularities to publish on Flagged for Review

- **Gross / earned / MAGI wording:** preliminary ACWDL 25-30 uses “total gross income”; public DHCS pages say work and earn $580; the September notice says any source; the federal rule requires MAGI-based methodology. Use the federal methodology and September notice for the general income route; leave the user's calculated income blank.
- **Seasonal averaging:** early California guidance and its September outreach describe broader fluctuating income. Section 435.552(g) explicitly conditions the six-month average on seasonal-worker status. Do not assume variable trading returns alone qualify.
- **Timing:** the September outreach enclosure says March 2027, while the cover letter and general work-rule page say January 1. ACWDL 26-14 clarifies renewal initiation and phase-in; the user's first assessment month remains blank.
- **Caregiver age wording:** DHCS's federal-impact page says “under 13”; 435.554 and the member notice say **13 or younger**. Use the regulatory language; flag the abbreviated webpage.
- **Notice deadline:** preliminary ACWDL 25-30 counts 30 days from notice date. Current 435.558(a)(2), (c)(4) provides 30 days from receipt, presumed five days after notice date unless shown otherwise. Publish the current federal rule and flag the older wording.
- **Dynamic FPL chart:** the search excerpt labeled the generic Covered California `FPL-chart.pdf` as 2026; its retrieved text is now **2027**, and explicitly references **2026** DHCS Medi-Cal values. The 2027 Medi-Cal ceilings cannot be filled in from that chart. Use the standalone 2026 DHCS enclosure for current monthly thresholds.
- **Legal challenge / delay:** an official filing announcement and an extension request are verified, but a superseding final outcome or approved California good-faith exemption was not confirmed. Do not infer relief. 435.560 permits limited CMS-approved extensions, not automatic delays.
- **Personal facts and Kalshi/property-manager hours:** all eligibility, MAGI, contract classification, accepted hours, county hardship status, and premium estimates remain undetermined.

## Access anomalies (not used as authorities)

- The attempted Covered California URL `/support/before-you-buy/when-can-i-buy-health-insurance/` returned a soft-404 (“Sorry! That page doesn't exist.”). It will not be linked on the site. Use the July 21, 2026 official rate announcement / current enrollment guidance instead.
- IRS Form 6781 PDF extraction includes long dotted form lines. Verify substantive instructions in the later chunks, not the form's layout artifacts.
- No third-party tax blog, insurer marketing page, commercial eligibility calculator, or news article is being promoted to a verified authority.

## Original repository audit

The initial repository contained only the title `# MaltaProj9` in `README.md`. There were no pre-existing healthcare claims, tables, dependencies, site implementation, or scripts to verify line by line. GitHub Pages was already configured to publish the `main` branch root. All substantive content in this project is new work with the provenance described above.
