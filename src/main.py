from data_ingestion import load_all_hospitals
from disease_timeseries import create_disease_series

def is_outbreak(series):
    """
    Determine if a disease is a new outbreak based on growth pattern.
    """

    # Sort by timestamp to guarantee correct order
    ordered = dict(sorted(series.items()))
    values = list(ordered.values())

    if len(values) < 4:
        return False

    # Baseline = average of first half
    mid = len(values) // 2
    baseline_avg = sum(values[:mid]) / mid

    # Recent = average of last 2 days
    recent_avg = sum(values[-2:]) / 2

    # Conditions for outbreak
    if baseline_avg == 0:
        return False

    growth_ratio = recent_avg / baseline_avg

    # Strong public-health threshold
    return growth_ratio >= 2.5 and recent_avg >= 20


def main():
    print("\n--- Disease Outbreak Detection System ---\n")

    df = load_all_hospitals()

    if df.empty:
        print("No hospital data available.")
        return

    disease_series = create_disease_series(df)

    outbreaks = []

    for disease, series in disease_series.items():
        if is_outbreak(series):
            outbreaks.append(disease)

    if outbreaks:
        print("⚠️ Potential New Disease Outbreaks Detected:\n")
        for d in outbreaks:
            print(f"- {d}")
    else:
        print("No abnormal disease spread detected.")

    print("\n--- Analysis Completed ---\n")


if __name__ == "__main__":
    main()
