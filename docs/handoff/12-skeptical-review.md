# Independent skeptical review

# 12.1 Review mandate

The skeptical review was conducted separately from the proposal-writing pass and asked: “What would make the reported lift wrong, non-reproducible or misleading even if the dashboard looks convincing?” The review was cross-checked against current official Google documentation and the cited causal-inference and Google Trends reliability research.

# 12.2 Red-team findings and adopted changes

| **\#** | **Challenged assumption**                     | **Failure mode**                                                                          | **Adopted change**                                                         | **Status** |
|--------|-----------------------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------|
| **1**  | “Click a ZIP to see ZIP lift.”                | Public Trends does not provide a defensible ZIP time series.                              | ZIP displays delivery; parent geography displays lift with explicit label. | Resolved   |
| **2**  | Targeted ZIPs define treatment.               | Targeting does not equal actual exposure.                                                 | Treatment uses delivered impressions/reach by geo/week.                    | Resolved   |
| **3**  | Trends index equals search volume.            | Values are sampled, normalized and 0-100 scaled.                                          | Use relative-interest language and scale-invariant ratios.                 | Resolved   |
| **4**  | One pull is the data.                         | Sampling/noise can change repeated downloads.                                             | Repeat pulls, median aggregation and source-variability sensitivity.       | Resolved   |
| **5**  | Category control is automatically unaffected. | Campaign messaging can also raise category terms.                                         | Use multiple generic controls, inspect movement and add negative controls. | Resolved   |
| **6**  | Before/after chart proves lift.               | Seasonality and common shocks create false effects.                                       | Add matched geography and event-study counterfactual.                      | Resolved   |
| **7**  | More impressions imply causal response.       | Weight allocation can be endogenous.                                                      | Binary primary effect; dose response secondary with conservative language. | Resolved   |
| **8**  | All nearby markets are valid controls.        | Media and people cross borders; spillover contaminates controls.                          | Audit delivery leakage and exclude/buffer contaminated controls.           | Resolved   |
| **9**  | Standard DiD works for any campaign.          | One/few geos, staggered starts or universal treatment need other methods.                 | Use the design decision tree and evidence downgrade/no-go branch.          | Resolved   |
| **10** | Two reports must contain two lift numbers.    | The second case may fail signal or control gates.                                         | Allow a rigorous feasibility memo instead of a fabricated estimate.        | Resolved   |
| **11** | Dashboard can recalculate metrics.            | Duplicate business logic causes silent disagreement.                                      | Single canonical model-output table feeds every product.                   | Resolved   |
| **12** | A significant coefficient is enough.          | Pre-trends, source variance, influence and confounds can still invalidate interpretation. | Mandatory validation matrix and evidence tier.                             | Resolved   |

## 12.3 Residual risks that cannot be fully eliminated retrospectively

- Unobserved market-specific events may remain even after matching and category controls.

- Actual individual exposure and individual search behavior are not linked; the design is aggregate and ecological.

- Google Trends remains a sampled relative-interest source rather than a transaction ledger.

- Campaign-delivery allocation may remain correlated with expected demand, especially for weight-response analysis.

- Search interest may occur outside the user’s home or delivery ZIP and may spill across market borders.

- A retrospective design is generally weaker than a prospectively randomized geo holdout.

## 12.4 Red-team verdict

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>CONDITIONALLY APPROVED</strong></p>
<p>The project is defensible and high-value only with the revised geography, actual-delivery treatment, matched counterfactual, repeated-source QA, validation matrix and evidence-tier language. The original ZIP-level Google Trends dashboard concept is not approved as stated.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 12.5 Completeness audit

| **Dimension**      | **Covered in handoff**                                                                      | **Remaining sponsor input**                     |
|--------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------|
| **Business scope** | Assignment interpretation, deliverables, client/campaign scope and success criteria.        | Final primary/replication scope.                |
| **Data**           | Delivery, search, geography, universe, event and validation schemas.                        | Actual source access and field availability.    |
| **Method**         | Calculation, model branches, event timing, exposure weight and inference.                   | Methods reviewer/tool preference.               |
| **Validation**     | QA, pre-trends, placebos, negative controls, sensitivity, influence and first-party checks. | Available first-party outcome.                  |
| **Product**        | Report structure, dashboard pages, filters, labels and client-safe rules.                   | Approved dashboard platform and brand template. |
| **Governance**     | RACI, access, versioning, client privacy and approvals.                                     | Named owners/security requirements.             |
| **Handoff**        | Repository, status file, run manifest, runbook, rerun and definition of done.               | Final storage/deployment location.              |
