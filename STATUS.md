# Halo Project Status

**Overall status:** Phase 0 repository and backup setup complete; sponsor and data-feasibility decisions remain open  
**Last updated:** 2026-08-20  
**Current gate:** Approve scope, assign owners, and complete candidate-campaign/data inventory


## Completed foundation

- [x] Repository scaffold established on `main` through a reviewed pull request.
- [x] Full handoff converted to source-controlled Markdown under `docs/handoff/`.
- [x] Calculation and QA package added with six passing tests.
- [x] GitHub Actions validation workflow added for Python 3.11 and 3.12.
- [x] Exact DOCX, XLSX, and complete ZIP snapshot backed up to the designated Google Drive folder.
- [x] Office artifact checksums and a verification script recorded in `ARTIFACTS.md`.

## Phase status

| Phase | Name | Status | Exit requirement |
|---|---|---|---|
| 0 | Charter, scope, access, and governance | In progress | Sponsor decisions recorded; owners named; repository and security rules approved |
| 1 | Candidate campaign and data feasibility | Not started | One primary and one backup/replication case selected or explicitly rejected |
| 2 | Search measurement design freeze | Not started | Query baskets, outcome, windows, analysis geography, control rules, and estimand approved |
| 3 | Delivery ingestion and geography mapping | Not started | Source totals reconcile and mapping coverage passes |
| 4 | Search-data retrieval and reliability QA | Not started | Repeated-pull stability and signal gates pass |
| 5 | Panel construction and estimation | Not started | Primary DiD/event-study and weight association run reproducibly |
| 6 | Validation and evidence grading | Not started | Placebos, sensitivities, influence, spillover, and confounder checks complete |
| 7 | Report and dashboard build | Not started | Both products read the same frozen model-output table |
| 8 | Replication or feasibility memo | Not started | Second case either passes the full pipeline or receives a documented no-go disposition |
| 9 | Reproduction, release, and handoff | Not started | Clean rerun, approvals, tagged release, and walkthrough complete |

## Immediate open decisions

- [ ] Confirm whether scope is one client with one to two campaigns or two separate clients.
- [ ] Name the sponsor, methods reviewer, ad-operations/data owner, account lead, and dashboard owner.
- [ ] Identify two to four candidate campaigns for screening.
- [ ] Confirm availability of ZIP-by-week actual impressions, reach, frequency, spend, tactics, and flight dates.
- [ ] Confirm approved Google Trends retrieval route and whether alpha API access is available.
- [ ] Select a secondary validation metric, if available.
- [ ] Select the approved dashboard environment and client-sharing/security model.
- [ ] Confirm the preferred ZIP/ZCTA-to-market crosswalk and household denominator.
- [ ] Define a business-relevant lift threshold and run a pre-period MDE/precision check.
- [ ] Approve the primary-versus-exploratory analysis list and subgroup multiplicity rule.

## Current blockers

| ID | Blocker | Owner | Resolution needed |
|---|---|---|---|
| B-01 | Candidate campaigns not supplied | Sponsor | Provide two to four candidates and basic flight/delivery metadata |
| B-02 | Actual delivery schema not confirmed | Ad ops/data owner | Provide field inventory and sample extract |
| B-03 | Search access route not confirmed | Sponsor/methods reviewer | Approve manual export, alpha API, or licensed source |
| B-04 | First-party validation outcome unknown | Account lead/data owner | Confirm Search Console, analytics, lead, call, or site outcome availability |

## Next status update

Update this file after the kickoff meeting and again after every gate decision. Do not mark a phase complete merely because code or a dashboard exists; use the exit requirement above.
