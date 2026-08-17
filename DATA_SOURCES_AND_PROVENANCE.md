# Data Sources & Provenance

## Group Members

1. Sibusiso Agent Mathonsi 202331971
2. Kegoikantse Sebetseba 202414220
3. Agcobile Qabo 202469432
4. Lebogang Malatjie 202404978
5. Tlotlo Naledi 202422544
6. Tlotlanang Naledi 202422539

## Purpose and scope

This register documents the local data extracts used in the South Africa food-security analysis. It is intended to make the evidence trail clear for reviewers and stakeholders. The analysis is a country-specific, descriptive analysis of the observations contained in these extracts; it does not establish causation or produce a forecast.

## Source register

| Dataset | Local raw file | Provider and identifier evidenced in the extract | South Africa scope used | Measure and time coverage |
| --- | --- | --- | --- | --- |
| Prevalence of severe food insecurity in the population (%) | `Raw datasets/Prevalence of severe food insecurity in the population (%)/WB_WDI_SN_ITK_SVFI_ZS.csv` | World Bank Data360 / World Development Indicators; database `WB_WDI`; indicator `WB_WDI_SN_ITK_SVFI_ZS` | `REF_AREA = ZAF` (South Africa); six retained annual records | Percentage of population; available years 2018–2023 |
| Integrated Food Security Phase Classification | `Raw datasets/Integrated Food Security Phase Classification/IPC_IPC.csv` | World Bank Data360 / World Bank Open Data; database `IPC_IPC` | `REF_AREA = ZAF` (South Africa); 12 retained records | Persons and percentages by IPC phase; October 2020 snapshot |

## Traceability

- The raw CSV files are retained unchanged in `Raw datasets/`.
- The reproducible transformation entry point is `Python or Excel Data Analysis/food_security_pipeline.py`.
- Country filtering uses `REF_AREA = ZAF` or the matching `REF_AREA_LABEL` value, then creates the cleaned South Africa files in `Data Preparation/`.
- Derived numerical tables, SQLite query exports, Excel output, charts, and the report pack are generated from those filtered records. See `README.md` for the rerun procedure.

## Critical data-quality and interpretation note: IPC Phase 5

For the October 2020 South Africa IPC snapshot, the raw extract records **Phase 5 – Famine as missing** for both the persons and percentage measures (`OBS_STATUS_LABEL = Missing value`). It must not be described as an observed zero or as evidence that no Phase 5 population existed.

The pipeline retains the raw missing values in the cleaned data and labels Phase 5 as **Not reported** in stakeholder-facing outputs. Stakeholder reporting should therefore use the independently supplied `IPC_IPC_P3PLUS` observation for the headline result: **9,335,159 people (16.0% of the classified population) were recorded in Phase 3 or above** in the October 2020 snapshot. Any Phase 3–5 subtotal based on individual phase rows must be labelled as a derived reconciliation over the reported rows, not as a confirmed Phase 5 value.

## Source-link and retrieval limitation

The supplied CSV extracts and project notes identify the provider, database, and indicator codes above, but contain **no source URL, download date, or extraction timestamp**. No URL has been invented in this register. Before external publication, add the exact retrieval URL, download date, and any licence/citation text from the source portal to this file or the final report.
