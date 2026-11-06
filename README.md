# South African Food Security Analysis

A personal portfolio project exploring food insecurity indicators in South Africa through data preparation, descriptive analysis, SQL, and visualisation. The analysis brings together an annual severe-food-insecurity series and an October 2020 Integrated Food Security Phase Classification (IPC) snapshot.

## Project objective

Transform public data extracts into clear, carefully qualified findings that can support understanding and communication of food-security conditions in South Africa.

## Data and scope

- **Severe food insecurity prevalence:** South Africa, annual observations for 2018–2023, measured as a percentage of the population. Source: World Development Indicators extract.
- **IPC phase distribution:** South Africa, October 2020 snapshot, measured in people and percentage of the classified population. Source: Integrated Food Security Phase Classification extract.

These datasets cover different measures and time periods. They are presented as complementary views, not directly interchangeable measures.

## Work included

- Data preparation, quality checks, and descriptive statistics
- Numerical summaries and year-on-year analysis
- SQLite database integration with schema and SQL queries
- Analysis workbook and labelled visualisations
- Written findings and reproducible workflow materials

## Repository structure

- **Data Preparation/** - cleaned data, descriptive statistics, and quality notes
- **Numeric Analysis/** - numerical summaries and calculations
- **Python or Excel Data Analysis/** - analysis workflow and workbook
- **Database Integration/** - SQLite database, schema, queries, and query exports
- **Visualisation/** - labelled charts and explanations
- **Report & Demo/** - project report and presentation materials

## Important interpretation note

The October 2020 South Africa IPC extract has no reported value for Phase 5 (Famine). This is missing data, not an observed zero. The source-supplied Phase 3+ result records 9,335,159 people, or 16.0% of the classified population, in Phase 3 or above. Refer to [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md) for source details and interpretation limitations.

## Tools and skills

Data cleaning, descriptive analysis, SQL, SQLite, spreadsheet analysis, data visualisation, and communicating evidence with appropriate context.

## Reproducing the analysis

See the workflow guides in the project folders and [DATA_SOURCES_AND_PROVENANCE.md](DATA_SOURCES_AND_PROVENANCE.md) for source identifiers, filters, and data limitations. The supplied data extracts are stored in the repository.

---

Prepared as an individual data analytics portfolio project by Sibusiso Agent Mathonsi.
