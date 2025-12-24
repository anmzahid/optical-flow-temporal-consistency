Here is a **clean, GitHub-ready `README.md`** version of your project. You can **copy–paste this directly** into your repository’s `README.md` file.

---

```markdown
# Optical Flow Temporal Consistency

A modular, easy-to-use Python tool for analyzing motion in videos using **dense optical flow** (Farneback algorithm from OpenCV).

This project extracts frames from a video, computes optical flow between consecutive frames, visualizes motion as color images, analyzes motion patterns, detects sudden changes (anomalies), and generates a **demo video** with motion heatmap, direction arrows, and anomaly highlights.

---

## 🔍 Why This Project Is Interesting

Understanding motion is a core problem in computer vision. Optical flow allows us to:
- Analyze how objects move over time
- Detect abnormal motion patterns
- Identify camera shakes, cuts, or sudden scene changes

This project provides a **complete end-to-end pipeline** for motion analysis that is:
- Practical
- Easy to customize
- Suitable for research, surveillance, sports analytics, and creative applications

---

## 🎯 Use Cases

Perfect for:
- Surveillance footage review
- Action / sports video analysis
- Detecting camera shake or abrupt motion
- Motion consistency research
- Creative video effects and motion studies

---

## ✨ Features

- Frame extraction from any video format supported by OpenCV  
- Dense optical flow using the **Farneback** method  
- Color-coded flow visualization  
  - Hue → direction  
  - Saturation → magnitude  
- Motion magnitude and temporal consistency analysis  
- Simple statistical anomaly detection (sudden motion changes)  
- Output demo video with:
  - Semi-transparent **JET heatmap** overlay
  - Black motion arrows (sparse grid)
  - Red **“ANOMALY DETECTED”** text on flagged frames  
- Clean, modular code with centralized configuration

---

## 📁 Project Structure

```

optical_flow_project/
├── main.py                     # Main script – runs the full pipeline
├── config.py                   # All tunable parameters (FPS, anomaly sensitivity, etc.)
├── requirements.txt            # Python dependencies
├── utils/
│   ├── **init**.py
│   ├── frame_extractor.py      # Extracts frames from video
│   ├── flow_computer.py        # Computes and visualizes optical flow
│   ├── anomaly_detector.py     # Detects motion anomalies
│   └── video_generator.py      # Creates final demo video
├── input_video.mp4             # Example placeholder (replace with your video)
├── frames/                     # Auto-created: extracted frames
├── flows/                      # Auto-created: optical flow visualization images
├── flow_analysis_plot.png      # Auto-created: motion statistics plot
└── demo_optical_flow.mp4       # Auto-created: final result video

````

---

## 🧩 Requirements

- Python **3.7+**
- OpenCV
- NumPy
- Matplotlib

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/optical_flow_project.git
cd optical_flow_project
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Use

### 1. Add Your Video

You have two options:

* **Option A (Simple)**
  Place your video in the project folder and rename it to:

  ```
  input_video.mp4
  ```

* **Option B (Recommended)**
  Use a video from any location using its full path.

Supported formats: `.mp4`, `.avi`, `.mov`, `.mkv`
(any format OpenCV can read)

---

### 2. Run the Analysis

#### Basic usage

```bash
python main.py input_video.mp4
```

#### Use a video from any directory

```bash
python main.py /path/to/your/video.mp4
```

#### Custom output video name

```bash
python main.py your_video.mp4 --output_video my_analysis_result.mp4
```

#### View all options

```bash
python main.py --help
```

---

## 📊 Output Files

After processing, the following files are generated:

* `frames/`
  → All extracted frames (PNG)

* `flows/`
  → Color-coded optical flow images

* `flow_analysis_plot.png`
  → Two plots:

  * Temporal consistency (spikes indicate anomalies)
  * Average motion magnitude over time

* `demo_optical_flow.mp4`
  → Final video with:

  * Motion heatmap overlay
  * Direction arrows
  * Anomaly alerts

---

## 🛠 Customization

Edit `config.py` to fine-tune the behavior:

```python
ANOMALY_STD_MULTIPLIER = 2.5  # Higher = fewer anomalies (1.5 = more sensitive)
DEMO_FPS = 30                # Output video frame rate
ARROW_STEP = 12              # Smaller = denser arrows (slower rendering)
```

You can also tweak `FLOW_PARAMS` for better performance on:

* Fast motion videos
* Low-light footage
* High-resolution clips

---

## 📌 Example

```bash
python main.py ../videos/sports_highlight.mp4 \
    --output_video sports_motion_analysis.mp4
```

---

## ⚠️ Notes

* Processing time depends on video length and resolution
* For re-running on a new video:

  * Delete or rename `frames/` and `flows/`
* Anomaly detection works best for:

  * Sudden motion
  * Scene cuts
  * Camera shake

---

## 🐞 Troubleshooting

* **Video not found**
  → Check file path and filename

* **OpenCV errors**
  → Convert video to MP4 format

* **Slow performance**
  → Use lower resolution or shorter clips

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## ❤️ Acknowledgements

Built with **Python + OpenCV**
December 2025

**Enjoy exploring motion in your videos!**

```

---

If you want next:
- ⭐ **Badge section** (Python, OpenCV, License)
- 📸 **GIF / demo video preview**
- 🧠 **Research-style motivation**
- 📈 **Results section**

Just tell me 👍
```
