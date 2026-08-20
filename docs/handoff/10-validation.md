# Validation, inference, and evidence tiers

# 10.1 Validation matrix

| **Test**                        | **Question answered**                                            | **Pass indicator**                                                                     | **Failure response**                                  |
|---------------------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Delivery reconciliation**     | Did the analysis use the full and correct campaign delivery?     | Geo/week total matches official source within documented rounding.                     | Block modeling and resolve source discrepancy.        |
| **Signal stability**            | Is the search series reproducible enough?                        | Low zero rate; repeated-pull median stable; no unexplained one-off spikes.             | Coarsen, revise preapproved basket, or no-go.         |
| **Pre-trends/event study**      | Were treated and control markets moving similarly before launch? | Lead pattern visually and substantively consistent with parallel movement.             | Change controls/design or lower evidence tier.        |
| **Placebo dates**               | Would the method find lift before the campaign?                  | Pseudo-campaign estimates cluster around no effect.                                    | Investigate seasonality/model misspecification.       |
| **Negative-control terms**      | Did unrelated search also move?                                  | No campaign-timed effect on controls.                                                  | Investigate common shock or source artifact.          |
| **Alternative baskets/windows** | Does the result depend on one arbitrary choice?                  | Direction and magnitude broadly stable across prespecified variants.                   | Report range or lower evidence tier.                  |
| **Leave-one-geo-out**           | Is one market driving the conclusion?                            | Result survives removal of influential geographies.                                    | Report concentration and avoid pooled generalization. |
| **First-party triangulation**   | Does another outcome move in compatible timing/direction?        | Consistent direction with branded site behavior, calls/leads or other approved metric. | Explain divergence; do not hide it.                   |

## 10.2 Pre-trend review rule

Do not rely only on a “non-significant” pre-trend test. With few geographies or noisy data, a test can lack power. Review the event-study graph, magnitude of leads, treated-control fit, sensitivity to control selection and the amount of pre-period data. Modern marketing quasi-experiment guidance emphasizes clearly communicating the identifying assumptions behind causal claims \[15\].

## 10.3 Inference by design

| **Design situation**                                      | **Preferred path**                                                       | **Inference note**                                                                             |
|-----------------------------------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Many treated and comparison geographies**               | Modern panel DiD/event study.                                            | Cluster at the treatment-assignment geography; consider small-cluster corrections when needed. |
| **One or a few treated geographies with long pre-period** | Matched-market TBR or synthetic control/Bayesian structural time series. | Use placebo/permutation or posterior intervals; inspect pre-fit.                               |
| **Staggered launch across geographies**                   | Group-time DiD/event study.                                              | Avoid a naive two-way fixed-effects summary when effects/timing differ \[8\].                  |
| **Only continuous exposure and everyone treated**         | Continuous-dose design or descriptive association.                       | Dose comparisons require stronger assumptions; use conservative language \[9\].                |
| **No credible control and short pre-period**              | Descriptive report only.                                                 | No incremental causal lift claim.                                                              |

## 10.4 Evidence tiers

| **Tier**                              | **Required evidence**                                                                                                                            | **Claim ceiling**                                                                |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **1. Strong quasi-experimental**      | Stable source; credible exposure contrast; good pre-fit; event study, placebo, sensitivity and influence checks pass; major confounds addressed. | Estimated incremental branded-search lift for the analyzed campaign/geographies. |
| **2. Directional quasi-experimental** | Core design works but one or more limitations remain, such as few geographies, moderate pre-fit or incomplete confound/validation coverage.      | Directional estimated lift associated with campaign exposure.                    |
| **3. Descriptive**                    | No credible counterfactual, sparse signal, universal treatment or substantial unresolved confounding.                                            | Observed search change relative to a benchmark; no causal claim.                 |
| **4. Insufficient evidence**          | Search signal, delivery, mapping or source QA fails.                                                                                             | No lift estimate; issue a feasibility memo.                                      |

## 10.5 Required sensitivity summary in each report

| **Variant**                      | **Estimate**  | **Interval / uncertainty** | **Direction retained?** | **Notes**                      |
|----------------------------------|---------------|----------------------------|-------------------------|--------------------------------|
| **Primary specification**        | \[generated\] | \[generated\]              | \[generated\]           | Approved query/control/window. |
| **Alternative category basket**  | \[generated\] | \[generated\]              | \[generated\]           | Tests control definition.      |
| **Alternative control set**      | \[generated\] | \[generated\]              | \[generated\]           | Tests matching dependence.     |
| **Alternative carryover window** | \[generated\] | \[generated\]              | \[generated\]           | Tests lag assumption.          |
| **Repeated Trends pull set**     | \[generated\] | \[generated\]              | \[generated\]           | Tests source variability.      |
