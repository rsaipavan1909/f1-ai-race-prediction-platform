import os
import requests
import pandas as pd

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE, "data", "raw")
PROCESSED_DIR = os.path.join(BASE, "data", "processed")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

BASE_URL = "https://api.jolpi.ca/ergast/f1"


def fetch_json(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def extract_2026_results():
    url = f"{BASE_URL}/2026/results.json?limit=1000"
    data = fetch_json(url)

    races = data["MRData"]["RaceTable"]["Races"]

    rows = []

    for race in races:
        season = int(race["season"])
        round_no = int(race["round"])
        race_name = race["raceName"]

        for result in race["Results"]:
            driver = result["Driver"]
            constructor = result["Constructor"]

            rows.append({
                "season": season,
                "round": round_no,
                "race_name": race_name,
                "driver_code": driver.get("code"),
                "driver_id": driver.get("driverId"),
                "driver_name": f"{driver.get('givenName')} {driver.get('familyName')}",
                "team_name": constructor.get("name"),
                "grid_position": int(result.get("grid", 0)) if str(result.get("grid", "0")).lstrip("-").isdigit() else None,
                "finish_position": int(result.get("positionOrder")) if result.get("positionOrder") else None,
                "classified_position": result.get("position"),
                "points": float(result.get("points", 0)),
                "status": result.get("status"),
                "laps": int(result.get("laps", 0)) if result.get("laps") else None,
            })

    df = pd.DataFrame(rows)

    raw_path = os.path.join(RAW_DIR, "jolpica_2026_results.csv")
    processed_path = os.path.join(PROCESSED_DIR, "race_results_2026.csv")

    df.to_csv(raw_path, index=False)
    df.to_csv(processed_path, index=False)

    print(f"Extracted rows: {len(df)}")
    print(f"Raw saved to: {raw_path}")
    print(f"Processed saved to: {processed_path}")
    print(df.head())


if __name__ == "__main__":
    extract_2026_results()