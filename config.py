# config.py
import os

# Directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRAMES_DIR = os.path.join(BASE_DIR, "frames")
FLOWS_DIR = os.path.join(BASE_DIR, "flows")

# Optical Flow Parameters (Farneback)
FLOW_PARAMS = {
    "pyr_scale": 0.5,
    "levels": 3,
    "winsize": 15,
    "iterations": 3,
    "poly_n": 5,
    "poly_sigma": 1.2,
    "flags": 0
}

# Anomaly Detection
ANOMALY_STD_MULTIPLIER = 2.0

# Demo Video
DEMO_FPS = 20
ARROW_STEP = 16