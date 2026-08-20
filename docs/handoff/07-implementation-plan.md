# Phased implementation plan

# 7.1 Board columns

| **Column**                 | **Entry rule**                                                        | **Exit rule**                                  |
|----------------------------|-----------------------------------------------------------------------|------------------------------------------------|
| **Backlog**                | Task is documented but not yet unblocked or prioritized.              | Dependencies and owner are defined.            |
| **Ready**                  | Inputs and acceptance criteria are available.                         | Owner begins work.                             |
| **In Progress**            | Active work is occurring.                                             | Output is complete or blocked.                 |
| **Blocked / Input Needed** | A named dependency prevents progress.                                 | Dependency is resolved and documented.         |
| **Methods Review**         | Calculation, assumptions or QA require reviewer sign-off.             | Reviewer approves or returns specific changes. |
| **Stakeholder Review**     | Business wording, usability or client-safety require review.          | Sponsor/account lead approves.                 |
| **Done**                   | Acceptance criteria, documentation and linked artifacts are complete. | Reopen only through a logged change request.   |

## 7.2 Illustrative ten-week cadence

The following cadence is a sequencing model rather than a fixed promise. Gates should control movement: do not start dashboard polish before the search signal, geography and counterfactual have passed review.

| **Phase**                       | **Indicative timing** | **Gate / milestone**                                                  |
|---------------------------------|-----------------------|-----------------------------------------------------------------------|
| **0. Charter and scope**        | Week 1                | Scope, clients/campaigns, roles, security and evidence goal approved. |
| **1. Feasibility audit**        | Weeks 1-2             | At least one campaign passes the mandatory gates.                     |
| **2. Search measurement**       | Weeks 2-3             | Frozen query baskets and stable retrieval protocol approved.          |
| **3. Geography and controls**   | Weeks 3-4             | Analysis level, crosswalk and comparison set approved.                |
| **4. Data pipeline**            | Weeks 4-5             | Reconciled analysis table and QA report complete.                     |
| **5. Estimation**               | Weeks 5-6             | Primary lift, event study and weight analysis produced.               |
| **6. Validation**               | Weeks 6-7             | Placebos, sensitivity, first-party checks and evidence tier complete. |
| **7. Product outputs**          | Weeks 7-9             | Report A and reusable dashboard reach stakeholder review.             |
| **8. Replication and red team** | Weeks 8-9             | Second case or no-go memo; skeptical review resolved.                 |
| **9. Handoff**                  | Week 10               | Rerun, archive, training and ownership transfer complete.             |

## Phase 0 - Charter, scope and access

| **ID**   | **Task and output**                                                                                            | **Owner**           | **Done when**                         |
|----------|----------------------------------------------------------------------------------------------------------------|---------------------|---------------------------------------|
| **H0.1** | Confirm whether the commitment is one client/1-2 campaigns or two clients; document primary and stretch scope. | Sponsor             | Signed charter and scope boundary.    |
| **H0.2** | Name intern, sponsor, methods reviewer, ad-ops owner, account lead, dashboard owner and security contact.      | Sponsor             | RACI accepted.                        |
| **H0.3** | Define executive question, evidence ceiling and prohibited claims.                                             | Sponsor + reviewer  | One-page measurement brief.           |
| **H0.4** | Approve client aliases, storage, access and client-safe output rules.                                          | Security/data owner | Governance checklist passed.          |
| **H0.5** | Create repository, issue templates, status file and decision log.                                              | Intern              | Project structure merged and visible. |

## Phase 1 - Campaign and data feasibility

| **ID**   | **Task and output**                                                         | **Owner**             | **Done when**                            |
|----------|-----------------------------------------------------------------------------|-----------------------|------------------------------------------|
| **H1.1** | Inventory candidate campaigns and collect delivery/data-owner contacts.     | Intern + account lead | Candidate register complete.             |
| **H1.2** | Profile actual delivery by ZIP/week; reconcile totals and identify leakage. | Intern + ad ops       | Delivery QA packet.                      |
| **H1.3** | Test brand/category terms at candidate geographies and time grains.         | Intern                | Signal table: zeros, variance, coverage. |
| **H1.4** | Build concurrent-events calendar and national-media overlap assessment.     | Account lead          | Known-events log.                        |
| **H1.5** | Apply mandatory gates and select primary/replication candidates.            | Sponsor + reviewer    | Go/no-go decision log.                   |

## Phase 2 - Search measure design

| **ID**   | **Task and output**                                                  | **Owner**             | **Done when**                           |
|----------|----------------------------------------------------------------------|-----------------------|-----------------------------------------|
| **H2.1** | Draft branded, category, negative-control and anchor baskets.        | Intern + account lead | Query registry v0.1.                    |
| **H2.2** | Test term versus topic behavior, ambiguity and regional stability.   | Intern                | Query diagnostic notebook/report.       |
| **H2.3** | Define source settings, repeated-pull count and raw-file naming.     | Intern + reviewer     | Retrieval protocol approved.            |
| **H2.4** | Freeze query registry before viewing final post-period estimates.    | Reviewer              | Versioned approval record.              |
| **H2.5** | Run and archive production pulls; quantify pull-to-pull variability. | Intern                | Raw search archive + variability table. |

## Phase 3 - Geography and comparison design

| **ID**   | **Task and output**                                                 | **Owner**         | **Done when**               |
|----------|---------------------------------------------------------------------|-------------------|-----------------------------|
| **H3.1** | Build ZIP-to-ZCTA/county/CBSA/market bridge with allocation ratios. | Intern            | Geo crosswalk table and QA. |
| **H3.2** | Select smallest stable search-analysis geography.                   | Intern + reviewer | Analysis-level decision.    |
| **H3.3** | Aggregate delivery and universe measures to geo/week.               | Intern            | Exposure table.             |
| **H3.4** | Identify candidate low/no-delivery controls using pre-period only.  | Intern            | Control candidate table.    |
| **H3.5** | Match/select controls; inspect pre-trends and spillover risk.       | Reviewer + intern | Locked comparison set.      |

## Phase 4 - Reproducible pipeline and QA

| **ID**   | **Task and output**                                                            | **Owner** | **Done when**                  |
|----------|--------------------------------------------------------------------------------|-----------|--------------------------------|
| **H4.1** | Implement source ingestion with schemas and type validation.                   | Intern    | Automated raw-to-interim load. |
| **H4.2** | Implement query aggregation and repeated-pull median logic.                    | Intern    | Search measure module + tests. |
| **H4.3** | Implement geography allocation and exposure normalization.                     | Intern    | Geo/exposure module + tests.   |
| **H4.4** | Create one canonical geo-week analysis table.                                  | Intern    | Versioned processed dataset.   |
| **H4.5** | Generate automated QA report: totals, gaps, zeros, outliers, mapping coverage. | Intern    | QA report passes thresholds.   |
| **H4.6** | Have data owner reconcile output to campaign source.                           | Ad ops    | Signed reconciliation.         |

## Phase 5 - Estimation

| **ID**   | **Task and output**                                                    | **Owner**         | **Done when**                |
|----------|------------------------------------------------------------------------|-------------------|------------------------------|
| **H5.1** | Produce descriptive delivery and search plots before modeling.         | Intern            | Exploratory packet.          |
| **H5.2** | Calculate four-cell ratio-of-ratios estimate.                          | Intern            | Audit table and simple lift. |
| **H5.3** | Fit primary DiD with geography/time effects and appropriate inference. | Intern + reviewer | Model output table.          |
| **H5.4** | Fit event study; inspect lead coefficients and post timing.            | Intern + reviewer | Event-study chart.           |
| **H5.5** | Build normalized impression/reach-weight bins and response chart.      | Intern            | Weight-response output.      |
| **H5.6** | Record model formula, package versions and run seed/config.            | Intern            | Run manifest complete.       |

## Phase 6 - Robustness and validation

| **ID**   | **Task and output**                                                     | **Owner**             | **Done when**       |
|----------|-------------------------------------------------------------------------|-----------------------|---------------------|
| **H6.1** | Run placebo launch dates and pre-period pseudo-campaigns.               | Intern                | Placebo table/plot. |
| **H6.2** | Run alternative query baskets, time windows and geography/control sets. | Intern                | Sensitivity matrix. |
| **H6.3** | Run leave-one-geo-out and high-leverage-market diagnostics.             | Intern                | Influence report.   |
| **H6.4** | Test negative-control terms and annotate external events.               | Intern + account lead | Confound review.    |
| **H6.5** | Compare direction/timing with approved first-party outcomes.            | Data owner + intern   | Validation summary. |
| **H6.6** | Assign evidence tier and approve exact client language.                 | Methods reviewer      | Methods sign-off.   |

## Phase 7 - Reports and dashboard

| **ID**   | **Task and output**                                                 | **Owner**             | **Done when**                 |
|----------|---------------------------------------------------------------------|-----------------------|-------------------------------|
| **H7.1** | Create Client Report A from governed model outputs.                 | Intern                | Draft report.                 |
| **H7.2** | Build reusable dashboard data contract and client/campaign configs. | Intern                | Dashboard model.              |
| **H7.3** | Implement executive, delivery, lift, weight and methods/QA views.   | Intern                | Functional dashboard.         |
| **H7.4** | Add parent-geo labels and prevent unsupported ZIP-lift language.    | Intern + reviewer     | Geography UX test passed.     |
| **H7.5** | Create internal and client-safe output modes.                       | Intern + account lead | Client-safety review.         |
| **H7.6** | Reconcile every displayed value to final model-output table.        | Intern + reviewer     | Report/dashboard parity test. |

## Phase 8 - Replication and skeptical review

| **ID**   | **Task and output**                                                              | **Owner**        | **Done when**                      |
|----------|----------------------------------------------------------------------------------|------------------|------------------------------------|
| **H8.1** | Run the frozen pipeline on Case B without changing formulas post hoc.            | Intern           | Replication output or failure log. |
| **H8.2** | Document any required config-only differences.                                   | Intern           | Case B config and comparison.      |
| **H8.3** | Conduct isolated skeptical review across data, design, inference, UX and claims. | Methods reviewer | Red-team issue log.                |
| **H8.4** | Resolve each issue or document accepted residual risk.                           | Sponsor + intern | Disposition table complete.        |
| **H8.5** | Finalize Report B or feasibility memo.                                           | Intern + sponsor | Approved second deliverable.       |

## Phase 9 - Handoff and closeout

| **ID**   | **Task and output**                                            | **Owner**            | **Done when**                |
|----------|----------------------------------------------------------------|----------------------|------------------------------|
| **H9.1** | Execute clean-environment rerun from raw inputs.               | New analyst + intern | Reproducibility test passed. |
| **H9.2** | Archive source inventory, configs, outputs, QA and references. | Intern               | Release package.             |
| **H9.3** | Write operating guide and troubleshooting notes.               | Intern               | Runbook complete.            |
| **H9.4** | Train dashboard/report owner and record walkthrough.           | Intern + owner       | Ownership accepted.          |
| **H9.5** | Document future prospective geo-test design recommendations.   | Reviewer             | Next-test memo.              |
| **H9.6** | Close decision log, known limitations and enhancement backlog. | Sponsor              | Project accepted.            |

## 7.3 Status file template

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>Recommended README/status.md fields</strong></p>
<p>Current phase and gate; percent complete by phase; current evidence tier; latest validated lift (internal only); completed decisions; open blockers; data freshness; next three tasks; risks; links to report, dashboard, QA and run manifest.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
