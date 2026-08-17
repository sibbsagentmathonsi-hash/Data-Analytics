DROP TABLE IF EXISTS ipc_cleaned;
DROP TABLE IF EXISTS ipc_phase_distribution;
DROP TABLE IF EXISTS severe_food_insecurity;
DROP TABLE IF EXISTS ipc_phase_summary;

-- Tables are populated by the Python pipeline from cleaned CSV/DataFrame outputs.
-- The schema below documents the table purpose and key analytical fields.
CREATE TABLE ipc_cleaned (
    ref_area TEXT,
    ref_area_label TEXT,
    indicator TEXT,
    indicator_label TEXT,
    unit_measure TEXT,
    unit_measure_label TEXT,
    unit_type TEXT,
    unit_type_label TEXT,
    comp_breakdown_1_label TEXT,
    comp_breakdown_2 TEXT,
    comp_breakdown_2_label TEXT,
    time_period TEXT,
    obs_value REAL,
    obs_status_label TEXT,
    obs_conf_label TEXT,
    period TEXT,
    year INTEGER,
    month INTEGER,
    phase TEXT,
    metric TEXT
);

CREATE TABLE ipc_phase_distribution (
    ref_area TEXT,
    ref_area_label TEXT,
    indicator TEXT,
    indicator_label TEXT,
    unit_measure TEXT,
    unit_measure_label TEXT,
    unit_type TEXT,
    unit_type_label TEXT,
    comp_breakdown_1_label TEXT,
    comp_breakdown_2 TEXT,
    comp_breakdown_2_label TEXT,
    time_period TEXT,
    obs_value REAL,
    obs_status_label TEXT,
    obs_conf_label TEXT,
    period TEXT,
    year INTEGER,
    month INTEGER,
    phase TEXT,
    metric TEXT,
    phase_order REAL
);

CREATE TABLE severe_food_insecurity (
    ref_area TEXT,
    ref_area_label TEXT,
    indicator TEXT,
    indicator_label TEXT,
    unit_measure TEXT,
    unit_measure_label TEXT,
    unit_type TEXT,
    unit_type_label TEXT,
    time_period INTEGER,
    obs_value REAL,
    obs_status_label TEXT,
    obs_conf_label TEXT,
    year INTEGER,
    year_on_year_change_percentage_points REAL,
    rolling_3_year_average REAL
);

CREATE TABLE ipc_phase_summary (
    phase TEXT,
    phase_order REAL,
    people REAL,
    people_status TEXT,
    percentage REAL,
    percentage_status TEXT,
    reporting_treatment TEXT,
    people_display TEXT,
    percentage_display TEXT
);