import pandas as pd
import time

def create_disease_series(df):
    disease_series = {}

    df['date'] = pd.to_datetime(df['date'])

    for disease in df['disease'].unique():
        subset = df[df['disease'] == disease]
        grouped = subset.groupby('date')['patient_count'].sum()

        series = {}
        for dt, val in grouped.items():
            ts = int(dt.timestamp())  # ✅ convert to UNIX timestamp
            series[ts] = int(val)

        disease_series[disease] = series

    return disease_series
