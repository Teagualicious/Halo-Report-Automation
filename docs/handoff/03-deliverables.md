# Revised deliverables

# 3.1 Deliverable architecture

| **Deliverable**                             | **Audience**                              | **Minimum contents**                                                                                        | **Acceptance test**                                                         |
|---------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **D1. Halo Methodology & Validation Guide** | Analysts, leadership, reviewers           | Definitions, data rules, query registry, geography rules, equations, assumptions, QA, evidence language.    | A second analyst can reproduce the method without oral clarification.       |
| **D2. Client Report A**                     | Account leadership and high-tier client   | Executive result, delivery footprint, lift chart, event study, weight response, validation and limitations. | Every claim traces to a governed output and uses approved evidence wording. |
| **D3. Client Report B / Replication Memo**  | Internal sponsor; client if qualified     | Same report template if feasibility passes; otherwise a no-go diagnostic and next-test plan.                | No unsupported lift number is issued solely to satisfy a two-report target. |
| **D4. Halo Explorer Dashboard**             | Internal users; client-safe view optional | Client/campaign filters, ZIP delivery map, parent-geo lift, trend, dose response, methods/QA.               | Dashboard result exactly matches report and model-output table.             |
| **D5. Reproducibility Bundle**              | Future analyst and technical owner        | Configs, code, source inventory, run manifest, tests, model outputs, archive.                               | Clean rerun produces the same rounded lift and charts.                      |

## 3.2 Recommended report count

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>Primary commitment</strong></p>
<p>Commit to one gold-standard report and one replication path. Produce the second client-facing report only if it clears the same feasibility and QA gates.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This adjustment preserves the requested two-report structure while making research integrity explicit. The fallback is not an incomplete deliverable: it is a documented feasibility memo showing search-volume tests, control availability, data gaps, confounds and the exact changes needed for a future valid case study.

## 3.3 Why one dashboard is preferable to two

- A shared data contract prevents Client A and Client B from silently using different calculations.

- Client-specific query baskets and geographies can live in configuration files rather than duplicated code.

- Fixes to calculations, labels or QA logic apply to both cases.

- The intern’s effort remains centered on measurement quality rather than application maintenance.

- A client-safe export can hide control identities, internal notes and other clients while retaining the same calculation.

## 3.4 Minimum viable product versus stretch

| **Layer**       | **Minimum viable**                                                       | **Stretch after validation**                                                 |
|-----------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Method**      | One reproducible binary lift estimate with event-study/pre-trend checks. | Alternative estimators, heterogeneous effects and automated model selection. |
| **Search data** | Approved CSV exports with a repeat-pull protocol.                        | Limited alpha API integration and scheduled retrieval.                       |
| **Exposure**    | Weekly impressions and normalized impression weight.                     | Reach/frequency curves, channel-specific weight and carryover.               |
| **Dashboard**   | Local or approved BI dashboard with four pages.                          | Automated refresh, access controls and client-specific publishing.           |
| **Validation**  | At least one first-party outcome or a documented unavailability.         | Multiple outcomes, placebo campaigns and prospective geo holdout design.     |
