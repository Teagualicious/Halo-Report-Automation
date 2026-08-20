# QA and Release Checklist

## Data and mapping

- [ ] Delivery totals reconcile to the source system.
- [ ] Duplicate client/campaign/geography/week rows are resolved.
- [ ] Mapping coverage and allocation factors meet the approved threshold.
- [ ] Household or universe denominators have a documented source and release date.
- [ ] Control geographies have no material campaign leakage or documented exceptions.

## Search source

- [ ] Exact queries/topics, filters, geography, time zone, and date windows are versioned.
- [ ] Raw retrievals and checksums are archived.
- [ ] Repeated-pull zero rates and variability pass or trigger aggregation/downgrade.
- [ ] Brand/category terms were selected without post-period outcome mining.
- [ ] Ambiguous terms and category contamination are reviewed.

## Design and estimation

- [ ] Treatment is based on actual delivery.
- [ ] Pre-period fit and event-study leads are reviewed visually and quantitatively.
- [ ] Estimator matches the timing structure and number of geographies.
- [ ] Inference accounts for geography clustering and few-cluster limitations.
- [ ] Exposure-weight language matches the identification strength.
- [ ] Pre-period MDE/precision analysis shows the case can answer a business-relevant question.
- [ ] Primary specifications were frozen before post-period inspection.
- [ ] Confirmatory subgroup tests are limited or multiplicity is addressed; other slices are labeled exploratory.

## Robustness

- [ ] In-time placebo complete.
- [ ] In-space/permutation placebo complete where feasible.
- [ ] Alternative query, control, and window specifications complete.
- [ ] Leave-one-geography-out influence complete.
- [ ] Spillover and concurrent-event audit complete.
- [ ] Secondary validation outcome reviewed or documented unavailable.

## Product parity and release

- [ ] Report and dashboard use the same `run_id` and model-output table.
- [ ] Estimate, interval, evidence tier, geography, dates, and limitation text match.
- [ ] Client-safe version removes other-client data, internal notes, credentials, and sensitive paths.
- [ ] A clean environment reproduces the rounded result and charts.
- [ ] Methods reviewer and sponsor signoffs are recorded.
- [ ] Release is tagged and archived with run manifest and decision log.
