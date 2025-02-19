Face Recognition Using OpenCV and face_recognition

Overview

This project implements real-time face recognition using the face_recognition and cv2 libraries. The program detects faces from a live webcam feed and identifies them based on a set of predefined images.

Features

Loads and encodes known faces from image files.

Captures video using the webcam.

Detects faces in real-time.

Compares detected faces with known encodings and identifies them.

Displays recognized names on the video feed.

Exits the program when 'q' is pressed.

Requirements

Python 3.x

OpenCV (cv2)

face_recognition library

NumPy (numpy)

Installation

Install dependencies:

pip install opencv-python numpy face-recognition

Ensure you have a webcam connected and working.

Usage

Place images of known persons in the specified directory (/Users/sohashaikh/Desktop/object detection open cv/).

Update the script with the correct file paths.

Run the script:

python face_recognition.py

The webcam feed will open, detecting and labeling known faces.

Press 'q' to exit the program.

How It Works

The script loads images of known individuals and encodes their facial features.

It continuously captures video frames and processes every alternate frame to improve performance.

It detects faces and compares them against known encodings.

If a match is found, the corresponding name is displayed.

Known Issues

The accuracy of recognition depends on lighting and image quality.

Processing many faces may slow down performance.

Future Improvements

Optimize for faster processing.

Implement database storage for face encodings.

Add support for multiple cameras.
