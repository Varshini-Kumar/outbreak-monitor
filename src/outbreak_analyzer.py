def identify_outbreaks(disease_series, anomaly_map):
    outbreaks = []
    for disease, anomalies in anomaly_map.items():
        if len(anomalies) >= 2:   # sustained abnormal growth
            outbreaks.append(disease)
    return outbreaks
