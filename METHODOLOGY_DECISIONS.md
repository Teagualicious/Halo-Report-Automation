# Methodology Decision Record

Complete and approve this document before examining post-campaign outcomes beyond feasibility checks.

## Outcome

- Brand basket ID: OPEN
- Category basket ID: OPEN
- Negative-control basket ID: OPEN
- Primary outcome: `log((brand_rsv + epsilon) / (category_rsv + epsilon))` or approved share-of-search alternative
- Zero/suppression handling: coarsen geography/time or reject; do not silently impute
- Search type/category filter: OPEN

## Unit and timing

- Analysis geography: OPEN
- Time grain: weekly by default
- Pre-period: OPEN
- Campaign period: OPEN
- Carryover period: OPEN
- Event-study reference week: OPEN
- Material-exposure start rule: OPEN

## Treatment and comparison

- Primary treatment definition: actual exposure above approved threshold
- Low/no-exposure definition: OPEN
- Normalized exposure measure: impressions per 1,000 households or approved reach/GRP measure
- Control selection variables: pre-outcome level/trend/volatility, category dynamics, size, region, urbanicity, serviceability
- Spillover exclusion/buffer: OPEN

## Estimator and inference

- Primary estimator branch: OPEN
- Geography and time fixed effects: required where supported
- Staggered adoption handling: cohort-aware estimator if treatment timing varies
- Standard errors: clustered by geography; few-cluster procedure if necessary
- Weight-response treatment: secondary descriptive/associational unless stronger identification is approved

## Validation

- Event-study/pre-trend review
- In-time placebo
- In-space placebo/permutation
- Alternative query baskets
- Alternative control sets
- Alternative pre/carryover windows
- Leave-one-geography-out influence
- Repeated Trends-pull sensitivity
- Spillover and concurrent-event audit
- Secondary first-party outcome comparison

## Claim ceiling

Assign evidence tier before drafting the client conclusion. Statistical significance alone does not determine the tier.
