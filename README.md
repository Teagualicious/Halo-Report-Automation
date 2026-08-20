# Halo Brand-Lift Measurement Project

This repository scaffold converts the approved handoff into an executable project. The goal is to estimate whether campaign-exposed geographies experienced incremental branded-search interest relative to category demand and comparable low/no-exposure geographies, then evaluate whether response was associated with normalized impression weight.

## Non-negotiable measurement rules

1. ZIPs are the campaign-delivery and map layer. Search lift is estimated only at the smallest supported, stable analysis geography.
2. Treatment is based on actual delivered exposure, not only targeted ZIPs.
3. Google Trends values are relative search-interest indices, not absolute search counts, clicks, sales, or proof of an organic click.
4. The primary estimate is a treated-versus-comparison, post-versus-pre difference-in-differences result with category controls.
5. Impression-weight response is secondary and should be described as an association unless allocation supports causal identification.
6. A documented “not reliably estimable” conclusion is an acceptable project outcome.

## Start here

1. Review the complete source-controlled handoff at `docs/handoff/README.md`.
2. Download and complete `Halo_Kickoff_and_Data_Intake.xlsx` from the designated project backup folder with the sponsor, methods reviewer, ad-operations owner, and account lead. See `docs/WORKBOOK_GUIDE.md`.
3. Resolve all items marked `OPEN` in `STATUS.md` and `DECISION_LOG.csv`.
4. Copy `config/campaign_template.yaml` to a campaign-specific file and replace every placeholder.
5. Place immutable source extracts in `data/raw/`; never edit them in place.
6. Run the test suite before adding client data:

```bash
python -m pip install -r environment/requirements.txt
pytest -q
```

7. Complete Phase 1 feasibility screening before building a dashboard or client narrative.

## Repository layout

```text
config/                 Versioned campaign, query, geography, and model choices
data/raw/               Immutable source files
  /interim/             Reconciled and mapped intermediate data
  /processed/           Canonical analysis tables
  /external/            Public crosswalks and market denominators
docs/                   Handoff, methods, decisions, and templates
outputs/reports/        Client/internal report exports
outputs/dashboard/      Dashboard-ready datasets and builds
outputs/figures/        Governed charts
outputs/tables/         Governed model and QA tables
outputs/qa/             Validation reports and run manifests
src/halo/               Tested calculation and QA code
tests/                  Unit and acceptance tests
environment/            Reproducible dependency specification
```

## Core governed outputs

The report and dashboard must read from the same canonical model-output table. At minimum it should contain:

- client and campaign aliases;
- analysis geography and period;
- outcome/query-basket version;
- treatment and comparison definitions;
- point estimate and uncertainty interval;
- event-time estimates;
- normalized exposure metrics;
- evidence tier;
- QA status and limitation text;
- run ID and Git commit.

## Definition of ready for modeling

A campaign is ready only when delivery reconciles, search signal is stable enough, analysis geography is supported, a credible comparison exists, query baskets are frozen using pre-period information, concurrent events are documented, and the methods reviewer approves the design branch.

## Office deliverables and backup

The exact DOCX, XLSX, and complete ZIP snapshot are retained in the designated Google Drive backup folder. See `ARTIFACTS.md` for governed file names, checksums, and repository-native equivalents.
