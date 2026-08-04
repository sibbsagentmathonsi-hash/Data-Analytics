# NDTA631 Food Security Data Analysis and Visualisation Report

Topic: South African food security and severe food insecurity

Prepared for: NDTA631 Data Analysis and Visualisation Group Assignment 2026

Note: Add group member names and student numbers before final submission.

## Executive Summary

This project analyses South African food-security conditions using two World Bank Data360 datasets: the Integrated Food Security Phase Classification (IPC) and the World Development Indicators severe food insecurity prevalence series.

The main finding is that severe food insecurity prevalence rose from 6.9% in 2018 to 8.5% in 2023. The IPC 2020-10 snapshot also shows 9,335,159 people, or 16.0% of the classified population, in Phase 3 or above.

Together, the datasets describe both a multi-year trend and a detailed severity distribution. The trend suggests worsening pressure over time, while the IPC snapshot clarifies how many people fall into each food insecurity phase.

## Data Sources and Scope

The IPC dataset contains monthly classification records by country, indicator, unit, phase, and time period. For this project it was filtered to South Africa records only.

The severe food insecurity prevalence dataset contains annual World Development Indicators observations. For South Africa, the available records cover 2018 to 2023.

The raw CSV files were preserved unchanged in the Raw datasets folder. All cleaning, transformations, and outputs were written to separate project folders for auditability.

## Data Preparation

Column names were normalised into lowercase snake_case fields. South Africa was selected using REF_AREA = ZAF or REF_AREA_LABEL = South Africa.

Numeric observation values were converted with explicit coercion, time periods were parsed into year/month fields, and IPC phase labels were extracted into readable phase names.

The IPC Phase 5 records contain missing values for both people and percentage. These missing values remain visible in the cleaned file, while numeric summaries use a filled value of zero only where totals require arithmetic.

## Numerical Analysis

The severe food insecurity average across the available period is 7.95%. The minimum is 6.9% and the maximum is 8.5%.

The total change over the observed period is 1.6 percentage points. Year-on-year changes are exported in the Numeric Analysis folder.

The IPC distribution shows Phase 1 and Phase 2 as the largest groups, but Phase 3 and Phase 4 still account for 9,335,159 people in crisis-or-worse conditions.

## Database Integration

A SQLite database named food_security.db was generated from the cleaned datasets. It includes tables for cleaned IPC records, IPC phase distribution, severe food insecurity trend data, and summarised IPC phase results.

The database folder includes schema.sql, queries.sql, exported SELECT query results, and safe UPDATE/DELETE examples. The update and delete examples use WHERE clauses and are intended for a copied demo table.

This demonstrates that the cleaned data can be stored, queried, modified safely, and exported for reporting or visualisation.

## Visualisation

The visualisation folder contains a severe food insecurity trend line chart, IPC phase distribution charts by people and percentage, and a combined dashboard.

The charts use clear titles, axis labels, units, value labels, and consistent colours. They are designed for direct use in the final report and class demonstration.

The trend line makes the rise from 2018 to 2023 visible, while the IPC bars show the population scale of each classification phase.

## Conclusion and Recommendations

South Africa's severe food insecurity prevalence increased across the observed WDI series, ending at its highest available value in 2023.

Policy and programme discussion should focus on the Phase 3 and Phase 4 population groups because they represent people already experiencing crisis or emergency conditions in the IPC framework.

Recommended next steps are to add household-level or provincial data if available, compare South Africa against regional benchmarks, and update the analysis when newer WDI or IPC observations become available.

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