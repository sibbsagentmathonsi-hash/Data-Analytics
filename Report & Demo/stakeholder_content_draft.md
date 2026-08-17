# Stakeholder Report Content Draft — South African Food Security

**Purpose.** This is a concise, eight-page content plan for the final stakeholder report. It is written from the supplied project extract and should be paired with polished Excel (or notebook) visuals and a corrected database evidence pack.

**Group Members.**
1. Sibusiso Agent Mathonsi 202331971
2. Kegoikantse Sebetseba 202414220
3. Agcobile Qabo 202469432
4. Lebogang Malatjie 202404978
5. Tlotlo Naledi 202422544
6. Tlotlanang Naledi 202422539

**Non-negotiable reporting rule.** The IPC Phase 5 observations in the supplied October 2020 extract are marked *Missing value*. They must be displayed as **Not reported**, never as `0`, `0%`, or `0.0M`. The report should use the source-reported Phase 3+ result of **9,335,159 people (16.0%)**.

---

<!-- PAGE 1 -->

## 1. Executive message and decision request

### South African food security: evidence indicates a rise in severe food insecurity, with an October 2020 acute-food-insecurity snapshot identifying a substantial Phase 3+ population

**Executive message.** In the supplied World Development Indicators extract, the prevalence of severe food insecurity in South Africa increased from **6.9% in 2018** to **8.5% in 2023** — a rise of **1.6 percentage points**. The latest value in this extract is also the highest in the six-year series. Separately, the October 2020 IPC snapshot reports **9.34 million people**, or **16.0% of the classified population**, in IPC Phase 3 or above (Crisis or worse).

These measures are complementary, not interchangeable. The annual WDI measure tracks severe food insecurity prevalence over time; the IPC result is a time-specific classification snapshot. Together they justify refreshing the evidence base, focusing planning attention on people in Crisis or worse, and obtaining subnational detail before making geographic allocation decisions.

**Decision requested from stakeholders.** Endorse a 90-day evidence-refresh and targeting workplan that:

- validates the current national position against the latest available sources;
- obtains provincial/district, demographic, and programme-coverage data;
- prioritises analysis of populations in IPC Phase 3+ where current, local evidence supports it; and
- establishes a governed dashboard with named data owners and a regular refresh cycle.

**Key indicators at a glance.**

| Indicator | Result | Interpretation |
| --- | ---: | --- |
| Severe food insecurity prevalence, 2018 | 6.9% | Baseline in the supplied annual series |
| Severe food insecurity prevalence, 2023 | 8.5% | Latest supplied annual observation; not a current 2026 estimate |
| Change, 2018–2023 | +1.6 percentage points | An increase in prevalence; do not describe it as “1.6%” |
| Average, 2018–2023 | 7.95% | Descriptive average across six annual observations |
| IPC Phase 3+, October 2020 | 9,335,159 people (16.0%) | Source-reported snapshot of Crisis or worse |

**Visual on this page.** A clean executive dashboard in Excel: three KPI cards, one small annual trend, and one Phase 3+ callout. Include the source and time-period note directly below the visual.

---

<!-- PAGE 2 -->

## 2. Decision question, scope, and sources

### Decision question

What does the supplied evidence indicate about the direction of severe food insecurity in South Africa, and what does the available IPC snapshot add about the severity distribution of acute food insecurity?

### Scope

The analysis is national in scope and uses South Africa records only (`REF_AREA = ZAF` or `REF_AREA_LABEL = South Africa`). It does not estimate causes, forecast future outcomes, assess intervention impact, or identify provincial/district hotspots.

### Data sources

| Source | Measure used | Time coverage in supplied extract | Role in the report |
| --- | --- | --- | --- |
| World Bank World Development Indicators (WDI), indicator `SN.ITK.SVFI.ZS` | Prevalence of severe food insecurity in the population (%) | 2018–2023 | Annual trend |
| World Bank Data360 extract, `IPC_IPC` | IPC phase distribution and source-reported Phase 3+ total | October 2020 | Acute-food-insecurity severity snapshot |

The WDI indicator is published by the World Bank with the Food and Agriculture Organization of the United Nations (FAO) named as source. See [World Bank WDI indicator SN.ITK.SVFI.ZS](https://data.worldbank.org/indicator/SN.ITK.SVFI.ZS). The supplied IPC data should be cited as the project’s World Bank Data360 extract, together with [World Bank Data360](https://data360.worldbank.org/) and the [IPC Acute Food Insecurity Classification methodology](https://www.ipcinfo.org/ipcinfo-website/ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/).

**Publication note.** Add the exact original download URLs, file version, licence, and access date from the group’s download record before issuing the report. Do not substitute the report publication date for the data-download date.

---

<!-- PAGE 3 -->

## 3. Method and data-quality assurance

### Analytical approach

1. Preserve the two raw source files unchanged.
2. Filter to South Africa and retain source identifiers, units, observation status, and time period.
3. Convert observations to numeric values; separate counts from percentages before calculating summaries.
4. Calculate annual year-on-year changes and a descriptive rolling average for the WDI series. Report changes in **percentage points**.
5. Use the source-reported `IPC_IPC_P3PLUS` observation for the Phase 3+ headline. Retain Phase 5 as missing where the source reports it as missing.
6. Store clean, documented records in the project database; reproduce visuals and summary tables from those records.

### Data-quality controls to state in the report

- The supplied South Africa WDI series contains six annual observations and no missing values.
- The supplied IPC extract contains both people counts and percentages. These are different units and must not be averaged together.
- The IPC Phase 5 people and percentage observations are missing in the supplied snapshot. A missing observation is an information gap, not evidence of zero people.
- The phase distribution is one October 2020 snapshot; the WDI series is annual and runs through 2023. The two measures cannot be combined into a single trend or used to infer causation.

**Visual on this page.** A one-panel data lineage: `Raw source files → validated South Africa records → SQLite tables → Excel dashboard/report`. Add row counts and a small data-quality callout: “Phase 5: not reported in supplied IPC snapshot.”

---

<!-- PAGE 4 -->

## 4. Finding 1 — severe food insecurity prevalence increased in the supplied annual series

### Headline

The supplied annual series rose from **6.9% in 2018** to **8.5% in 2023**, an increase of **1.6 percentage points**. Values increased from 2018 through 2021, were unchanged at 8.4% in 2021–2022, and then rose to 8.5% in 2023.

| Year | Severe food insecurity prevalence | Year-on-year change |
| ---: | ---: | ---: |
| 2018 | 6.9% | — |
| 2019 | 7.5% | +0.6 percentage points |
| 2020 | 8.0% | +0.5 percentage points |
| 2021 | 8.4% | +0.4 percentage points |
| 2022 | 8.4% | 0.0 percentage points |
| 2023 | 8.5% | +0.1 percentage points |

### Stakeholder interpretation

The observed upward movement warrants monitoring and a current-data refresh. It does **not** by itself establish why food insecurity changed, which population groups are affected, or where additional support should be directed. Those decisions require more recent and disaggregated evidence.

**Visual on this page.** An Excel line chart titled *South Africa: severe food insecurity prevalence, 2018–2023*. Show values as labels, keep a consistent y-axis across the report, and add the annotation “+1.6 percentage points since 2018.” Use a footnote: “Source: World Bank WDI, indicator SN.ITK.SVFI.ZS; supplied extract. Latest observation in extract: 2023.”

---

<!-- PAGE 5 -->

## 5. Finding 2 — the October 2020 IPC snapshot identifies a material Phase 3+ population

### Headline

In the supplied October 2020 IPC snapshot, **16.0%** of the classified population — **9,335,159 people** — was reported in **IPC Phase 3 or above (Crisis or worse)**.

| IPC phase | People | Share of classified population | Reporting treatment |
| --- | ---: | ---: | --- |
| Phase 1 — Minimal | 34,950,493 | 59% | Reported |
| Phase 2 — Stressed | 14,844,785 | 25% | Reported |
| Phase 3 — Crisis | 8,175,072 | 14% | Reported |
| Phase 4 — Emergency | 1,160,087 | 2% | Reported |
| Phase 5 — Famine | Not reported | Not reported | **Do not convert to zero** |
| Phase 3+ — Crisis or worse | 9,335,159 | 16.0% | Source-reported headline |

The IPC framework differentiates five acute-food-insecurity phases: Minimal/None, Stressed, Crisis, Emergency, and Catastrophe/Famine. Phase 3+ is conventionally referred to as Crisis or worse. See the [IPC classification overview](https://www.ipcinfo.org/ipcinfo-website/ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/).

### Stakeholder interpretation

The source-reported Phase 3+ result indicates a sizable group experiencing high levels of acute food insecurity in this snapshot. It supports prioritising current assessment and response planning for Crisis-or-worse populations, but it is not evidence that the same number or share applied in 2023 or today.

**Visual on this page.** A horizontal phase-distribution chart, ordered from Phase 1 to Phase 5 using an accessible severity palette. Mark Phase 3 and Phase 4 distinctly; show Phase 5 as “Not reported” with a note, not as a zero-length bar. Add a Phase 3+ callout of 9.34 million / 16.0%.

---

<!-- PAGE 6 -->

## 6. Reproducibility and database integration

### Why the database matters

The database is the report’s audit trail: it should make the path from raw source records to findings reproducible, allow stakeholders to inspect the metric definitions, and support refreshes without manually rebuilding tables or visuals.

### Stakeholder-facing assurance statement

The final evidence pack should contain:

- an entity-relationship diagram and data dictionary;
- executable database-definition and load scripts for all tables used in reporting;
- documented primary keys, foreign keys, validation checks, and indexes where appropriate;
- parameterised or clearly labelled queries that reproduce the annual trend, phase distribution, and Phase 3+ result;
- a safe update/delete demonstration performed only in a copied demo table, with before/after row counts and a transaction/rollback record; and
- exported query results that exactly match the stored SQL and Excel visuals.

### Suggested database narrative

“The analysis uses a reproducible SQLite reporting layer. Cleaned annual WDI observations and IPC phase observations are loaded with their source identifiers, units, observation status, and time period retained. Report-ready summary queries produce the annual trend and the October 2020 Phase 3+ snapshot. The database is an analytical evidence store, not a live operational system.”

**Visual on this page.** A compact ERD or data-lineage diagram plus a small table showing: question, query output, and dashboard use. Do not insert raw SQL screenshots as the main visual; place detailed SQL in an appendix/evidence pack.

---

<!-- PAGE 7 -->

## 7. Recommended actions

### 1. Refresh the evidence base before allocating resources

**Action:** Obtain the latest WDI/FAO release and the latest relevant IPC assessment, then document differences in coverage and methodology.  
**Owner:** [Data steward / monitoring and evaluation lead]  
**Timing:** Within 30 days  
**Success measure:** A signed-off refresh note identifying the current value, source version, and comparability to the supplied extract.

### 2. Add subnational and population-group detail

**Action:** Combine current food-security evidence with province/district, household, demographic, price, programme-coverage, and vulnerability data where permitted.  
**Owner:** [Analytics lead with programme and geographic data owners]  
**Timing:** Within 60–90 days  
**Success measure:** A prioritisation view that identifies where and for whom Phase 3+ risk or severe food insecurity warrants action.

### 3. Use Phase 3+ as a planning trigger, not a stand-alone allocation rule

**Action:** Define response and escalation criteria using current local evidence, feasibility, programme coverage, and risk context.  
**Owner:** [Programme / policy lead]  
**Timing:** At the next planning cycle  
**Success measure:** An approved trigger matrix that distinguishes monitoring, targeted support, and emergency escalation.

### 4. Establish governance for the stakeholder dashboard

**Action:** Publish an Excel or Power BI dashboard with metric definitions, source links, last-refresh date, data owner, and caveats on every page.  
**Owner:** [Business intelligence owner]  
**Timing:** Within 90 days  
**Success measure:** A dashboard refreshed on an agreed schedule with no unresolved data-quality exceptions.

---

<!-- PAGE 8 -->

## 8. Limitations, next steps, and references

### Limitations

- The WDI trend uses six supplied annual observations (2018–2023); it is descriptive and should not be extrapolated or presented as a forecast.
- The IPC evidence is a single October 2020 snapshot, so it does not establish a current position or trend.
- The WDI and IPC measures use different concepts, timing, and likely methodologies. Their relationship is contextual, not a direct numerical comparison or causal test.
- The analysis is national only. It does not identify geographic hotspots, demographic disparities, drivers, intervention effectiveness, or unmet need.
- Phase 5 is missing in the supplied IPC extract. No zero estimate should be inferred from this absence.
- “Latest” means latest in the supplied project extract. Refresh external data before any operational decision or public claim.

### Next reporting cycle

Update this report when current source data and subnational evidence are available. Retain the original extract and calculation version so that revisions are transparent rather than silently overwriting prior findings.

### References and source notes

1. World Bank. *Prevalence of severe food insecurity in the population (%)*, World Development Indicators, indicator `SN.ITK.SVFI.ZS`. https://data.worldbank.org/indicator/SN.ITK.SVFI.ZS. The page identifies the Food and Agriculture Organization of the United Nations as the source. Accessed: **[insert actual access date]**.
2. World Bank Data360. *Integrated Food Security Phase Classification* project extract (`IPC_IPC.csv`). https://data360.worldbank.org/. Exact dataset download URL, version, licence, and original access date: **[insert from download record]**.
3. Integrated Food Security Phase Classification. *IPC Acute Food Insecurity Classification*. https://www.ipcinfo.org/ipcinfo-website/ipc-overview-and-classification-system/ipc-acute-food-insecurity-classification/en/. Accessed: **[insert actual access date]**.

---

## Production checklist for the final report

- Replace this draft’s bracketed owners, dates, team details, and source-access fields.
- Use “percentage points” for differences between percentage values.
- Use `Not reported` for missing Phase 5 values; never substitute `0`.
- Add figure numbers, concise captions, direct source notes, and accessibility alt text.
- Keep the final report to eight pages by placing detailed SQL, data dictionaries, and validation logs in an appendix/evidence pack.
- Ensure every figure and table reconciles to the final database query output and Excel workbook.
