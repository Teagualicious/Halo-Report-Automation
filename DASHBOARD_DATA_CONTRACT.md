# Dashboard Data Contract

The dashboard is a presentation layer over frozen outputs. It must not calculate a different lift estimate from the report.

## Required tables

### `campaign_geo_week`
One row per client, campaign, analysis geography, and week.

Required fields:

- `run_id`, `client_alias`, `campaign_id`, `analysis_geo_id`, `analysis_geo_name`, `week_start`;
- `treated`, `post`, `event_week`;
- `brand_rsv`, `category_rsv`, `outcome_value`;
- `impressions`, `reach`, `frequency`, `spend`, `impressions_per_1000_households`;
- `query_version`, `geo_mapping_version`, `source_pull_set_id`, `qa_status`.

### `model_summary`
One row per governed model/specification.

- `run_id`, `model_id`, `specification_role`;
- `estimand`, `estimate`, `std_error`, `ci_low`, `ci_high`, `p_value`;
- `evidence_tier`, `claim_text`, `limitation_text`;
- `treated_geo_count`, `control_geo_count`, `pre_weeks`, `post_weeks`;
- `approved_for_client`, `reviewer`, `approval_date`.

### `event_study`

- `run_id`, `model_id`, `event_week`, `estimate`, `ci_low`, `ci_high`, `is_pre_period`.

### `zip_delivery_map`

- `client_alias`, `campaign_id`, `zip_or_zcta`, `analysis_geo_id`;
- `impressions`, `reach`, `frequency`, `spend`, `allocation_factor`, `mapping_quality`.

### `qa_summary`

- `run_id`, `check_id`, `status`, `blocking`, `observed_value`, `threshold`, `evidence_location`.

## Interaction rule

Clicking a ZIP may show ZIP delivery details and highlight its parent analysis geography. The lift KPI must remain labeled with the parent geography; the interface must not imply a ZIP-specific search-lift estimate.

## Dashboard pages

1. Executive summary.
2. Delivery footprint and ZIP explorer.
3. Trend, counterfactual, and event study.
4. Geography and exposure-weight response.
5. Methods, QA, evidence tier, and limitations.

## Parity test

The rounded estimate, interval, evidence tier, period, geography, and limitation text shown in the dashboard must equal the governed report values for the same `run_id` and `model_id`.
