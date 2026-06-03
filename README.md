# 🏎 Formula 1 AI Race Prediction & Driver Form Analytics Platform

## Overview

An end-to-end Formula 1 analytics platform that predicts race outcomes using 2026 season performance data, driver form metrics, qualifying positions, and explainable AI scoring.

The project extracts Formula 1 race results from the Jolpica F1 API, engineers driver performance features, generates race predictions, and visualizes results through an interactive Tableau dashboard.

---

## 🚀 Live Dashboard

📊 **Interactive Tableau Dashboard**

[Formula 1 AI Race Prediction & Driver Form Analytics Dashboard](https://public.tableau.com/app/profile/sai.pavan.rambhatla/viz/Formula1AIRacePredictionDriverFormAnalytics/Formula1AIRacePredictionDriverFormAnalytics?utm_source=chatgpt.com)

---

## Project Architecture

```text
Jolpica F1 API
        │
        ▼
2026 Race Results
        │
        ▼
Feature Engineering
        │
        ▼
Driver Form Metrics
        │
        ▼
Monaco Grid Position Input
        │
        ▼
Prediction Engine
        │
        ▼
Prediction Scores
        │
        ▼
Tableau Dashboard
```

---

## Technologies Used

### Programming

* Python
* Pandas
* NumPy

### Data Collection

* Jolpica Formula 1 API
* REST API Integration

### Analytics & Machine Learning

* Feature Engineering
* Driver Form Analysis
* Explainable AI Scoring
* Race Outcome Prediction

### Visualization

* Tableau Public

### Version Control

* Git
* GitHub

---

## Data Source

The project uses Formula 1 race data from the Jolpica API.

Data collected includes:

* Race Results
* Driver Information
* Constructor Information
* Grid Positions
* Points
* Finishing Positions

---

## Features Engineered

The prediction engine generates driver performance metrics using 2026 season results.

| Feature                 | Description                             |
| ----------------------- | --------------------------------------- |
| Recent Points           | Average points scored over recent races |
| Average Finish Position | Driver finishing consistency            |
| Podium Rate             | Percentage of podium finishes           |
| Grid Position           | Starting position for the race          |
| Race Count              | Number of races completed               |

---

## Prediction Methodology

The race prediction engine combines multiple driver performance indicators into a weighted prediction score.

### Monaco-Specific Weighting

| Feature                 | Weight |
| ----------------------- | ------ |
| Grid Position           | 35%    |
| Recent Points           | 25%    |
| Average Finish Position | 20%    |
| Podium Rate             | 20%    |

Monaco receives additional emphasis on qualifying position due to limited overtaking opportunities on the circuit.

---

## Explainable AI

The platform provides transparency by exposing feature-level contributions for every driver prediction.

For each prediction, the model explains:

* Impact of Grid Position
* Impact of Recent Performance
* Impact of Average Finishing Position
* Impact of Podium Consistency

This enables users to understand **why a driver is ranked above another driver**.

---

## Dashboard Components

### Driver Prediction Scores

Ranks drivers based on predicted race performance.

### Predicted Finishing Order

Displays projected race results for all drivers.

### Predicted Podium

Highlights projected podium finishers.

### Feature Contribution Breakdown

Visualizes how each feature contributes to the final prediction score.

### Interactive Filtering

Allows exploration of predictions by driver and constructor.

---

## Sample Monaco 2026 Prediction

| Position | Driver                | Team     |
| -------- | --------------------- | -------- |
| P1       | George Russell        | Mercedes |
| P2       | Andrea Kimi Antonelli | Mercedes |
| P3       | Charles Leclerc       | Ferrari  |
| P4       | Max Verstappen        | Red Bull |
| P5       | Oscar Piastri         | McLaren  |

---

## Project Structure

```text
f1-ai-race-prediction-platform/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│
├── src/
│   ├── extract_2026_results.py
│   ├── build_features.py
│   └── predict_monaco.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

### Clone Repository

```bash
git clone <repository-url>
cd f1-ai-race-prediction-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Extract 2026 Race Data

```bash
python src/extract_2026_results.py
```

### Build Driver Features

```bash
python src/build_features.py
```

### Generate Monaco Prediction

```bash
python src/predict_monaco.py
```

---

## Key Learning Outcomes

* Sports Analytics
* Feature Engineering
* Predictive Modeling
* Explainable AI
* Data Visualization
* API Integration
* End-to-End Analytics Workflow
* Tableau Dashboard Development

---

## Future Enhancements

* Random Forest Prediction Model
* XGBoost Race Predictor
* Monte Carlo Race Simulation
* Weather Impact Analysis
* Pit Stop Strategy Modeling
* Constructor Championship Predictions
* Live Race Weekend Prediction Updates

---

## Author

**Sai Pavan Rambhatla**

* MS in Electrical and Computer Engineering, University of Illinois Chicago
* Data Engineer | Analytics Engineer | Data Analytics Enthusiast

📊 Tableau Public Profile:

[Sai Pavan Rambhatla Tableau Public Profile](https://public.tableau.com/app/profile/sai.pavan.rambhatla?utm_source=chatgpt.com)

## License

This project is intended for educational, research, and portfolio purposes.
