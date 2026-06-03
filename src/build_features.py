import os
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FILE = os.path.join(BASE, "data", "processed", "race_results_2026.csv")
OUTPUT_FILE = os.path.join(BASE, "data", "processed", "driver_form_features.csv")

df = pd.read_csv(INPUT_FILE)

# Fix finish position
df["finish_position"] = df["finish_position"].fillna(df["classified_position"])
df["finish_position"] = pd.to_numeric(df["finish_position"], errors="coerce")
df["points"] = pd.to_numeric(df["points"], errors="coerce").fillna(0)
df["grid_position"] = pd.to_numeric(df["grid_position"], errors="coerce")

df = df.sort_values(["driver_code", "round"])

features = []

for driver in df["driver_code"].dropna().unique():
    driver_df = df[df["driver_code"] == driver].sort_values("round")

    latest = driver_df.iloc[-1]

    features.append({
        "driver_code": driver,
        "driver_name": latest["driver_name"],
        "team_name": latest["team_name"],
        "race_count": len(driver_df),

        "prev_3_avg_points": driver_df["points"].tail(3).mean(),
        "prev_3_avg_finish": driver_df["finish_position"].tail(3).mean(),
        "podium_rate": driver_df["finish_position"].le(3).mean(),
        "avg_grid_position": driver_df["grid_position"].mean()
    })

features_df = pd.DataFrame(features)

features_df.to_csv(OUTPUT_FILE, index=False)

print(f"Created features: {OUTPUT_FILE}")
print(features_df.head())
print(f"\nDrivers: {len(features_df)}")