# Assignment interpretation

# 1.1 Business question

The project asks whether campaign exposure generated incremental branded-search interest beyond what would have happened because of normal category demand, seasonality and market-level differences. The output must be understandable to an executive, reproducible by an analyst and appropriately cautious about causal attribution.

## 1.2 Three analytical questions

| **Question**               | **Operational definition**                                                                                                     | **Primary output**                                  |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **Q1. Was there lift?**    | Did the brand/category search index rise more in exposed geographies after launch than in matched low/no-exposure geographies? | Estimated lift percentage and uncertainty interval. |
| **Q2. When did it occur?** | Did the difference appear after launch, persist during the flight and decay or remain after the flight?                        | Event-study / weekly lift chart.                    |
| **Q3. Did weight matter?** | Was larger normalized reach or impression weight associated with larger estimated response?                                    | Binned exposure-response chart with causal caveat.  |

## 1.3 Scope discrepancy that must be resolved

The assignment specifies “1-2 campaigns for a high-tier client,” while the proposed deliverables describe reports for two large clients. Those are not identical scopes. The recommended baseline is one high-tier client with one primary campaign and one replication campaign. A second client becomes a stretch case only after the primary case clears feasibility and the shared pipeline works.

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 98%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p><strong>Why this matters</strong></p>
<p>Two polished reports are not a success if one is based on unstable search signal or an invalid counterfactual. A documented no-go decision is more credible than a forced lift number.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 1.4 Definition of project success

- A nontechnical stakeholder can explain the estimate in one sentence and trace it to a chart.

- An analyst can reproduce the exact estimate from governed inputs without manual spreadsheet editing.

- The method distinguishes target geography, actual delivery geography and analysis geography.

- The report shows the point estimate, uncertainty, pre-trend evidence, sensitivity results and evidence tier.

- The dashboard never implies precision below the level supported by the search data.

- The second case either replicates the method or clearly documents why it failed the feasibility gate.
