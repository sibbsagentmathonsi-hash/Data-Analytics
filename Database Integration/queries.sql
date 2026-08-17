-- 1. Severe food insecurity trend by year.
SELECT year, obs_value AS severe_food_insecurity_percent, year_on_year_change_percentage_points
FROM severe_food_insecurity
ORDER BY year;

-- 2. IPC phase distribution in phase order, with missing Phase 5 preserved.
SELECT phase, people, percentage, reporting_treatment
FROM ipc_phase_summary
ORDER BY phase_order;

-- 3. Source-reported Phase 3+ KPI for Crisis or worse.
SELECT
    MAX(CASE WHEN metric = 'people' THEN obs_value END) AS source_reported_p3plus_people,
    MAX(CASE WHEN metric = 'percentage' THEN obs_value END) AS source_reported_p3plus_percentage
FROM ipc_cleaned
WHERE indicator = 'IPC_IPC_P3PLUS';

-- 4. Phase-row reconciliation. SUM ignores the missing Phase 5 value; this is not a Phase 5 zero estimate.
SELECT
    SUM(people) AS reported_phase_3_4_people,
    SUM(percentage) AS reported_phase_3_4_percentage,
    SUM(CASE WHEN people IS NULL OR percentage IS NULL THEN 1 ELSE 0 END) AS missing_phase_rows
FROM ipc_phase_summary
WHERE phase IN ('Phase 3 - Crisis', 'Phase 4 - Emergency', 'Phase 5 - Famine');

-- 5. Safe UPDATE example for a copied/demo table.
CREATE TABLE IF NOT EXISTS severe_food_insecurity_demo AS
SELECT * FROM severe_food_insecurity;
UPDATE severe_food_insecurity_demo
SET obs_status_label = 'Reviewed for project'
WHERE year = 2023;

-- 6. Safe DELETE example targeting invalid records only.
DELETE FROM severe_food_insecurity_demo
WHERE year IS NULL;