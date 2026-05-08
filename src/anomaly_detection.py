import numpy as np

# ---- Luminol compatibility patch ----
# Luminol uses numpy.asscalar(), which is removed.
# We patch it safely here.
if not hasattr(np, "asscalar"):
    np.asscalar = lambda x: x.item()
# -------------------------------------

from luminol.anomaly_detector import AnomalyDetector


def detect_anomalies(series):
    detector = AnomalyDetector(series)
    return detector.get_anomalies()
