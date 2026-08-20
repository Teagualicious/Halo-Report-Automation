# Campaign selection and feasibility

# 5.1 Mandatory pass/fail gates

| **Gate** | **Requirement**                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| **G1**   | Actual delivery is available by geography and week, and totals reconcile to the campaign delivery source.                            |
| **G2**   | The campaign produced meaningful geographic exposure contrast: credible low/no-delivery comparisons exist.                           |
| **G3**   | The brand and category query baskets have stable, non-suppressed signal at a defensible geography.                                   |
| **G4**   | There is enough pre-period history to inspect trends and enough campaign/post data to measure response.                              |
| **G5**   | Major concurrent national media, promotions, PR events or operational changes are documented and do not make attribution impossible. |
| **G6**   | The ZIP-to-analysis-geography mapping is complete and the selected parent geography does not create excessive exposure mixing.       |
| **G7**   | Client/data governance permits the analysis and the planned dashboard/report view.                                                   |

## 5.2 Candidate comparison scorecard

After all mandatory gates pass, use the following scorecard to choose the primary and replication cases. Score each dimension 0 = weak, 1 = workable, 2 = strong. The score is a prioritization aid, not evidence of validity.

| **Dimension**           | **0 - weak**                          | **1 - workable**              | **2 - strong**                                 |
|-------------------------|---------------------------------------|-------------------------------|------------------------------------------------|
| **Search signal**       | Frequent suppression / unstable pulls | Usable only after aggregation | Stable at multiple geographies and pulls       |
| **Geo contrast**        | Nearly universal or diffuse delivery  | Some low/high variation       | Clear treated and credible comparison markets  |
| **Pre-period fit**      | Visible divergence                    | Mixed fit                     | Strong visual fit across long pre-period       |
| **Delivery data**       | Targets or monthly totals only        | Weekly impressions by geo     | Weekly impressions, reach, frequency and spend |
| **Confounds**           | Major undocumented overlap            | Known and partly controllable | Clean event calendar and limited overlap       |
| **Validation outcomes** | None available                        | One directional outcome       | Multiple first-party outcomes                  |
| **Executive relevance** | Limited decision value                | Useful case                   | Clear optimization or client-story value       |

## 5.3 Recommended campaign profile

- A campaign with concentrated local-market delivery rather than nationwide saturation.

- A recognizable consumer brand with enough branded-search volume but not one dominated by constant national news.

- A clearly bounded flight, stable creative/offer and limited overlapping major promotions.

- At least several treated and comparison analysis geographies, or one strong treated market with a long pre-period for synthetic control.

- A practical first-party validation outcome, such as branded query clicks, direct/organic sessions, store-locator activity, calls or qualified leads.

## 5.4 Go/no-go meeting output

| **Output**                    | **Required content**                                                                    |
|-------------------------------|-----------------------------------------------------------------------------------------|
| **Candidate decision log**    | Primary case, replication case, rejected cases and reason for rejection.                |
| **Analysis level**            | ZIP display grain, selected search-analysis geography, mapping method and leakage rate. |
| **Search feasibility packet** | Term baskets, pull settings, zero rate, repeated-pull variance and selected time grain. |
| **Control strategy**          | Candidate comparison geographies and pre-period similarity summary.                     |
| **Known-events calendar**     | Concurrent campaigns, offers, PR, outages, openings, competitor events and holidays.    |
| **Evidence ceiling**          | Strong quasi-experimental, directional, or descriptive-only ceiling before modeling.    |
