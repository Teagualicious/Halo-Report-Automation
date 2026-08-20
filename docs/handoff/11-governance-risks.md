# Roles, risks, and definition of done

# 11.1 RACI

| **Workstream**           | **Intern** | **Sponsor** | **Methods reviewer** | **Ad ops / data** | **Account lead** | **Dashboard owner** |
|--------------------------|------------|-------------|----------------------|-------------------|------------------|---------------------|
| **Charter/scope**        | R          | A           | C                    | C                 | C                | I                   |
| **Campaign data**        | R          | I           | C                    | A/R               | C                | I                   |
| **Query baskets**        | R          | I           | A                    | I                 | C                | I                   |
| **Geography/controls**   | R          | I           | A                    | C                 | I                | I                   |
| **Model/validation**     | R          | I           | A                    | C                 | C                | I                   |
| **Report narrative**     | R          | A           | C                    | I                 | C                | I                   |
| **Dashboard**            | R          | C           | C                    | I                 | C                | A                   |
| **Client-safe approval** | C          | A           | C                    | I                 | R                | C                   |
| **Final handoff**        | R          | A           | C                    | C                 | C                | R                   |

R = Responsible, A = Accountable, C = Consulted, I = Informed. One person may fill multiple roles, but the methods review should remain separate from the person whose success is measured by producing a positive lift.

# 11.2 Risk register

| **Risk**                             | **Early warning**                                           | **Mitigation**                                                                     | **Residual disclosure**                   |
|--------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------|
| **ZIP-level search unavailable**     | No stable or supported ZIP series.                          | Use supported parent geography; ZIP delivery-only UX.                              | Lift is not ZIP-specific.                 |
| **Sparse branded search**            | Zeros, spikes, unstable repeated pulls.                     | Coarsen geography/time; basket rules; no-go gate.                                  | Relative signal is limited.               |
| **No credible controls**             | All comparable markets received material delivery.          | Alternative campaign, synthetic time series, or descriptive tier.                  | No strong incremental claim.              |
| **Delivery selection bias**          | High-weight markets had stronger pre-demand/objectives.     | Binary primary design, pre-period matching, covariates, conservative dose wording. | Weight association may remain confounded. |
| **Spillover/interference**           | Control geographies receive media or cross-border audience. | Delivery-leakage audit; exclude buffer markets; sensitivity.                       | Estimate may be attenuated.               |
| **Concurrent events**                | Promotion/PR/news aligns with launch.                       | Event calendar, controls, annotations, alternative windows.                        | Cannot fully isolate campaign.            |
| **Google Trends sampling/revisions** | Historical pulls change.                                    | Repeat pulls, median, archive, rerun sensitivity.                                  | Source uncertainty included.              |
| **Few geographies**                  | Unstable standard errors and influence.                     | Matched-market/synthetic approach; leave-one-out; evidence downgrade.              | Limited generalizability.                 |
| **Dashboard overstates precision**   | ZIP click appears to show ZIP lift.                         | Parent-geo labels, evidence flags, no unsupported ranking.                         | Visual is a navigation layer.             |
| **Second report forced**             | Case B fails signal/data gates.                             | Issue documented feasibility memo.                                                 | No unsupported estimate.                  |

# 11.3 Definition of done

- The scope and evidence tier are approved in the decision log.

- Campaign totals reconcile, mapping coverage is documented and source QA passes.

- Query baskets, control set, analysis geography and windows are versioned and frozen.

- The simple four-cell calculation and the regression estimate reconcile within expected rounding/definition differences.

- Event study, placebos, negative controls, sensitivity and influence tests are complete and visible.

- Report and dashboard read from the same canonical model-output table and display the same rounded result.

- Every client-facing chart includes geography, period, metric definition, evidence tier and relevant limitation.

- A clean-environment rerun produces the same model outputs and artifacts.

- A new analyst can execute the runbook and explain the method without relying on the intern’s memory.

- Raw client data, credentials and internal-only intelligence are excluded from public artifacts.

## 11.4 Handoff packet

| **Artifact**                            | **Required status**                                                   |
|-----------------------------------------|-----------------------------------------------------------------------|
| **Methodology guide**                   | Final, versioned, methods-review approved.                            |
| **Client Report A**                     | Final and stakeholder approved.                                       |
| **Client Report B or feasibility memo** | Final and disposition documented.                                     |
| **Dashboard**                           | Internal functional build plus client-safe export/config if approved. |
| **Repository release**                  | Tagged commit with locked environment and tests.                      |
| **Data inventory and manifests**        | Complete source provenance and checksums.                             |
| **QA/validation packet**                | All tests, failures, overrides and evidence tier.                     |
| **Runbook and walkthrough**             | Owner trained; recording/location documented.                         |
| **Future-test memo**                    | Prospective geo holdout recommendation for stronger next measurement. |
