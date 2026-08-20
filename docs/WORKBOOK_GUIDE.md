# Halo Kickoff and Data Intake Workbook Guide

The workbook is the operational companion to the methodology. Its exact `.xlsx` version is retained in the designated project backup folder and verified by the checksum in `ARTIFACTS.md`.

## Worksheets

1. **Instructions** — operating order and interpretation guardrails.
2. **Lift Calculator** — transparent ratio-of-ratios and additive share-of-search DiD audit calculations. It is an explanation and reconciliation tool, not the production estimator.
3. **Campaign Screening** — weighted candidate scorecard plus mandatory pass/fail gates.
4. **Data Request** — source fields, owners, status, receipt dates, and storage locations.
5. **Query Registry** — exact brand, category, negative-control, and anchor-query governance.
6. **Event Calendar** — promotions, PR, paid search, SEO, competitor activity, weather, and other possible confounders.
7. **Decision Log** — scope, geography, treatment, estimator, exceptions, and approvals.
8. **QA Gates** — blocking measurement and release requirements.
9. **Project Plan** — tasks from Phase 0 through reproduction and handoff.

## Required use sequence

1. Complete the charter, role, access, security, and dashboard-environment decisions.
2. Enter two to four candidate campaigns and apply mandatory gates before using the weighted score.
3. Track required delivery, geography, search, event, validation, and governance inputs.
4. Freeze the query baskets and primary specification before reviewing campaign-period outcomes.
5. Reconcile the simple lift calculator to the governed production output.
6. Do not release a client result while any blocking QA gate is unresolved.

## Formula definitions

Multiplicative lift:

```text
[(treated post brand/category) / (treated pre brand/category)]
---------------------------------------------------------------- - 1
[(control post brand/category) / (control pre brand/category)]
```

Additive share-of-search DiD:

```text
[treated post share - treated pre share]
- [control post share - control pre share]
```

The illustrative workbook inputs produce a multiplicative lift of 27.27% and an additive share-of-search DiD of approximately 5.69 percentage points. These are examples only.
