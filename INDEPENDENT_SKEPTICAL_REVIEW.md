# Independent Skeptical Review

## Review question

Assume the dashboard looks convincing and the point estimate is positive. What could still make the result wrong, overstated, non-reproducible, or unusable for a client decision?

## Verdict

**Conditionally approved.** The revised design is substantially stronger than a ZIP-level Google Trends before/after dashboard, but the project should not advance from feasibility to client reporting until the additional gates below are resolved.

## Findings retained from the main handoff

| Challenge | Failure mode | Required response |
|---|---|---|
| ZIP click implies ZIP lift | Search data do not support the displayed precision | ZIP shows delivery; lift is labeled at the supported parent geography |
| Targeted ZIPs define exposure | Targeting can differ materially from actual delivery | Use delivered impressions/reach by geography and week |
| Trends index equals volume | Relative, normalized, sampled values are misread as counts | Use relative-search language and preserve raw retrieval settings |
| One retrieval is treated as truth | Repeated samples can change | Archive repeated pulls, aggregate transparently, and report stability |
| Category term is automatically a clean control | Campaign or outside events may affect category demand | Use a governed basket, negative controls, and sensitivity alternatives |
| Before/after proves lift | Seasonality and common shocks can create false lift | Use credible comparison geographies and event-time diagnostics |
| More weight proves more causal response | Budget and expected demand can determine weight | Keep dose response secondary unless stronger identification exists |
| Statistical significance proves business value | Small or fragile effects can be “significant” | Report interval, practical threshold, evidence tier, and sensitivity |

## Additional red-team requirements added during continuation

### 1. Minimum-detectable-effect and precision gate

Before selecting the final case, estimate the amount of lift that the available geographies, pre-period variability, and campaign timing can plausibly detect. A case should be rejected or labeled exploratory when the expected confidence interval is too wide to distinguish a business-relevant effect from noise.

**Required output:** a short MDE/precision simulation or resampling memo using pre-period data only.

### 2. Primary-versus-exploratory specification lock

The primary query basket, outcome, control-selection rule, window, estimator, and exposure definition must be frozen before inspecting the campaign-period result. Alternative queries, windows, models, and subgroups must be labeled sensitivity or exploratory analyses.

**Required output:** dated configuration freeze and decision-log approval.

### 3. Multiplicity and subgroup restraint

A dashboard can invite dozens of geography, channel, creative, audience, and dose comparisons. Some will look positive by chance. The project should either limit confirmatory subgroup tests, use an approved multiplicity procedure, or clearly label them exploratory without isolated significance claims.

**Required output:** approved list of confirmatory comparisons and an exploratory-analysis label rule.

### 4. Practical decision threshold

Define what magnitude of branded-search lift would matter for the client before seeing the result. A narrow estimate below that threshold may be statistically credible but commercially immaterial.

**Required output:** sponsor-approved practical threshold or decision rubric.

### 5. Interference and contamination map

Media exposure, commuting, retail/service areas, search location, and market borders can contaminate low/no-exposure controls. A binary spillover flag is not enough for high-risk cases.

**Required output:** control-leakage table showing adjacent markets, observed delivery leakage, service overlap, and sensitivity exclusions.

### 6. Outcome interpretation audit

Branded search can increase because of curiosity, negative news, paid-search activity, a promotion, or campaign-driven consideration. It is not automatically favorable brand sentiment or revenue.

**Required output:** account-lead interpretation memo and at least one secondary outcome where available.

## Final adversarial signoff questions

- Could another analyst reproduce the exact estimate without asking which export, query, or filter was used?
- Would the conclusion remain materially similar under reasonable query, control, and window alternatives?
- Is the confidence interval narrow enough to answer the business question?
- Is the primary result clearly separated from exploratory slices?
- Could spillover, concurrent promotions, PR, paid search, or pre-existing market momentum explain the result?
- Does every ZIP interaction state that the lift belongs to a parent analysis geography?
- Would the team still publish a null, negative, or not-estimable result using the same rules?

If any answer is no, the evidence tier must be downgraded or the case rejected.
