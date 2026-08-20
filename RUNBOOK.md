# Analyst Runbook

## 1. Initialize

- Confirm all owners and scope in `PROJECT_CHARTER.md`.
- Complete the intake workbook.
- Assign decision IDs for all departures from the handoff defaults.
- Create a campaign configuration from `config/campaign_template.yaml`.

## 2. Ingest and reconcile delivery

- Copy source files into `data/raw/` without editing.
- Record file hashes and row counts.
- Reconcile campaign totals by client, campaign, week, tactic, and geography.
- Resolve or document unmatched/duplicate rows.
- Normalize exposure by households or approved targetable universe.

## 3. Map geography

- Store the crosswalk release in `data/external/`.
- Allocate delivery using documented weights.
- Calculate mapping coverage and flags.
- Mark spillover/control contamination risks.

## 4. Freeze search design

- Register exact brand, category, and negative-control baskets.
- Use only pre-period information for control and query selection.
- Record source settings and retrieve repeated pulls.
- Produce zero-rate, correlation, and variability QA.

## 5. Build panel and estimate

- Create one row per analysis geography and week.
- Reconcile the simple lift calculator to the production model definition.
- Estimate the approved DiD/event-study branch.
- Estimate normalized weight response as secondary analysis.

## 6. Validate

Run all blocking QA checks, placebos, alternate queries/controls/windows, leave-one-out influence, spillover checks, event audit, and secondary-outcome comparison. Assign evidence tier before writing the executive conclusion.

## 7. Publish

- Freeze governed model outputs.
- Build report and dashboard from the same `run_id`.
- Run parity, security, and clean-environment reproduction checks.
- Obtain methods reviewer and sponsor approvals.
- Tag and archive the release.
