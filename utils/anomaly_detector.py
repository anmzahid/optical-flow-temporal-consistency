# utils/anomaly_detector.py
import numpy as np
from ..config import ANOMALY_STD_MULTIPLIER

def detect_anomalies(temporal_consistency):
    if len(temporal_consistency) == 0:
        print("No temporal consistency data – no anomalies detected.")
        return []
    
    mean_val = np.mean(temporal_consistency)
    std_val = np.std(temporal_consistency)
    threshold = mean_val + ANOMALY_STD_MULTIPLIER * std_val
    
    # Anomaly at transition i → i+1 means highlight frame i+1
    anomaly_frames = [i + 2 for i, val in enumerate(temporal_consistency) if val > threshold]
    
    print(f"Anomaly threshold: {threshold:.2f}")
    print(f"Detected anomalous frames (to highlight): {anomaly_frames}")
    
    return anomaly_frames