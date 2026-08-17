# NDTA631 Data Analysis and Visualisation

Professional, reproducible analysis of South African food-security indicators for the NDTA631 2026 group assignment. The project combines an annual severe-food-insecurity series with an October 2020 Integrated Food Security Phase Classification (IPC) snapshot to communicate the available evidence clearly and responsibly.

## Group Members

1. Sibusiso Agent Mathonsi
2. Kegoikantse Sebetseba
3. Agcobile Qabo
4. Lebogang Malatjie
5. Tlotlo Naledi
6. Tlotlanang Naledi

## Stakeholder-ready deliverables

| Deliverable | Location | Use |
| --- | --- | --- |
| Analysis workbook | `Python or Excel Data Analysis/food_security_analysis_workbook.xlsx` | Excel-based review of the Summary, SVFI Trend, and IPC Phase Snapshot tables and charts |
| Final charts | `Visualisation/` | Presentation-ready PNG exports, including the overview dashboard |
| Written report | `Report & Demo/NDTA631_Group_Report.docx` and `.pdf` | Narrative, methods, findings, and recommendations |
| Database evidence | `Database Integration/food_security.db`, `schema.sql`, `queries.sql`, and exported query-result CSVs | Auditable SQLite integration and SQL evidence |
| Reproducible workflow | `Python or Excel Data Analysis/food_security_pipeline.py` | Regenerates the derived outputs from the preserved raw extracts |

## Analysis scope

| Topic | Evidence used | Scope |
| --- | --- | --- |
| Severe food insecurity prevalence | World Development Indicators extract | South Africa, annual observations available for 2018–2023; unit: percentage of population |
| IPC phase distribution | Integrated Food Security Phase Classification extract | South Africa, October 2020 snapshot; units: persons and percentage of classified population |

This is a descriptive analysis of the observations supplied in the project extracts. The two datasets differ in metric and time coverage, so they are presented as complementary views rather than as directly interchangeable measures.

## Important reporting caveat

The October 2020 South Africa IPC record for **Phase 5 – Famine** is missing for both persons and percentage. It is not an observed zero. The analysis keeps the raw missing values and labels Phase 5 as **Not reported** in stakeholder-facing outputs.

For stakeholder communication, use the source-supplied Phase 3+ result rather than implying a confirmed Phase 5 value: **9,335,159 people, or 16.0% of the classified population, were recorded in Phase 3 or above** in the October 2020 snapshot. The full evidence and wording guidance are in [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md).

## Repository structure

| Folder | Contents |
| --- | --- |
| `Raw datasets/` | Preserved source CSV extracts. Do not edit these files. |
| `Data Preparation/` | South Africa cleaned files, descriptive statistics, and data-quality notes. |
| `Numeric Analysis/` | Numerical summaries, phase tables, and year-on-year calculations. |
| `Python or Excel Data Analysis/` | Reusable Python pipeline, transformed tables, and Excel workbook. |
| `Database Integration/` | SQLite database, schema, query script, query exports, and safe-operation evidence. |
| `Visualisation/` | Final labelled PNG charts and chart explanations. |
| `Report & Demo/` | Markdown, DOCX, and PDF report versions plus demo material. |

Each workflow folder includes a `PROCESS.txt` guide describing its role in the pipeline.

## Data provenance

The project uses two locally supplied World Bank Data360 extracts:

- `WB_WDI_SN_ITK_SVFI_ZS.csv` — World Development Indicators, indicator `WB_WDI_SN_ITK_SVFI_ZS`, *Prevalence of severe food insecurity in the population (%)*.
- `IPC_IPC.csv` — Integrated Food Security Phase Classification database, including `IPC_IPC_P3PLUS` and phase-level observations.

Read [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md) before presenting the results. It records the source identifiers, country filters, data limitations, and the Phase 5 interpretation constraint. The supplied extracts do not include a download URL or retrieval timestamp, so those fields should be added from the source portal before any external publication.

## Reproduce the analysis

### Prerequisites

- Python 3.10 or later (the current project environment was tested with Python 3.14.6).
- Internet access is not required to run the pipeline because the input extracts are stored locally.
- Microsoft Excel or a compatible spreadsheet application is recommended for reviewing the generated workbook.

### Setup

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If script execution is restricted on a managed Windows device, activate the environment using the organisation-approved method, then run the same `pip` commands.

### Run

```powershell
python "Python or Excel Data Analysis\food_security_pipeline.py"
```

The script checks for both raw CSV inputs, filters South Africa records, creates cleaned and numerical outputs, writes the SQLite database and query exports, creates the Excel workbook and visualisations, and regenerates the report/demo pack. A successful run ends with:

```text
Food security analysis pipeline completed successfully.
```

> **Important:** Running the pipeline intentionally replaces generated files in `Data Preparation/`, `Numeric Analysis/`, `Database Integration/`, `Visualisation/`, `Python or Excel Data Analysis/`, and `Report & Demo/`. Preserve any manual edits or presentation annotations before rerunning it. It does not modify the raw source CSV files.

## Verification checklist

After a successful run, confirm that these evidence items are present:

- `Data Preparation/cleaned_severe_food_insecurity_south_africa.csv` and `cleaned_ipc_phase_distribution_south_africa.csv`
- `Numeric Analysis/numerical_summary.csv` and `ipc_phase_summary.csv`
- `Python or Excel Data Analysis/food_security_analysis_workbook.xlsx`
- `Database Integration/food_security.db` plus `query_result_*.csv`
- `Visualisation/food_security_overview_dashboard.png`
- `Report & Demo/NDTA631_Group_Report.pdf`

Open the Excel workbook to validate the analysis tables and embedded charts, and use the generated PNG files as report or slide exports. When discussing results, retain the units exactly as labelled: percentages for severe food insecurity, people/percentage for the IPC snapshot, and percentage points for year-on-year changes.

## Database integration

The pipeline creates `Database Integration/food_security.db` with these analytical tables:

- `ipc_cleaned`
- `ipc_phase_distribution`
- `severe_food_insecurity`
- `ipc_phase_summary`

`schema.sql` documents the analytical fields, and `queries.sql` records the SELECT statements and safe UPDATE/DELETE examples. The safe examples use `WHERE` clauses and a copied demonstration table; they are evidence of safe-query patterns, not a change to the production analytical data. Exported query results provide an auditable bridge between SQLite and the report/visual outputs.

## Technology stack

| Area | Tooling |
| --- | --- |
| Data preparation and analysis | Python, Pandas, NumPy |
| Visualisation | Matplotlib and Seaborn; Excel workbook charts for spreadsheet review |
| Database | SQLite through Python's standard `sqlite3` module |
| Excel output | OpenPyXL |
| Report generation | Python standard library, Matplotlib PDF backend, and generated DOCX/PDF artifacts |

Exact third-party package versions used in the current project environment are pinned in `requirements.txt`.

## Submission readiness

- [x] Raw source extracts preserved.
- [x] Reproducible Python pipeline and Excel workbook available.
- [x] Cleaned data, numerical tables, visual exports, SQLite database, and query results present.
- [x] Report and demo artifacts present.
- [ ] Add team names and student numbers to the final report files.
- [ ] Add the source portal URLs, retrieval dates, and any required citation/licence text before external publication.
