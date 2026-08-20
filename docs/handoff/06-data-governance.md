# Data requirements, geography, and query governance

# 6.1 Required data inventory

| **Domain**          | **Required fields**                                                                                                | **Preferred grain**        | **Owner / source**                    |
|---------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------|
| **Campaign master** | client_id, campaign_id, channel, objective, start/end, offer, creative version, planned geo, planned budget        | Campaign / tactic          | Account lead + planning               |
| **Delivery**        | date/week, delivered ZIP or geo, impressions, unique reach, frequency, spend, video completes/clicks if relevant   | ZIP x week x channel       | Ad operations / platform export       |
| **Search**          | query basket id, term/topic identifiers, geography, date, relative interest, search type, category filter, pull id | Analysis geo x week x pull | Google Trends export/API              |
| **Geography**       | ZIP, ZCTA, city, county, CBSA/metro, market, state, residential/business/total allocation ratios                   | ZIP-to-parent bridge       | HUD-USPS/Census + internal market map |
| **Universe**        | population, households, targetable households or relevant audience universe                                        | Analysis geo               | Approved public/internal source       |
| **Events**          | promotions, PR, national media, sponsorships, openings, outages, competitor events, holidays                       | Date x geography           | Client/account/research               |
| **Validation**      | Search Console branded clicks/impressions, direct/organic sessions, store locator, calls, leads or sales           | Best available geo x week  | Client-approved first-party source    |

## 6.2 Delivery reconciliation checks

- Sum ZIP/week delivery and reconcile to the official campaign total; document tolerated rounding only.

- Separate targeted geography from delivered geography and identify delivery outside the intended area.

- Check duplicate rows, missing weeks, negative values, impossible frequency and reach greater than the selected universe.

- Confirm whether geolocation reflects user presence, presence-or-interest, device location, billing location or another platform definition.

- Aggregate channels only after preserving channel-specific fields; channel mix can change the halo timing and exposure-response relationship.

# 6.3 ZIP and ZCTA mapping rule

USPS ZIP Codes are delivery-route constructs, while Census ZIP Code Tabulation Areas are generalized polygons created for statistics and mapping. Not every ZIP has a corresponding ZCTA, and ZCTA polygons should not be presented as official ZIP delivery boundaries \[6\]. Use HUD-USPS crosswalk allocations to bridge ZIPs to Census geographies such as counties and CBSAs; those files are designed for allocation and are updated regularly \[7\].

| **Use case**                        | **Recommended allocation weight**                           |
|-------------------------------------|-------------------------------------------------------------|
| **Consumer / household advertiser** | Residential address ratio.                                  |
| **Business-to-business advertiser** | Business address ratio.                                     |
| **Mixed audience or unknown**       | Total address ratio, with residential/business sensitivity. |
| **Map display only**                | Current Census ZCTA polygon, labeled as an approximation.   |

## 6.4 Exposure aggregation

For a ZIP that maps to more than one parent market, allocate delivery using the selected crosswalk ratio, then sum to analysis geography and week. Preserve the unallocated and multi-parent share as QA fields. The final report should show the percentage of campaign delivery that maps cleanly to the selected analysis geography.

## 6.5 Query registry schema

| **Field**                  | **Description**                                                            |
|----------------------------|----------------------------------------------------------------------------|
| **query_basket_id**        | Stable ID such as BRAND_A_V1 or CATEGORY_A_V1.                             |
| **role**                   | brand, category, negative control, or anchor.                              |
| **query_type**             | search term, exact phrase, grouped term, or Google topic.                  |
| **query_text_or_topic_id** | Exact value used in the source interface/API.                              |
| **language / country**     | Locale settings.                                                           |
| **search_type**            | Web Search primary; optional YouTube, News, Image or Shopping sensitivity. |
| **category_filter**        | Google Trends category selection, if used.                                 |
| **valid_from / valid_to**  | Version window; prevents silent post-hoc query changes.                    |
| **approval**               | Analyst, sponsor and methods-review status.                                |
| **rationale / exclusions** | Why the term is included and known ambiguity risks.                        |

## 6.6 Google Ads Keyword Planner as supplementary validation

Google Ads historical metrics can return approximate monthly searches for specified keywords and geo targets \[5\]. Google Ads supports location targeting by targetable postal regions where available \[16\]. This can be useful to test whether a brand term has meaningful monthly volume in candidate ZIPs or to validate direction at a coarser interval. It should not replace the primary weekly Trends design because the metric, update cadence and scaling differ.

## 6.7 Data-governance requirements

- Keep raw client campaign data in an approved restricted location; never place it in a public Git repository.

- Use client aliases and configuration IDs in code, screenshots and test fixtures.

- Exclude API credentials, account IDs and personally identifiable data from source control.

- Create an immutable raw-data folder; cleaning produces new interim and processed files rather than overwriting sources.

- Record checksums, row counts, retrieval timestamps and transformation version in the run manifest.

- Separate internal and client-safe dashboard/report configurations.
