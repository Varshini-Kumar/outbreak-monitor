# Outbreak Monitor

AI-Based Infectious Disease Forecasting and Outbreak Detection System

## Overview

Outbreak Monitor is a predictive healthcare surveillance platform designed to detect potential infectious disease outbreaks using time-series forecasting and statistical anomaly detection.

The system collects anonymized disease case reports from multiple healthcare institutions, processes regional disease trends, predicts future case counts using ARIMA forecasting, and identifies abnormal disease escalation using Z-score analysis.

This project aims to support early outbreak detection, real-time monitoring, and proactive public health response.


## Features

- Regional disease surveillance
- Multi-hospital data aggregation
- ARIMA(1,1,1) time-series forecasting
- Z-score based anomaly detection
- Real-time outbreak alert generation
- Disease trend visualization
- Lightweight and scalable architecture

## Technologies Used

- Python 3
- Pandas
- NumPy
- Statsmodels
- Scikit-learn
- Matplotlib

## Project Structure

```bash
OUTBREAK/
│
├── src/
│   ├── main.py
│   ├── data_ingestion.py
│   ├── disease_timeseries.py
│   └── anomaly_detection.py
│
├── uploads/
│   ├── hospital_A.csv
│   ├── hospital_B.csv
│   └── hospital_C.csv
│
├── requirements.txt
└── README.md
```

## System Workflow

1. Upload disease datasets from hospitals
2. Validate and merge regional data
3. Preprocess time-series records
4. Forecast disease trends using ARIMA
5. Detect anomalies using Z-score analysis
6. Generate outbreak alerts
7. Visualize disease trends and risk levels

## Forecasting Model

The system uses the ARIMA(1,1,1) model for short-term infectious disease trend prediction.

The model captures:
- temporal dependencies
- trend patterns
- statistical variations in disease data

Fallback prediction is used when historical data is insufficient.

## Alert Classification

| Alert Level | Description |
|---|---|
| NORMAL | Disease activity within expected range |
| LOW | Moderate deviation detected |
| HIGH | Significant abnormal escalation detected |

## Performance Metrics

| Metric | Value |
|---|---|
| MAE | 1.00 |
| RMSE | 1.58 |
| MAPE | 6.83% |

## Future Enhancements

- Real-time hospital API integration
- Email/SMS outbreak notifications
- Deep learning forecasting models
- GIS-based outbreak heatmaps
- Interactive web dashboard deployment

## How to Run

### Install dependencies


pip install -r requirements.txt


### Run the project


python src/main.py


## Research Focus

- Epidemiological forecasting
- Disease surveillance systems
- AI-driven outbreak monitoring
- Statistical anomaly detection
- Public health analytics
