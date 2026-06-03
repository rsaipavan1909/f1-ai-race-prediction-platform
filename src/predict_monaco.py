import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FEATURES_FILE = os.path.join(BASE, "data", "processed", "driver_form_features.csv")
GRID_FILE = os.path.join(BASE, "data", "processed", "monaco_grid.csv")
OUTPUT_FILE = os.path.join(BASE, "outputs", "monaco_predictions.csv")

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

features = pd.read_csv(FEATURES_FILE)
grid = pd.read_csv(GRID_FILE)

df = grid.merge(features, on="driver_code", how="left")

df["prev_3_avg_points"] = df["prev_3_avg_points"].fillna(0)
df["prev_3_avg_finish"] = df["prev_3_avg_finish"].fillna(20)
df["podium_rate"] = df["podium_rate"].fillna(0)
df["avg_grid_position"] = df["avg_grid_position"].fillna(20)
df["driver_name"] = df["driver_name"].fillna(df["driver_code"])
df["team_name"] = df["team_name"].fillna("Unknown")

max_points = max(df["prev_3_avg_points"].max(), 1)
max_finish = max(df["prev_3_avg_finish"].max(), 1)
max_grid = max(df["grid_position"].max(), 1)

df["points_score"] = df["prev_3_avg_points"] / max_points

df["finish_score"] = 1 - ((df["prev_3_avg_finish"] - 1) / (max_finish - 1))
df["finish_score"] = df["finish_score"].clip(0, 1)

df["podium_score"] = df["podium_rate"]

df["grid_score"] = 1 - ((df["grid_position"] - 1) / (max_grid - 1))
df["grid_score"] = df["grid_score"].clip(0, 1)

df["prediction_score"] = (
      df["points_score"] * 0.25
    + df["finish_score"] * 0.20
    + df["podium_score"] * 0.20
    + df["grid_score"] * 0.35
)

df["points_contribution"] = df["points_score"] * 0.25
df["finish_contribution"] = df["finish_score"] * 0.20
df["podium_contribution"] = df["podium_score"] * 0.20
df["grid_contribution"] = df["grid_score"] * 0.35

df["prediction_reason"] = (
    "Grid="
    + df["grid_position"].astype(str)
    + ", AvgPts="
    + df["prev_3_avg_points"].round(1).astype(str)
)

df = df.sort_values("prediction_score", ascending=False)

df["predicted_position"] = range(1, len(df) + 1)

df["predicted_podium"] = 0
df.loc[df["predicted_position"] <= 3, "predicted_podium"] = 1

df["predicted_top_10"] = 0
df.loc[df["predicted_position"] <= 10, "predicted_top_10"] = 1

df.to_csv(OUTPUT_FILE, index=False)

CONTRIBUTIONS_OUTPUT_FILE = os.path.join(
    BASE,
    "outputs",
    "monaco_prediction_contributions.csv"
)

contribution_df = df[
    [
        "predicted_position",
        "driver_code",
        "driver_name",
        "team_name",
        "points_contribution",
        "finish_contribution",
        "podium_contribution",
        "grid_contribution",
    ]
].melt(
    id_vars=[
        "predicted_position",
        "driver_code",
        "driver_name",
        "team_name",
    ],
    value_vars=[
        "points_contribution",
        "finish_contribution",
        "podium_contribution",
        "grid_contribution",
    ],
    var_name="feature",
    value_name="contribution"
)

contribution_df["feature"] = contribution_df["feature"].replace({
    "points_contribution": "Recent points",
    "finish_contribution": "Average finish",
    "podium_contribution": "Podium rate",
    "grid_contribution": "Grid position",
})

contribution_df.to_csv(CONTRIBUTIONS_OUTPUT_FILE, index=False)

print(f"Contribution file saved to: {CONTRIBUTIONS_OUTPUT_FILE}")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

print("\n=== Monaco 2026 Prediction ===")
print(
    df[
        [
            "predicted_position",
            "driver_code",
            "driver_name",
            "team_name",
            "grid_position",
            #"prev_3_avg_points",
            #"prev_3_avg_finish",
            #"podium_rate",
            "prediction_score",
            #"prediction_reason"
            "points_contribution",
            "finish_contribution",
            "podium_contribution",
            "grid_contribution",
        ]
    ].head(10)
)

print(f"\nSaved to: {OUTPUT_FILE}")