-- 1. Severe food insecurity trend by year.
SELECT year, obs_value AS severe_food_insecurity_percent, year_on_year_change_percentage_points
FROM severe_food_insecurity
ORDER BY year;

-- 2. IPC phase distribution ranked by population share.
SELECT phase, people, percentage
FROM ipc_phase_summary
ORDER BY percentage DESC;

-- 3. Crisis-or-worse population count from Phase 3, Phase 4, and Phase 5.
SELECT SUM(people) AS crisis_or_worse_people
FROM ipc_phase_summary
WHERE phase IN ('Phase 3 - Crisis', 'Phase 4 - Emergency', 'Phase 5 - Famine');

-- 4. Safe UPDATE example for a copied/demo table.
CREATE TABLE IF NOT EXISTS severe_food_insecurity_demo AS
SELECT * FROM severe_food_insecurity;
UPDATE severe_food_insecurity_demo
SET obs_status_label = 'Reviewed for project'
WHERE year = 2023;

-- 5. Safe DELETE example targeting invalid records only.
DELETE FROM severe_food_insecurity_demo
WHERE year IS NULL;