# Data Validation Rules

## Purpose and scope

Apply these checks on every refresh from the supplied raw files through the South Africa analytical outputs. A failed required check should stop publication and be recorded in the refresh log. Source values remain unchanged; presentation rounding is applied only in stakeholder-facing tables and charts.

| Control | Rule | Expected result for supplied data | Status / action if failed |
| --- | --- | --- | --- |
| Source inventory | Confirm the two expected raw files are present and readable. | `IPC_IPC.csv`: 5,364 rows; `WB_WDI_SN_ITK_SVFI_ZS.csv`: 1,385 rows. | Required — halt the refresh. |
| Country filter | Select `REF_AREA = 'ZAF'`, then assert `REF_AREA_LABEL = 'South Africa'`. Do not rely on a label-only match. | 12 IPC rows and 6 severe-food-insecurity rows. | Required — investigate source or filter logic. |
| IPC period type | Parse IPC `TIME_PERIOD` strictly as `YYYY-MM`; derive a calendar date only after successful parsing. | All 12 rows parse; each is `2020-10` (October 2020 snapshot). | Required — retain invalid records in an exception file; do not coerce silently. |
| Annual period type | Parse severe-food-insecurity `TIME_PERIOD` as an integer year. | Six consecutive years: 2018–2023, with one observation per year. | Required — flag gaps, duplicates, or invalid years. |
| Numeric type and range | Convert normal-status `OBS_VALUE` values explicitly. Persons must be non-negative; percentages must be within 0–100. | No invalid non-missing values. Severe-food-insecurity values are 6.9, 7.5, 8.0, 8.4, 8.4, and 8.5. | Required — quarantine invalid values and report them. |
| Business-key uniqueness | Check IPC uniqueness on `(REF_AREA, INDICATOR, UNIT_MEASURE, COMP_BREAKDOWN_2, TIME_PERIOD)` and annual-series uniqueness on `(REF_AREA, INDICATOR, TIME_PERIOD)`. | No duplicate South Africa records. The phase-distribution output has one row per `(time_period, phase, metric)`. | Required — resolve duplicates before aggregation. |
| Missingness and status | Keep `OBS_VALUE` null when the source marks it missing; preserve the source status in the cleaned data. | Exactly two IPC values are missing: Phase 5 (Famine) persons and percentage, both marked `Missing value`. Severe-food-insecurity has zero missing values. | Required — never substitute zero for an unreported Phase 5 value. Display it as **Not reported** and retain a missingness flag. |
| Unit separation | Aggregate people and percentages separately. Do not calculate a single mean, minimum, or maximum across the mixed IPC units. | Report phase counts and phase shares in separate tables; the existing mixed-unit IPC descriptive mean is not a valid stakeholder metric. | Required for reporting — redesign the summary if units are mixed. |
| Phase-total check | Sum reported IPC phase counts and reported phase shares separately, without treating Phase 5 as zero. | Reported Phase 1–4 counts sum to 59,130,437; reported Phase 1–4 shares sum to 100.0%. These are sums of reported values, not proof that Phase 5 is zero. | Informational — disclose the Phase 5 data limitation. |
| P3+ reconciliation | Compare the direct `IPC_IPC_P3PLUS` measure with the sum of available Phase 3–5 rows, while retaining the direct source value as the authoritative KPI. | Direct P3+ result: 9,335,159 people and 16.0%. Reported Phase 3 + 4 counts also equal 9,335,159; Phase 5 is missing. Dividing this count by the reported Phase 1–4 total gives 15.7874% (15.8%), not 16.0% — a 0.2126 percentage-point difference. | Informational — do not force a reconciliation, impute Phase 5, or describe 16.0% as a ratio recalculated from the reported phase-count total. Label 16.0% as the source-reported P3+ share. |
| Trend calculation | Sort annual observations by year, calculate year-on-year change in percentage points, and round display values only. | 2018–2023 change: +1.6 percentage points (6.9% to 8.5%); arithmetic mean: 7.95%. | Required — label changes as **percentage points**, not percent. |
| Rolling-average rule | A three-year rolling average requires three observations. | Publish rolling averages from 2020 onward; show 2018 and 2019 as `N/A`, or explicitly label an alternative calculation as an “up-to-three-year average.” | Required for stakeholder-facing output. |

## Publication controls

- Use `#,##0` for people, `0.0%`-style display only when the stored value is a proportion, or `0.0"%"` when the stored value is already percentage points (for example, `8.5`). Use `+0.0;−0.0;0.0` with a `pp` suffix for percentage-point changes.
- Store raw numeric precision in the analytical layer, but round exports, database query results, and Excel cells to the stated presentation precision. Do not expose floating-point artifacts such as `0.09999999999999964`.
- Identify the annual 2023 observation as the **latest available supplied source observation**, not as a current-condition estimate.
- Publish the IPC result as a single October 2020 snapshot; do not infer a time trend or causal relationship between the monthly IPC snapshot and the annual severe-food-insecurity series.
- Record the data-provider name, indicator code, source URL, extract date, geography, time coverage, and known limitations alongside each published output.
