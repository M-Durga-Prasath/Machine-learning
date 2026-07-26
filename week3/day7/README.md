# 🚗 Week 3 Capstone — Autonomous Driving Perception Pipeline

> **Location:** `week3/day7/`
> **Main notebook:** [`capstoneproj.ipynb`](capstoneproj.ipynb)

---

## What This Project Does

This project builds a **mini autonomous-driving perception system** that processes a dashcam-style video and produces a fully annotated output with real-time analytics. It combines object detection with multi-object tracking to simulate the perception layer of a self-driving car.

### Pipeline at a Glance

```
Input Video → YOLOv8 Detection → ByteTrack Tracking → Annotated Output Video
```

Specifically, the system:

1. **Detects objects** in every frame using a YOLOv8 model (`yolov8n.pt`)
2. **Tracks objects** across frames using the ByteTrack algorithm, assigning persistent IDs
3. **Draws motion trails** showing each tracked object's path over time
4. **Counts unique vehicles** and pedestrians on screen
5. **Monitors a danger zone** at the bottom of the frame — triggers a pedestrian alert when a person enters it
6. **Overlays live FPS** to measure inference speed
7. **Saves the annotated result** as a video to `output/track1.mp4`

---

## Sample Output Features

The generated output video includes:

| Feature | Description |
|---------|-------------|
| Bounding boxes | Drawn around every detected object |
| Class labels | Car, person, truck, etc. |
| Confidence scores | Model confidence for each detection |
| Tracking IDs | Persistent IDs that follow objects across frames |
| Motion trails | Visual path history for each tracked object |
| FPS overlay | Real-time frames-per-second counter |
| Vehicle count | Unique vehicle count displayed on screen |
| Pedestrian alert | Warning triggered when a person enters the danger zone |

---

## Files

| File | Description |
|------|-------------|
| `capstoneproj.ipynb` | Complete perception pipeline notebook |
| `video.mp4` | Input dashcam video used for the demo |
| `yolov8n.pt` | YOLOv8-nano pretrained model weights |
| `output/track1.mp4` | Saved annotated output video |

---

## Tech Stack

- **Detection:** Ultralytics YOLOv8
- **Tracking:** ByteTrack (via Ultralytics)
- **Video Processing:** OpenCV
- **Framework:** PyTorch

---

## How to Run

```bash
# Make sure you have the dependencies installed
pip install ultralytics opencv-python torch

# Open the notebook
jupyter notebook capstoneproj.ipynb
```

1. Run the model and video setup cells
2. Run the tracking/inference cell
3. The annotated video is saved to `output/track1.mp4`

---

## What I Learned

- How to chain detection → tracking into a real-time perception pipeline
- ByteTrack's approach to multi-object tracking using Kalman filters and IoU matching
- Drawing persistent annotations (trails, IDs, zone alerts) on video frames with OpenCV
- Measuring and displaying real-time FPS during inference

---

## Future Improvements

- Lane detection overlay
- Traffic sign recognition
- Depth estimation from monocular video
- Sensor fusion (camera + LiDAR simulation)
- Path planning integration
