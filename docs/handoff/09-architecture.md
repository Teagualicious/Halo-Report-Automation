# Technical architecture and reproducibility

# 9.1 Recommended architecture

| **Layer**          | **Responsibility**                                                                    | **Implementation guidance**                                                    |
|--------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Configuration**  | Client/campaign/query/geography/model settings.                                       | YAML or JSON; versioned; no client secrets; schema validated.                  |
| **Raw inputs**     | Immutable source exports and reference files.                                         | Restricted storage; source naming standard; checksums.                         |
| **Ingestion**      | Read, type-check, standardize and log source data.                                    | Python scripts/modules; notebooks may inspect but not define production logic. |
| **Transformation** | Crosswalk ZIPs, aggregate search pulls, normalize exposure and create geo-week table. | Deterministic functions with unit tests.                                       |
| **Modeling**       | Ratio-of-ratios, DiD/event study, alternative method branch and sensitivity.          | Single model-output table consumed by all products.                            |
| **Validation**     | Automated QA, placebos, influence, pre-trend and first-party comparison.              | Machine-readable flags plus a review report.                                   |
| **Presentation**   | Report charts, dashboard data and client-safe exports.                                | Read from approved output tables only; no recalculation in visuals.            |

## 9.2 Suggested repository structure

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>halo-analysis/<br />
├── README.md<br />
├── status.md<br />
├── docs/<br />
│ ├── methodology.md<br />
│ ├── data_dictionary.md<br />
│ ├── query_registry.md<br />
│ ├── decisions.md<br />
│ └── runbook.md<br />
├── configs/<br />
│ ├── client_a.yaml<br />
│ └── client_b.yaml<br />
├── data/<br />
│ ├── raw/ # restricted / not committed<br />
│ ├── interim/<br />
│ ├── processed/<br />
│ └── reference/<br />
├── src/<br />
│ ├── ingest/<br />
│ ├── search/<br />
│ ├── geography/<br />
│ ├── exposure/<br />
│ ├── model/<br />
│ ├── validation/<br />
│ └── reporting/<br />
├── dashboard/<br />
├── reports/<br />
├── tests/<br />
├── audit/<br />
└── releases/</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 9.3 Canonical model-output table

| **Field**                                         | **Purpose**                                              |
|---------------------------------------------------|----------------------------------------------------------|
| **run_id**                                        | Unique link across source, model, report and dashboard.  |
| **client_alias / campaign_id**                    | Configuration identity.                                  |
| **analysis_geo_level**                            | City, metro/market, state or pooled panel.               |
| **analysis_window**                               | Pre, flight and carryover dates.                         |
| **query_registry_version**                        | Exact brand/category definition.                         |
| **control_set_version**                           | Exact comparison geographies and matching method.        |
| **estimate / standard_error / interval**          | Primary effect and uncertainty.                          |
| **lift_percent**                                  | 100 × \[exp(beta) - 1\] or approved simple equivalent.   |
| **pretrend_flag / placebo_flag / influence_flag** | QA outcomes.                                             |
| **evidence_tier**                                 | Approved interpretation ceiling.                         |
| **result_status**                                 | PASS, DIRECTIONAL, DESCRIPTIVE or INSUFFICIENT_EVIDENCE. |

## 9.4 Technology choice

Use the team’s approved analytics environment. A practical Python stack is pandas or polars, geopandas, statsmodels/linearmodels, Plotly and Streamlit or an approved BI layer. An R implementation may use packages designed for modern DiD and time-series counterfactual analysis. Regardless of language, the production calculation must live in tested scripts, not only in a notebook or dashboard formula.

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>Do not make the project dependent on unofficial scraping</strong></p>
<p>Prefer the official Trends alpha API if access is granted and the needed geographies are verified. Otherwise use governed manual exports or an approved licensed provider. Unofficial scraping may be useful for exploration but should not be the only production path.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 9.5 Run manifest

- Run ID and timestamp; analyst; Git commit; environment/package lockfile.

- Source filenames, row counts, hashes and retrieval timestamps.

- Client/campaign/query/control/geography configuration versions.

- Model formula, inference method, random seed and exception overrides.

- QA results, evidence tier, report/dashboard artifact hashes and approval status.
