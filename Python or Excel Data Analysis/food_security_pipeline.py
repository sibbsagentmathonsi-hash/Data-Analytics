from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "Raw datasets"
DATA_PREP_DIR = ROOT / "Data Preparation"
NUMERIC_DIR = ROOT / "Numeric Analysis"
VIS_DIR = ROOT / "Visualisation"
ANALYSIS_DIR = ROOT / "Python or Excel Data Analysis"

IPC_RAW = RAW_DIR / "Integrated Food Security Phase Classification" / "IPC_IPC.csv"
SVFI_RAW = (
    RAW_DIR
    / "Prevalence of severe food insecurity in the population (%)"
    / "WB_WDI_SN_ITK_SVFI_ZS.csv"
)


def ensure_output_dirs() -> None:
    for directory in [DATA_PREP_DIR, NUMERIC_DIR, VIS_DIR, ANALYSIS_DIR]:
        directory.mkdir(parents=True, exist_ok=True)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = (
        cleaned.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("/", "_", regex=False)
    )
    return cleaned


def load_raw_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    if not IPC_RAW.exists():
        raise FileNotFoundError(f"Missing IPC raw dataset: {IPC_RAW}")
    if not SVFI_RAW.exists():
        raise FileNotFoundError(f"Missing severe food insecurity raw dataset: {SVFI_RAW}")

    ipc = normalize_columns(pd.read_csv(IPC_RAW))
    svfi = normalize_columns(pd.read_csv(SVFI_RAW))
    return ipc, svfi


def clean_ipc(ipc: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    zaf = ipc.loc[
        (ipc["ref_area"].eq("ZAF")) | (ipc["ref_area_label"].eq("South Africa"))
    ].copy()

    keep_cols = [
        "ref_area",
        "ref_area_label",
        "indicator",
        "indicator_label",
        "unit_measure",
        "unit_measure_label",
        "unit_type",
        "unit_type_label",
        "comp_breakdown_1_label",
        "comp_breakdown_2",
        "comp_breakdown_2_label",
        "time_period",
        "obs_value",
        "obs_status_label",
        "obs_conf_label",
    ]
    zaf = zaf[keep_cols]
    zaf["obs_value"] = pd.to_numeric(zaf["obs_value"], errors="coerce")
    zaf["period"] = pd.to_datetime(zaf["time_period"], format="%Y-%m", errors="coerce")
    zaf["year"] = zaf["period"].dt.year
    zaf["month"] = zaf["period"].dt.month

    zaf["phase"] = (
        zaf["comp_breakdown_2_label"]
        .str.extract(r"(Phase \d - [A-Za-z]+)", expand=False)
        .fillna("Phase 3+")
    )
    zaf["metric"] = np.where(
        zaf["unit_measure_label"].eq("Persons"), "people", "percentage"
    )
    zaf["obs_value_filled"] = zaf["obs_value"].fillna(0)

    phases = zaf.loc[zaf["indicator"].eq("IPC_IPC_PHASE")].copy()
    phases["phase_order"] = (
        phases["phase"].str.extract(r"Phase (\d)", expand=False).astype(float)
    )
    phases = phases.sort_values(["metric", "phase_order"])

    p3plus = zaf.loc[zaf["indicator"].eq("IPC_IPC_P3PLUS")].copy()
    return zaf, phases, p3plus


def clean_svfi(svfi: pd.DataFrame) -> pd.DataFrame:
    zaf = svfi.loc[
        (svfi["ref_area"].eq("ZAF")) | (svfi["ref_area_label"].eq("South Africa"))
    ].copy()

    keep_cols = [
        "ref_area",
        "ref_area_label",
        "indicator",
        "indicator_label",
        "unit_measure",
        "unit_measure_label",
        "unit_type",
        "unit_type_label",
        "time_period",
        "obs_value",
        "obs_status_label",
        "obs_conf_label",
    ]
    zaf = zaf[keep_cols]
    zaf["year"] = pd.to_numeric(zaf["time_period"], errors="coerce").astype("Int64")
    zaf["obs_value"] = pd.to_numeric(zaf["obs_value"], errors="coerce")
    zaf = zaf.sort_values("year").reset_index(drop=True)
    zaf["year_on_year_change_percentage_points"] = zaf["obs_value"].diff()
    zaf["rolling_3_year_average"] = zaf["obs_value"].rolling(3, min_periods=1).mean()
    return zaf


def write_data_preparation_outputs(
    ipc_zaf: pd.DataFrame, ipc_phases: pd.DataFrame, svfi_zaf: pd.DataFrame
) -> None:
    ipc_zaf.to_csv(DATA_PREP_DIR / "cleaned_ipc_south_africa.csv", index=False)
    ipc_phases.to_csv(DATA_PREP_DIR / "cleaned_ipc_phase_distribution_south_africa.csv", index=False)
    svfi_zaf.to_csv(
        DATA_PREP_DIR / "cleaned_severe_food_insecurity_south_africa.csv",
        index=False,
    )

    stats_rows = [
        {
            "dataset": "Integrated Food Security Phase Classification",
            "raw_rows_for_south_africa": len(ipc_zaf),
            "missing_obs_values": int(ipc_zaf["obs_value"].isna().sum()),
            "minimum_obs_value": ipc_zaf["obs_value"].min(),
            "maximum_obs_value": ipc_zaf["obs_value"].max(),
            "mean_obs_value": ipc_zaf["obs_value"].mean(),
        },
        {
            "dataset": "Severe food insecurity prevalence",
            "raw_rows_for_south_africa": len(svfi_zaf),
            "missing_obs_values": int(svfi_zaf["obs_value"].isna().sum()),
            "minimum_obs_value": svfi_zaf["obs_value"].min(),
            "maximum_obs_value": svfi_zaf["obs_value"].max(),
            "mean_obs_value": svfi_zaf["obs_value"].mean(),
        },
    ]
    pd.DataFrame(stats_rows).to_csv(
        DATA_PREP_DIR / "descriptive_statistics.csv", index=False
    )

    notes = [
        "DATA QUALITY NOTES",
        "",
        "Scope:",
        "- Both raw datasets were filtered to South Africa using REF_AREA = ZAF or REF_AREA_LABEL = South Africa.",
        "- Raw files were not edited. Cleaned outputs were saved in the Data Preparation folder.",
        "",
        "Integrated Food Security Phase Classification:",
        f"- South Africa rows retained: {len(ipc_zaf)}.",
        f"- Missing OBS_VALUE entries: {int(ipc_zaf['obs_value'].isna().sum())}.",
        "- Missing IPC Phase 5 values were kept in the cleaned file and treated as 0 only in numeric summaries where a total is required.",
        "- The IPC dataset provides a snapshot for 2020-10, including counts and percentages by phase.",
        "",
        "Severe food insecurity prevalence:",
        f"- South Africa rows retained: {len(svfi_zaf)}.",
        f"- Missing OBS_VALUE entries: {int(svfi_zaf['obs_value'].isna().sum())}.",
        "- Values are percentages and cover the available years in the raw dataset.",
    ]
    (DATA_PREP_DIR / "data_quality_notes.txt").write_text("\n".join(notes), encoding="utf-8")


def write_numeric_outputs(
    ipc_phases: pd.DataFrame, p3plus: pd.DataFrame, svfi_zaf: pd.DataFrame
) -> pd.DataFrame:
    people = ipc_phases.loc[ipc_phases["metric"].eq("people")].copy()
    percentages = ipc_phases.loc[ipc_phases["metric"].eq("percentage")].copy()

    total_population_classified = people["obs_value_filled"].sum()
    p3plus_people = float(
        p3plus.loc[p3plus["metric"].eq("people"), "obs_value_filled"].iloc[0]
    )
    p3plus_percent = float(
        p3plus.loc[p3plus["metric"].eq("percentage"), "obs_value_filled"].iloc[0]
    )
    crisis_or_worse_people = people.loc[
        people["phase"].isin(["Phase 3 - Crisis", "Phase 4 - Emergency", "Phase 5 - Famine"]),
        "obs_value_filled",
    ].sum()

    svfi_values = svfi_zaf["obs_value"].to_numpy(dtype=float)
    svfi_years = svfi_zaf["year"].to_numpy(dtype=int)
    svfi_changes = np.diff(svfi_values)

    summary = pd.DataFrame(
        [
            {
                "metric": "IPC total classified population, 2020-10",
                "value": round(total_population_classified, 2),
                "unit": "people",
            },
            {
                "metric": "IPC people in Phase 3 or above, 2020-10",
                "value": round(p3plus_people, 2),
                "unit": "people",
            },
            {
                "metric": "IPC percentage in Phase 3 or above, 2020-10",
                "value": round(p3plus_percent, 2),
                "unit": "percent",
            },
            {
                "metric": "Calculated crisis-or-worse people from phase rows",
                "value": round(float(crisis_or_worse_people), 2),
                "unit": "people",
            },
            {
                "metric": "Severe food insecurity prevalence average",
                "value": round(float(np.mean(svfi_values)), 2),
                "unit": "percent",
            },
            {
                "metric": "Severe food insecurity prevalence minimum",
                "value": round(float(np.min(svfi_values)), 2),
                "unit": "percent",
            },
            {
                "metric": "Severe food insecurity prevalence maximum",
                "value": round(float(np.max(svfi_values)), 2),
                "unit": "percent",
            },
            {
                "metric": "Severe food insecurity total change",
                "value": round(float(svfi_values[-1] - svfi_values[0]), 2),
                "unit": "percentage points",
            },
        ]
    )
    summary.to_csv(NUMERIC_DIR / "numerical_summary.csv", index=False)

    yoy = pd.DataFrame(
        {
            "from_year": svfi_years[:-1],
            "to_year": svfi_years[1:],
            "change_percentage_points": np.round(svfi_changes, 2),
        }
    )
    yoy.to_csv(NUMERIC_DIR / "severe_food_insecurity_year_on_year_change.csv", index=False)

    phase_summary = people[["phase", "obs_value_filled"]].merge(
        percentages[["phase", "obs_value_filled"]],
        on="phase",
        suffixes=("_people", "_percentage"),
    )
    phase_summary.rename(
        columns={
            "obs_value_filled_people": "people",
            "obs_value_filled_percentage": "percentage",
        },
        inplace=True,
    )
    phase_summary["people"] = phase_summary["people"].round(0)
    phase_summary["percentage"] = phase_summary["percentage"].round(1)
    phase_summary.to_csv(NUMERIC_DIR / "ipc_phase_summary.csv", index=False)

    findings = [
        "NUMERICAL FINDINGS",
        "",
        f"- The severe food insecurity prevalence series runs from {svfi_years[0]} to {svfi_years[-1]}.",
        f"- Prevalence increased from {svfi_values[0]:.1f}% in {svfi_years[0]} to {svfi_values[-1]:.1f}% in {svfi_years[-1]}, a change of {svfi_values[-1] - svfi_values[0]:.1f} percentage points.",
        f"- The highest severe food insecurity prevalence in the available data is {np.max(svfi_values):.1f}%.",
        f"- The average severe food insecurity prevalence is {np.mean(svfi_values):.2f}%.",
        f"- In the IPC 2020-10 snapshot, {p3plus_people:,.0f} people were in Phase 3 or above, equal to {p3plus_percent:.1f}% of the classified population.",
        f"- The phase rows calculate {crisis_or_worse_people:,.0f} people in crisis-or-worse phases when missing Phase 5 values are treated as 0.",
    ]
    (NUMERIC_DIR / "numerical_findings.txt").write_text("\n".join(findings), encoding="utf-8")

    return phase_summary


def write_analysis_summary(svfi_zaf: pd.DataFrame, phase_summary: pd.DataFrame) -> None:
    latest_svfi = svfi_zaf.iloc[-1]
    analysis_summary = pd.DataFrame(
        [
            {
                "section": "Severe food insecurity trend",
                "finding": f"South Africa's severe food insecurity prevalence reached {latest_svfi['obs_value']:.1f}% in {int(latest_svfi['year'])}.",
            },
            {
                "section": "IPC phase distribution",
                "finding": "The IPC 2020-10 snapshot shows most classified people in Phase 1 or Phase 2, but a meaningful share in Phase 3 or above.",
            },
            {
                "section": "Project interpretation",
                "finding": "The datasets can be used together to explain both longer-term severe food insecurity prevalence and a detailed phase snapshot.",
            },
        ]
    )
    analysis_summary.to_csv(ANALYSIS_DIR / "analysis_summary.csv", index=False)
    phase_summary.to_csv(ANALYSIS_DIR / "transformed_ipc_phase_table.csv", index=False)
    svfi_zaf.to_csv(ANALYSIS_DIR / "transformed_svfi_trend_table.csv", index=False)


def save_visualisations(svfi_zaf: pd.DataFrame, phase_summary: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid", palette="Set2")
    plt.rcParams["figure.dpi"] = 140

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(data=svfi_zaf, x="year", y="obs_value", marker="o", linewidth=2.5, ax=ax)
    ax.set_title("South Africa: Severe Food Insecurity Prevalence", fontsize=14, weight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population with severe food insecurity (%)")
    ax.set_xticks(svfi_zaf["year"].astype(int).tolist())
    ax.set_ylim(0, max(10, svfi_zaf["obs_value"].max() + 1))
    for _, row in svfi_zaf.iterrows():
        ax.text(row["year"], row["obs_value"] + 0.12, f"{row['obs_value']:.1f}%", ha="center", fontsize=8)
    fig.tight_layout()
    fig.savefig(VIS_DIR / "severe_food_insecurity_trend.png")
    plt.close(fig)

    plot_people = phase_summary.copy()
    plot_people["people_millions"] = plot_people["people"] / 1_000_000
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=plot_people, x="people_millions", y="phase", hue="phase", legend=False, ax=ax)
    ax.set_title("South Africa IPC Phase Distribution by People, 2020-10", fontsize=14, weight="bold")
    ax.set_xlabel("People (millions)")
    ax.set_ylabel("IPC phase")
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1fM", padding=3, fontsize=8)
    fig.tight_layout()
    fig.savefig(VIS_DIR / "ipc_phase_distribution_people.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(data=phase_summary, x="phase", y="percentage", hue="phase", legend=False, ax=ax)
    ax.set_title("South Africa IPC Phase Distribution by Percentage, 2020-10", fontsize=14, weight="bold")
    ax.set_xlabel("IPC phase")
    ax.set_ylabel("Classified population (%)")
    ax.tick_params(axis="x", rotation=25)
    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f%%", padding=3, fontsize=8)
    fig.tight_layout()
    fig.savefig(VIS_DIR / "ipc_phase_distribution_percentage.png")
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    sns.lineplot(data=svfi_zaf, x="year", y="obs_value", marker="o", ax=axes[0])
    axes[0].set_title("Severe Food Insecurity Trend")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("% of population")
    sns.barplot(data=plot_people, x="people_millions", y="phase", hue="phase", legend=False, ax=axes[1])
    axes[1].set_title("IPC Phase Snapshot, 2020-10")
    axes[1].set_xlabel("People (millions)")
    axes[1].set_ylabel("")
    fig.suptitle("South Africa Food Security Overview", fontsize=16, weight="bold")
    fig.tight_layout()
    fig.savefig(VIS_DIR / "food_security_overview_dashboard.png")
    plt.close(fig)

    explanations = [
        "CHART EXPLANATIONS",
        "",
        "severe_food_insecurity_trend.png:",
        "- Shows the annual percentage of South Africa's population experiencing severe food insecurity in the available WDI data.",
        "- The line rises from 2018 to 2023, indicating a worsening prevalence over the period.",
        "",
        "ipc_phase_distribution_people.png:",
        "- Shows the number of people in each IPC phase in the 2020-10 South Africa snapshot.",
        "- Phase 1 and Phase 2 contain the largest groups, but Phase 3 and Phase 4 still represent millions of people.",
        "",
        "ipc_phase_distribution_percentage.png:",
        "- Shows the same IPC phase distribution as percentages of the classified population.",
        "- The chart supports the Phase 3+ result of 16% in crisis-or-worse food insecurity.",
        "",
        "food_security_overview_dashboard.png:",
        "- Combines the trend view and IPC snapshot for use in the report or presentation.",
    ]
    (VIS_DIR / "chart_explanations.txt").write_text("\n".join(explanations), encoding="utf-8")


def main() -> None:
    ensure_output_dirs()
    ipc_raw, svfi_raw = load_raw_data()
    ipc_zaf, ipc_phases, p3plus = clean_ipc(ipc_raw)
    svfi_zaf = clean_svfi(svfi_raw)
    write_data_preparation_outputs(ipc_zaf, ipc_phases, svfi_zaf)
    phase_summary = write_numeric_outputs(ipc_phases, p3plus, svfi_zaf)
    write_analysis_summary(svfi_zaf, phase_summary)
    save_visualisations(svfi_zaf, phase_summary)
    print("Food security analysis pipeline completed successfully.")


if __name__ == "__main__":
    main()
