# main.py
import argparse
import os
from utils.frame_extractor import extract_frames
from utils.flow_computer import compute_and_visualize_flow
from utils.anomaly_detector import detect_anomalies
from utils.video_generator import generate_demo_video

def main():
    parser = argparse.ArgumentParser(description="Modular Optical Flow Analysis Pipeline")
    parser.add_argument("video_path", help="Path to input video file")
    parser.add_argument("--output_video", default="demo_optical_flow.mp4", help="Output demo video name")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.video_path):
        raise FileNotFoundError(f"Video not found: {args.video_path}")
    
    print("=== Optical Flow Analysis Pipeline ===\n")
    
    print("1. Extracting frames...")
    extract_frames(args.video_path)
    
    print("\n2. Computing dense optical flow...")
    temporal_consistency = compute_and_visualize_flow()
    
    print("\n3. Detecting motion anomalies...")
    anomaly_frames = detect_anomalies(temporal_consistency)
    
    print("\n4. Generating demo video with visualizations...")
    generate_demo_video(anomaly_frames, args.output_video)
    
    print("\n=== Pipeline Complete! ===")
    print(f"Check: frames/, flows/, {args.output_video}, flow_analysis_plot.png")

if __name__ == "__main__":
    main()