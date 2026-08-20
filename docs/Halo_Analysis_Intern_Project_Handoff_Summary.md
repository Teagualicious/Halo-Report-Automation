# Halo Analysis Intern Project Handoff

**Prepared:** August 20, 2026  
**Status:** Build-ready proposal; client and data feasibility gates still required

## TL;DR

The project should test whether campaign-exposed markets experienced more branded Google search interest than expected after accounting for category demand and comparable unexposed markets. Keep campaign delivery at ZIP level, but estimate search lift only at a supported and reliable Google Trends geography. Build two client reports, one reusable dashboard with a client selector, a shared methods/validation pack, and a reproducible analysis repository.

The primary outcome should be weekly **brand share of search**:

`Brand RSV / (Brand RSV + approved category-control RSV values)`

The primary estimate should be a matched-market difference-in-differences effect with an event-study chart and uncertainty interval. Impression-weight response should be labeled an association unless exposure intensity was randomized or otherwise exogenous. A credible “not reliably estimable” result must be allowed.

## Core corrections to the original idea

1. Google Trends does not provide a supported, reliable ZIP-level time series for this use. ZIPs should remain the media-delivery layer; lift should be estimated at a city/metro/DMA-equivalent/state geography that passes volume and stability checks.
2. Google Trends is sampled, normalized, and relative. It does not provide absolute search counts or organic-click counts.
3. Repeated pulls can differ. Archive multiple extractions, use a median series, and enforce stability gates.
4. A difference-in-differences estimate requires comparable unexposed geographies, pre-period matching, spillover checks, clustered/few-geo inference, event-study diagnostics, placebos, and sensitivity tests.
5. Realized impression weight is usually endogenous. Use impressions per 1,000 households, reach, frequency, and pre-defined dose tiers, but use causal dose language only when assignment supports it.

## Recommended deliverables

- **Client Report A** and **Client Report B:** executive result, campaign map, observed-versus-counterfactual lift chart, geography results, dose-response, methods, validation, caveats, and business implications.
- **One reusable dashboard:** client selector; ZIP delivery map; parent-market lift; trend/counterfactual; geography explorer; dose-response; methods and QA.
- **Methods and validation package:** frozen queries, controls, formulas, assumptions, repeated-pull reliability, placebos, sensitivity tests, data lineage, and limitations.
- **Reproducible analysis package:** config-driven code, data schemas, tests, environment lock, output manifest, README, status file, and model card.

## Recommended methodology

### Outcome

Retrieve the approved brand and category-control terms together and calculate weekly brand share of search. Report lift in percentage points and relative percent. Do not translate the index into absolute search counts unless an independent calibration source is available.

### Difference-in-differences

`Lift_pp = (Treated post − Treated pre) − (Control post − Control pre)`

Use geography and week fixed effects, weekly data, and standard errors clustered by geography. If geographies start at different times, use a cohort-aware DiD estimator. If geo counts are small, add wild-cluster bootstrap or permutation/placebo inference.

### Control selection

Choose controls using pre-period data only. Match on search level, trend, volatility, seasonality, category behavior, population/households, region, urbanicity, and client service availability. Exclude geographies with likely campaign spillover.

### Google Trends reliability

Use at least five replicated pulls for the pilot and increase to ten or aggregate when instability is high. Archive exact URLs/requests, timestamps, CSVs, and hashes. Measure zero rates, replicate correlation, and CV/IQR. Reject or aggregate sparse/unstable geographies.

### Impression weight

Use impressions per 1,000 households and, when available, reach, frequency, and GRPs. Show pre-defined low/medium/high tiers and a continuous log-dose association. Unless weight was randomized/exogenous, say “associated with,” not “caused.”

## Phases

0. Kickoff, governance, repository, data request, and evidence-grade approval.
1. Screen two to four candidate campaigns and select one or two based on query volume, geography, control quality, timing, confounding, delivery completeness, and validation data.
2. Freeze the query basket, treatment, controls, windows, estimand, dose metric, inference, and sensitivity plan.
3. Ingest and reconcile delivery; map ZIPs to supported search geographies and denominators.
4. Collect replicated Google Trends data and produce a reliability report.
5. Build the weekly panel; match controls; estimate DiD/event-study and dose association.
6. Run placebos, alternate windows/queries/controls, leave-one-geo-out, spillover checks, and confounder audit. Assign evidence grade.
7. Build two reports and one client-switching dashboard from frozen outputs.
8. Run clean reproduction, finalize documentation, present, and create a prospective randomized geo-holdout blueprint.

## Hard veto conditions

- No supported geography with stable nonzero brand/category data.
- No clean control/counterfactual.
- Delivery cannot be reconciled or mapped.
- A dominant coincident event cannot be separated.
- Reasonable specifications reverse the result without explanation.
- Confidence interval is too wide for the intended conclusion.
- Stakeholders require ZIP-level causal lift or absolute search counts from Trends.

## Immediate inputs needed

- Two to four candidate campaigns.
- ZIP-week delivery, impressions, reach/frequency, planned weight, tactics, and flight dates.
- Brand and category term candidates.
- Promotions, PR, paid search, SEO, and other-media calendar.
- Preferred internal geography/crosswalk.
- Secondary validation metric.
- Dashboard destination/security environment.
- Named statistical reviewer.

## Definition of done

The primary result is reproducible and includes lift, uncertainty, evidence grade, assumptions, and analysis geography—or an explicit “not estimable” conclusion. Two reports and one dashboard use the same frozen outputs and never claim ZIP-level or absolute-search lift. Placebos, sensitivity, influence, spillover, and confounder checks are complete. The query registry, data dictionary, model card, environment, README, status file, and handoff walkthrough are complete.

## References

See `docs/handoff/appendix-b-schemas-checks.md` for the full selected research and official documentation list, including Google Trends documentation, geo-experiment research, DiD inference, and Google Trends reliability literature.
