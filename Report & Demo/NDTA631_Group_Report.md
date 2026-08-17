# NDTA631 Food Security Data Analysis and Visualisation Report

Topic: South African food security and severe food insecurity

Prepared for: NDTA631 Data Analysis and Visualisation Group Assignment 2026

Group Members:
1. Sibusiso Agent Mathonsi 202331971
2. Kegoikantse Sebetseba 202414220
3. Agcobile Qabo 202469432
4. Lebogang Malatjie 202404978
5. Tlotlo Naledi 202422544
6. Tlotlanang Naledi 202422539

## Executive Summary

This project analyses South African food-security conditions using two World Bank Data360 datasets: the Integrated Food Security Phase Classification (IPC) and the World Development Indicators severe food insecurity prevalence series.

The main finding is that severe food insecurity prevalence rose from 6.9% in 2018 to 8.5% in 2023. The IPC 2020-10 snapshot also shows 9,335,159 people, or 16.0% of the classified population, in Phase 3 or above.

Together, the datasets describe both a multi-year trend and a detailed severity distribution. The trend suggests worsening pressure over time, while the IPC snapshot identifies a substantial Crisis-or-worse population at one point in time.

## Data Sources and Scope

The IPC dataset contains monthly classification records by country, indicator, unit, phase, and time period. For this project it was filtered to South Africa records only.

The severe food insecurity prevalence dataset contains annual World Development Indicators observations. For South Africa, the available records cover 2018 to 2023.

The raw CSV files were preserved unchanged in the Raw datasets folder. All cleaning, transformations, and outputs were written to separate project folders for auditability.

## Data Preparation

Column names were normalised into lowercase snake_case fields. South Africa was selected using REF_AREA = ZAF or REF_AREA_LABEL = South Africa.

Numeric observation values were converted with explicit coercion, time periods were parsed into year/month fields, and IPC phase labels were extracted into readable phase names.

The IPC Phase 5 records contain missing values for both people and percentage. These missing values remain visible in the cleaned file, summary tables, workbook, database, and charts as Not reported.

## Numerical Analysis

The severe food insecurity average across the available period is 7.95%. The minimum is 6.9% and the maximum is 8.5%.

The total change over the observed period is 1.6 percentage points. Year-on-year changes are exported in the Numeric Analysis folder.

The IPC distribution shows Phase 1 and Phase 2 as the largest reported phase groups. Reported Phase 3 and Phase 4 rows sum to 9,335,159 people, while the source-reported Phase 3+ KPI remains 9,335,159 people.

## Database Integration

A SQLite database named food_security.db was generated from the cleaned datasets. It includes tables for cleaned IPC records, IPC phase distribution, severe food insecurity trend data, and summarised IPC phase results.

The database folder includes schema.sql, queries.sql, exported SELECT query results, and safe UPDATE/DELETE examples. The update and delete examples use WHERE clauses and are intended for a copied demo table.

This demonstrates that the cleaned data can be stored, queried, modified safely, and exported for reporting or visualisation.

## Visualisation

The visualisation folder contains a severe food insecurity trend line chart, IPC phase distribution charts by people and percentage, and a combined dashboard.

The charts use clear titles, axis labels, units, value labels, and consistent colours. They are designed for direct use in the final report and class demonstration.

The trend line makes the rise from 2018 to 2023 visible, while the IPC bars show the population scale of each classification phase.

## Conclusion and Recommendations

South Africa's severe food insecurity prevalence increased across the observed WDI series, ending at its highest supplied value in 2023.

Policy and programme discussion should use the source-reported Phase 3+ IPC result as a planning trigger, not as a stand-alone allocation rule.

Recommended next steps are to refresh the source data, add household-level or provincial evidence where available, and document comparability before making operational claims.

## Report Figures

- Visualisation/severe_food_insecurity_trend.png
- Visualisation/ipc_phase_distribution_people.png
- Visualisation/ipc_phase_distribution_percentage.png
- Visualisation/food_security_overview_dashboard.png

## Repository Evidence

- Data Preparation: cleaned CSV files, descriptive statistics, and data quality notes.
- Numeric Analysis: NumPy-driven summary tables and numerical findings.
- Python or Excel Data Analysis: reusable Python pipeline and Excel workbook.
- Database Integration: SQLite database, schema, queries, and exported query results.
- Visualisation: final PNG charts and chart explanations.
