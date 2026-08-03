# NDTA631 Data Analysis and Visualisation

Professional repository for the NDTA631 2026 group assignment. The project analyses South African food security indicators from World Bank Data360 and organises the complete workflow from raw datasets to reporting, charts, database work, and demo evidence.

## Project Focus

| Area | Details |
| --- | --- |
| Module | NDTA631 Data Analysis and Visualisation |
| Assessment | Group Assignment 2026 |
| Topic | South African food security and severe food insecurity |
| Data source | World Bank Data360 / World Bank Open Data |
| Due date | 24 August 2026 |
| Main tools | Python, Pandas, NumPy, Matplotlib, Seaborn, SQL or Excel |

## Research Story

This project uses two related food-security datasets to answer a clear question:

> How do South Africa's food insecurity classifications and severe food insecurity prevalence describe the country's food security situation over time?

The analysis should connect the datasets into one story by comparing:

- People in different Integrated Food Security Phase Classification categories.
- Severe food insecurity prevalence in the population.
- Changes across time periods where South African observations are available.
- Practical conclusions that can be explained clearly to a general reader.

## Repository Structure

| Folder | Purpose |
| --- | --- |
| `Raw datasets/` | Original food-security CSV files downloaded from World Bank Data360. Keep these files unchanged. |
| `Data Preparation/` | Cleaning scripts, cleaned datasets, missing-value handling notes, and descriptive statistics. |
| `Numeric Analysis/` | NumPy calculations, arrays, summary tables, and numerical interpretation. |
| `Visualisation/` | Charts, labelled plots, exported figures, and trend explanations. |
| `Database Integration/` | Database schema, SQL queries, import/export scripts, and database evidence. |
| `Python or Excel Data Analysis/` | Python notebooks/scripts or Excel workbooks used for transformations, charts, and summaries. |
| `Report & Demo/` | Final 7 to 9 page report, screenshots, presentation notes, and optional demo video material. |

Each main folder contains a `PROCESS.txt` guide explaining what should be done in that stage of the pipeline.

## Assignment Deliverables

The final submission should include:

- A 7 to 9 page report in DOCX and PDF formats.
- A clean GitHub repository with code, data workflow, and execution instructions.
- Python scripts, Jupyter notebooks, or Excel files showing the analysis.
- Environment configuration and clear setup notes.
- Clean, commented code with basic error handling.
- Evidence of database integration, including queries and safe update/delete operations.
- Clear visualisations with titles, labels, legends, and explanations.
- Optional but recommended video demo or screenshots.

## Suggested Workflow

1. Preserve the raw CSV files in `Raw datasets/`.
2. Filter the datasets for South Africa records where needed.
3. Clean column names, handle missing values, and save cleaned outputs in `Data Preparation/`.
4. Use NumPy in `Numeric Analysis/` to calculate totals, changes, averages, and comparisons.
5. Create labelled plots in `Visualisation/` using Matplotlib, Seaborn, Excel, or another approved tool.
6. Build a small database in `Database Integration/`, load cleaned data, and run select, update, delete, and export queries safely.
7. Summarise findings in `Python or Excel Data Analysis/` with transformed tables and charts.
8. Write the final report and prepare demo evidence in `Report & Demo/`.

## Data Handling Rules

- Do not edit the original raw CSV files directly.
- Save cleaned or transformed outputs in the relevant process folder.
- Use clear file names such as `cleaned_food_security.csv`, `summary_statistics.csv`, or `database_queries.sql`.
- Document assumptions, missing values, filters, and transformations.
- Keep charts readable with clear colour choices, titles, axis labels, and legends.

## Running the Project

Add the final scripts or notebooks as the analysis develops. A typical Python setup may look like:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas numpy matplotlib seaborn
```

If the group uses Excel instead of Python for parts of the analysis, place the workbook in `Python or Excel Data Analysis/` and include screenshots or exported charts in the relevant folders.

## Marking Alignment

| Criterion | Marks | Repository Evidence |
| --- | ---: | --- |
| Data Preparation | 15 | Cleaned data, missing-value handling, descriptive statistics |
| Numerical Analysis | 20 | NumPy arrays, calculations, tables, explained findings |
| Visualisation | 20 | Bar charts, scatter plots, histograms, box plots, trend explanations |
| Database Integration | 20 | Database file, schema, SQL queries, safe updates/deletes, Pandas import |
| Python/Excel Analysis | 15 | Transformed tables, formulas or scripts, charts, summaries |
| Report & Demo | 10 | Final report, screenshots, demo notes, optional video |

## Team Quality Checklist

- [ ] All group members' names and student numbers are included in report/code where required.
- [ ] At least two datasets are used together to tell one story.
- [ ] South Africa records are correctly filtered and explained.
- [ ] Missing values and data quality issues are documented.
- [ ] Numerical results are interpreted, not only calculated.
- [ ] Graphs are labelled and support the report conclusions.
- [ ] Database work is visible through scripts, screenshots, or schema diagrams.
- [ ] Final report is 7 to 9 pages and includes methods, charts, conclusions, and recommendations.
