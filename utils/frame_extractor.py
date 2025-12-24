# utils/frame_extractor.py
import cv2
import os
from ..config import FRAMES_DIR

def extract_frames(video_path):
    os.makedirs(FRAMES_DIR, exist_ok=True)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Cannot open video file: {video_path}")
    
    count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        filename = os.path.join(FRAMES_DIR, f"frame_{count:04d}.png")
        cv2.imwrite(filename, frame)
        count += 1
    
    cap.release()
    print(f"Extracted {count} frames to {FRAMES_DIR}")
    return count