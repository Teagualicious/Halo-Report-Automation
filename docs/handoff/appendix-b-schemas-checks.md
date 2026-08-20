# Appendix B: schemas and acceptance checks

# B.1 Canonical geo-week analysis table

| **Field**                | **Type**     | **Definition / validation**                                                         |
|--------------------------|--------------|-------------------------------------------------------------------------------------|
| **client_alias**         | string       | No direct client name in public code or test data.                                  |
| **campaign_id**          | string       | Stable internal identifier.                                                         |
| **analysis_geo_id**      | string       | Supported Trends geography identifier.                                              |
| **week_start**           | date         | Consistent UTC-aligned weekly boundary for 30+ day Trends windows \[1\].            |
| **treated**              | integer      | 1 when geography belongs to the approved treated group.                             |
| **post**                 | integer      | 1 beginning at material campaign start for the geography.                           |
| **impressions**          | numeric      | Nonnegative actual delivered impressions.                                           |
| **reach**                | numeric/null | Unique reach when available; must not exceed selected universe without explanation. |
| **targetable_universe**  | numeric      | Population/households/audience denominator.                                         |
| **impressions_per_1000** | numeric      | 1,000 × impressions / targetable_universe.                                          |
| **brand_index**          | numeric      | Median across frozen repeated pulls; nonnegative.                                   |
| **category_index**       | numeric      | Median across frozen repeated pulls; strictly positive for ratio model.             |
| **halo_index**           | numeric      | ln(brand_index / category_index) when eligible.                                     |
| **mapping_coverage**     | numeric      | Share of delivery allocated to the analysis geography.                              |
| **event_flags**          | string/list  | Known external events active in geo/week.                                           |

## B.2 Configuration fields

| **Section**   | **Example fields**                                                                              |
|---------------|-------------------------------------------------------------------------------------------------|
| **client**    | alias, campaign IDs, owner, approved output mode.                                               |
| **dates**     | pre_start, campaign_start, campaign_end, carryover_end.                                         |
| **search**    | brand basket ID, category basket ID, search type, category filter, time grain, pull count.      |
| **geography** | ZIP crosswalk release, allocation ratio, analysis level, treated/control IDs, spillover buffer. |
| **exposure**  | primary measure, universe source, treatment threshold, weight bins.                             |
| **model**     | estimator branch, covariates, inference method, reference week, sensitivity variants.           |
| **reporting** | rounding, evidence tier, client-safe labels, suppressed fields.                                 |

## B.3 Automated acceptance checks

| **Check ID** | **Rule**                                                                                      | **Blocking?** |
|--------------|-----------------------------------------------------------------------------------------------|---------------|
| **QA-01**    | Campaign delivery sum reconciles to source total.                                             | Yes           |
| **QA-02**    | At least the approved mapping-coverage threshold is allocated.                                | Yes           |
| **QA-03**    | No duplicate client/campaign/geo/week/source rows.                                            | Yes           |
| **QA-04**    | Brand and category zero/suppression rates below approved threshold.                           | Yes           |
| **QA-05**    | Repeated-pull variability below approved threshold or explicitly downgraded.                  | Yes           |
| **QA-06**    | No post-period information used to select controls or query terms.                            | Yes           |
| **QA-07**    | Report and dashboard lift equal canonical output after rounding.                              | Yes           |
| **QA-08**    | All charts include source, period, geography and metric definition.                           | Yes           |
| **QA-09**    | Placebo/sensitivity/influence results are attached.                                           | Yes           |
| **QA-10**    | Client-safe artifact contains no other client, control-market intelligence or restricted IDs. | Yes           |

## B.4 Final launch checklist

- Sponsor has approved the primary business question and scope.

- Methods reviewer has approved analysis design and claim language.

- Data owner has reconciled campaign delivery.

- Account lead has reviewed events, query meaning and client narrative.

- Dashboard owner has accepted the data contract and operating runbook.

- Security/client-safety review has passed.

- Clean rerun and report/dashboard parity checks have passed.

- Release is tagged and archived with the decision log and residual risks.

# References

Official source behavior, geography definitions and methodological research used in the handoff.

**\[1\]** Google Trends Help. “FAQ about Google Trends data.” Sampled and normalized data, 0-100 scaling, city-level statement, low-volume suppression, statistical noise and UTC timing. [Source](https://support.google.com/trends/answer/4365533?hl=en)

**\[2\]** Google Trends Help. “Explore results by region.” Regional/city rankings and metro availability. [Source](https://support.google.com/trends/answer/4355212?hl=en)

**\[3\]** Google Trends Help. “Compare Trends search terms.” Query groups, term variants and term-versus-topic behavior. [Source](https://support.google.com/trends/answer/4359550?hl=en)

**\[4\]** Google Search Central. “Google Trends API Alpha.” Limited alpha access, five-year window, consistent scaling and region/subregion data. [Source](https://developers.google.com/search/apis/trends)

**\[5\]** Google Ads API. “Generate Historical Metrics.” Approximate monthly keyword search volume and geo-target parameters. [Source](https://developers.google.com/google-ads/api/docs/keyword-planning/generate-historical-metrics)

**\[6\]** U.S. Census Bureau. “ZIP Code Tabulation Areas (ZCTAs).” ZCTA construction and distinction from USPS ZIP delivery areas. [Source](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html)

**\[7\]** HUD USER. “HUD-USPS ZIP Code Crosswalk Files.” Allocation between ZIP Codes and Census geographies. [Source](https://www.huduser.gov/apps/public/uspscrosswalk/home)

**\[8\]** Callaway, B., and Sant’Anna, P. H. C. (2021). “Difference-in-Differences with Multiple Time Periods.” Journal of Econometrics, 225(2), 200-230. [Source](https://doi.org/10.1016/j.jeconom.2020.12.001)

**\[9\]** Callaway, B., Goodman-Bacon, A., and Sant’Anna, P. H. C. (2024; revised 2026). “Difference-in-Differences with a Continuous Treatment.” NBER Working Paper 32117. [Source](https://www.nber.org/papers/w32117)

**\[10\]** Au, T. (2018). “A Time-Based Regression Matched Markets Approach for Designing Geo Experiments.” Google Research. [Source](https://research.google/pubs/a-time-based-regression-matched-markets-approach-for-designing-geo-experiments/)

**\[11\]** Brodersen, K. H., Gallusser, F., Koehler, J., Remy, N., and Scott, S. L. (2015). “Inferring causal impact using Bayesian structural time-series models.” [Source](https://arxiv.org/abs/1506.00356)

**\[12\]** Gummer, T., and Oehrlein, A.-S. (2024). “Using Google Trends Data to Study High-Frequency Search Terms: Evidence for a Reliability-Frequency Continuum.” Social Science Computer Review. [Source](https://consensus.app/papers/using-google-trends-data-to-study-highfrequency-search-gummer-oehrlein/008d63a67ac7566fb4f3c763e8b9359e/)

**\[13\]** Eichenauer, V. Z., Indergand, R., Martínez, I. Z., and Sax, C. (2021). “Obtaining consistent time series from Google Trends.” Economic Inquiry. [Source](https://consensus.app/papers/obtaining-consistent-time-series-from-google-trends-eichenauer-indergand/c34b38281309543383cc5d5814687939/)

**\[14\]** Raubenheimer, J. (2023). “Of babies, bathwater, and big data: Going beneath the surface of Franzén’s Google Trends recommendations.” Acta Sociologica. [Source](https://consensus.app/papers/of-babies-bathwater-and-big-data-going-beneath-the-surface-raubenheimer/349e190d3c9a5cd1b97c422e14a621f7/)

**\[15\]** Goldfarb, A., Tucker, C., and Wang, Y. (2022). “Conducting Research in Marketing with Quasi-Experiments.” Journal of Marketing, 86, 1-20. [Source](https://consensus.app/papers/conducting-research-in-marketing-with-quasiexperiments-goldfarb-tucker/9edec41c040852e59bc012ddcbe961d5/)

**\[16\]** Google Ads API. “Location targeting.” Targetable geographic regions, including postal regions where supported, and presence versus presence-or-interest settings. [Source](https://developers.google.com/google-ads/api/docs/targeting/location-targeting)

**\[17\]** Hölzl, J., Keusch, F., and Sajons, C. (2025). “The (mis)use of Google Trends data in the social sciences - A systematic review, critique, and recommendations.” Social Science Research, 126. [Source](https://consensus.app/papers/the-misuse-of-google-trends-data-in-the-social-sciences-a-h%C3%B6lzl-keusch/a4507c88bbc452f9be955fbd89a97825/)

## Research note

The document uses official product documentation for current platform capabilities and published methodological literature for design risks. Google Trends and Google Ads capabilities can change; reverify source behavior at project start and record the version/date in the decision log.

## Project handoff complete

**Build the evidence first. Then build the story around what the evidence can support.**

Next gate: sponsor scope decision plus campaign/data feasibility audit.
