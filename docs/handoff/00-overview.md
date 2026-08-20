# Overview and TL;DR

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>HALO</strong></p>
<p><strong>Brand-Lift Measurement</strong></p>
<p>Intern Project Handoff and Implementation Blueprint</p>
<p>Difference-in-differences case studies | Branded-search halo | Impression-weight response</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>ASSIGNED PROJECT</strong></p>
<p><em>“Brand-lift measurement case study ("Halo" analysis): Apply difference-in-differences methods to 1-2 campaigns for a high-tier client, measuring how campaign reach translated into organic branded search interest relative to category-level search controls, with campaign delivery data used to analyze response to impression weight. Deliverables: brand-lift chart and written methods summary with an estimated lift figure.”</em></p>
<p><strong>Prepared for project initiation | Research current as of August 20, 2026</strong></p></td>
</tr>
</tbody>
</table>

This handoff converts the assignment into a defensible measurement product, a phased project board, two client-ready report paths, a reusable dashboard specification, and a reproducibility package. It also records a separate skeptical review and the changes adopted in response.

# TL;DR - What this project is actually building

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>The simple explanation</strong></p>
<p>Did branded search grow more in places that actually received the campaign than in comparable places that did not, after removing the broader change in category search? Then, where the data permit, did markets receiving more impression weight show more lift?</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Recommendation at a glance

| **Decision**        | **Recommendation**                                                                                            | **Why**                                                                                                          |
|---------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Overall**         | Proceed, with a revised geography and evidence design.                                                        | The assignment is viable, but public Google Trends should not be treated as a ZIP-level time-series source.      |
| **Scope**           | One primary high-tier client with 1-2 campaigns; a second client is a replication stretch goal.               | This matches the written assignment and avoids forcing two weak case studies.                                    |
| **Geography**       | Keep ZIP-level campaign delivery in the map; estimate search lift at the smallest stable supported geography. | Official Google Trends documentation supports regional, metro and city-level views, not ZIP time series \[1-2\]. |
| **Method**          | Use a brand-versus-category, treated-versus-control, post-versus-pre design.                                  | This creates a clearer counterfactual than a simple before/after comparison.                                     |
| **Exposure**        | Use actual delivered reach/impressions, normalized to market size.                                            | Target lists do not prove exposure, and raw impressions are not comparable across market sizes.                  |
| **Dashboard**       | Build one reusable Halo Explorer with client/campaign filters, not two separate applications.                 | The method is the product; the interface should be a configurable presentation layer.                            |
| **Causal language** | Use an evidence tier and report uncertainty.                                                                  | Observational delivery allocation can remain confounded even when a DiD estimate is statistically precise.       |

## Core deliverables

> **1.** A shared Halo Methodology and Validation Guide containing the exact calculation, assumptions, query rules, geography rules, QA tests and interpretation language.
>
> **2.** Client Report A: the primary case study, including campaign footprint, brand-lift chart, estimated lift with interval, event-study/pre-trend view, impression-weight analysis and limitations.
>
> **3.** Client Report B: a replication case study only if the second campaign/client clears the data-quality gate; otherwise, a documented feasibility/validation memo explaining why a defensible lift estimate was not produced.
>
> **4.** One reusable Halo Explorer dashboard with client, campaign, parent market and ZIP selectors. ZIP clicks show ZIP delivery and the lift estimate for the supported parent analysis geography.
>
> **5.** A reproducibility bundle: source extracts, versioned configuration files, data dictionary, model code, test results, run manifest and final-output archive.

## Four non-negotiable guardrails

- Do not label a parent-market Google Trends estimate as a ZIP-level lift estimate.

- Do not call Google Trends values absolute search volume, organic clicks, conversions or sales; they are relative search-interest indices \[1\].

- Do not use targeted ZIPs as treatment exposure when actual delivery by geography and time is available.

- Do not interpret a raw correlation between impression weight and search change as a causal dose-response effect.

## Immediate sponsor decisions required

| **Decision**           | **Required choice**                                                    | **Default in this handoff**                                                    |
|------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Scope**              | One client with 1-2 campaigns versus two separate clients.             | One primary client/case plus one replication/stretch case.                     |
| **Data grain**         | Available delivery fields and time grain.                              | ZIP x week with impressions, unique reach, frequency and spend.                |
| **Search access**      | Trends alpha API, approved manual exports, or another licensed source. | Apply for alpha; design a manual-export fallback.                              |
| **Validation**         | First-party metrics that can be used without exposing client data.     | Search Console/website branded behavior or other agreed outcome.               |
| **Dashboard platform** | Approved BI tool, local HTML/Streamlit, or static prototype.           | Use the team’s approved platform; avoid a custom web build until methods pass. |

# Document map

| **Section**    | **Purpose**                                        |
|----------------|----------------------------------------------------|
| **1**          | Assignment interpretation and success criteria     |
| **2**          | Critical assessment of the proposed ZIP-level plan |
| **3**          | Revised deliverable package                        |
| **4**          | Measurement framework and calculation              |
| **5**          | Campaign selection and feasibility gate            |
| **6**          | Data requirements, geography and query governance  |
| **7**          | Phased implementation plan and project board       |
| **8**          | Dashboard and report specifications                |
| **9**          | Technical architecture and reproducibility         |
| **10**         | Validation, QA and evidence grading                |
| **11**         | Roles, governance, risks and definition of done    |
| **12**         | Separate skeptical review and issue resolution     |
| **Appendix A** | Worked lift example                                |
| **Appendix B** | Starter schemas, formulas and acceptance checks    |
| **References** | Official documentation and research basis          |

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>How to use this handoff</strong></p>
<p>The sponsor should approve Sections 1-5 before data work begins. The intern uses Sections 6-9 as the build plan. The methods reviewer signs off on Section 10. The final handoff is complete only when the checks in Section 11 pass.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
