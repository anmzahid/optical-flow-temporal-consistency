# utils/video_generator.py
import cv2
import os
import numpy as np
from ..config import FRAMES_DIR, FLOW_PARAMS, DEMO_FPS, ARROW_STEP

def generate_demo_video(anomaly_frames, output_path="demo_optical_flow.mp4"):
    frames_list = sorted([f for f in os.listdir(FRAMES_DIR) if f.endswith(".png")])
    if len(frames_list) < 2:
        raise ValueError("Not enough frames to generate video.")
    
    sample_frame = cv2.imread(os.path.join(FRAMES_DIR, frames_list[0]))
    h, w, _ = sample_frame.shape
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, DEMO_FPS, (w, h))
    
    prev_gray = cv2.cvtColor(sample_frame, cv2.COLOR_BGR2GRAY)
    
    for idx in range(1, len(frames_list)):
        frame_path = os.path.join(FRAMES_DIR, frames_list[idx])
        frame = cv2.imread(frame_path)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, **FLOW_PARAMS)
        mag, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        
        # Heatmap overlay
        mag_norm = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        heatmap = cv2.applyColorMap(mag_norm, cv2.COLORMAP_JET)
        overlay = cv2.addWeighted(frame, 0.7, heatmap, 0.3, 0)
        
        # Draw motion arrows
        y_grid, x_grid = np.mgrid[ARROW_STEP//2:h:ARROW_STEP, ARROW_STEP//2:w:ARROW_STEP]
        y_grid, x_grid = y_grid.astype(int), x_grid.astype(int)
        fx = flow[y_grid, x_grid, 0]
        fy = flow[y_grid, x_grid, 1]
        
        for (x, y), dx, dy in zip(np.nditer([x_grid, y_grid]), fx.ravel(), fy.ravel()):
            end_x, end_y = int(x + dx), int(y + dy)
            cv2.arrowedLine(overlay, (x, y), (end_x, end_y), (0, 0, 0), 1, tipLength=0.3)
        
        # Highlight anomaly
        if idx in anomaly_frames:
            cv2.putText(overlay, "ANOMALY DETECTED", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 255), 4)
        
        out.write(overlay)
        prev_gray = gray
    
    out.release()
    print(f"Demo video with motion visualization saved: {output_path}")