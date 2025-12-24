# utils/flow_computer.py
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from ..config import FRAMES_DIR, FLOWS_DIR, FLOW_PARAMS

def compute_and_visualize_flow():
    os.makedirs(FLOWS_DIR, exist_ok=True)
    
    frames = sorted([f for f in os.listdir(FRAMES_DIR) if f.endswith(".png")])
    if len(frames) < 2:
        raise ValueError("At least 2 frames required for optical flow.")
    
    prev_path = os.path.join(FRAMES_DIR, frames[0])
    prev_gray = cv2.imread(prev_path, cv2.IMREAD_GRAYSCALE)
    h, w = prev_gray.shape
    
    hsv = np.zeros((h, w, 3), dtype=np.uint8)
    hsv[..., 1] = 255
    
    prev_flow = None
    temporal_consistency = []
    avg_magnitudes = []
    
    for i in range(1, len(frames)):
        curr_path = os.path.join(FRAMES_DIR, frames[i])
        curr_gray = cv2.imread(curr_path, cv2.IMREAD_GRAYSCALE)
        
        flow = cv2.calcOpticalFlowFarneback(
            prev_gray, curr_gray, None,
            **FLOW_PARAMS
        )
        
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        avg_magnitudes.append(np.mean(mag))
        
        # Visualize and save flow
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        flow_path = os.path.join(FLOWS_DIR, f"flow_{i:04d}.png")
        cv2.imwrite(flow_path, bgr)
        
        if prev_flow is not None:
            diff = np.linalg.norm(flow - prev_flow)
            temporal_consistency.append(diff)
        
        prev_flow = flow.copy()
        prev_gray = curr_gray
    
    # Plot analysis
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(temporal_consistency, label="Temporal Consistency Diff")
    plt.title("Flow Temporal Consistency")
    plt.xlabel("Frame Pair Index")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(avg_magnitudes, label="Avg Magnitude", color="orange")
    plt.title("Average Motion Magnitude")
    plt.xlabel("Frame Index")
    plt.legend()
    
    plt.tight_layout()
    plt.savefig("flow_analysis_plot.png")
    plt.close()
    
    print(f"Optical flow visualizations saved to {FLOWS_DIR}")
    return temporal_consistency