# Formula 1 AI Race Prediction & Driver Form Analytics Platform

## Live Dashboard

🔗 Tableau Dashboard

https://public.tableau.com/app/profile/sai.pavan.rambhatla/viz/Formula1AIRacePredictionDriverFormAnalytics/Formula1AIRacePredictionDriverFormAnalytics

## Overview

An end-to-end Formula 1 race prediction platform built using 2026 season performance data, driver form analytics, and explainable AI scoring. Designed to demonstrate predictive analytics, feature engineering, model explainability, and dashboard development using real-world Formula 1 data.

## Tech Stack

| Layer               | Technology             |
| ------------------- | ---------------------- |
| Data Source         | Jolpica F1 API         |
| Processing          | Python, Pandas, NumPy  |
| Feature Engineering | Python                 |
| Prediction Engine   | Weighted Scoring Model |
| Dashboard           | Tableau Public         |
| Version Control     | Git, GitHub            |

## Architecture

```text
Jolpica F1 API
      ↓
Raw Race Results
      ↓
Driver Form Features
      ↓
Monaco Grid Position Input
      ↓
Prediction Engine
      ↓
Prediction Scores
      ↓
Tableau Dashboard
```

## Prediction Framework

* Recent Points Performance
* Average Finish Position
* Podium Rate
* Grid Position Impact
* Monaco-Specific Race Weighting

## Key Features

* Formula 1 race prediction using 2026 season data
* Driver form analytics based on recent race performance
* Monaco-specific prediction weighting
* Explainable AI scoring methodology
* Feature contribution analysis
* Predicted podium and finishing order projections
* Interactive Tableau dashboard
* Automated Python data pipeline

## Pipeline Flow

```text
extract_2026_results
          ↓
build_features
          ↓
monaco_grid_input
          ↓
predict_monaco
          ↓
prediction_outputs
          ↓
tableau_dashboard
```

## Dashboard KPIs

* Driver Prediction Scores
* Predicted Finishing Order
* Predicted Podium
* Feature Contribution Breakdown
* Constructor Performance Comparison

## Explainable AI

The prediction engine exposes feature-level contributions for every driver ranking:

* Grid Position Contribution
* Recent Points Contribution
* Average Finish Contribution
* Podium Rate Contribution

This enables transparent race predictions and driver ranking analysis.

## Project Structure

```text
f1-ai-race-prediction-platform/
├── data/
│   ├── raw/                 # Raw race data from Jolpica API
│   └── processed/           # Driver form features and inputs
├── outputs/                 # Prediction outputs
├── src/
│   ├── extract_2026_results.py
│   ├── build_features.py
│   └── predict_monaco.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/f1-ai-race-prediction-platform.git
cd f1-ai-race-prediction-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Extract race results
python src/extract_2026_results.py

# Build driver features
python src/build_features.py

# Generate Monaco prediction
python src/predict_monaco.py
```

## Resume Highlights

* Built an end-to-end Formula 1 race prediction platform using Python, Pandas, and Tableau
* Engineered driver form features using 2026 season race results and qualifying data
* Developed a Monaco-specific prediction engine using weighted driver performance metrics
* Implemented explainable AI scoring with feature contribution analysis
* Automated data extraction and feature engineering pipelines using Formula 1 API data
* Published interactive Tableau dashboards for race forecasting and driver performance analysis

## Future Enhancements

* Random Forest Prediction Model
* XGBoost Race Prediction
* Monte Carlo Race Simulation
* Weather Impact Analysis
* Pit Stop Strategy Optimization
* Live Race Weekend Forecasting
