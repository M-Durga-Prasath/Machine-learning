# Week 3 Day 7 - Autonomous Driving Perception Mini-System

This folder contains the Day 7 capstone project for the Week 3 perception module.

## Project Overview

The goal of this mini-system is to build a simple autonomous-driving style perception pipeline using:

- YOLOv8 object detection
- ByteTrack multi-object tracking
- Persistent object IDs
- Motion trails
- Live scene analytics
- A basic pedestrian danger-zone alert

The main implementation is in:

- `capstoneproj.ipynb`

## What Was Done

The notebook processes a video feed and:

1. Detects objects with YOLOv8
2. Tracks objects across frames with ByteTrack
3. Draws persistent track IDs on detections
4. Shows motion trails for tracked objects
5. Counts vehicles and people on screen
6. Measures FPS during inference
7. Highlights a bottom danger zone
8. Triggers a pedestrian alert when a person enters that zone
9. Saves the annotated result video to `output/track1.mp4`

## Files in This Folder

- `capstoneproj.ipynb` - notebook for the complete perception pipeline
- `video.mp4` - input video used for the demo
- `yolov8n.pt` - YOLOv8 pretrained model used for detection
- `output/track1.mp4` - saved tracked demo video

## Tech Stack

- Python
- Ultralytics YOLOv8
- OpenCV
- PyTorch

## How to Run

1. Open `capstoneproj.ipynb`
2. Run the model and video setup cells
3. Run the tracking cell
4. Save the output video
5. Display `output/track1.mp4` inside the notebook

## Sample Output

The generated output video includes:

- Bounding boxes
- Class labels
- Confidence scores
- Tracking IDs
- Motion trails
- FPS overlay
- Unique vehicle count
- Pedestrian alert zone

## Future Improvements

Possible next steps for the project:

- Lane detection
- Traffic sign detection
- Depth estimation
- Sensor fusion
- Path planning

## Notes

This version uses `yolov8n.pt` as the detector. If a custom-trained `best.pt` model performs better, it can be swapped into the notebook later.
