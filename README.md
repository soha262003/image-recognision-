# Real-time Face Recognition with OpenCV and face_recognition

This Python script performs real-time face recognition using your webcam.  It utilizes the `face_recognition` library for face detection and recognition, and OpenCV (cv2) for video capture and image processing.

## Prerequisites

Before running the script, ensure you have the following libraries installed:

*   **OpenCV (cv2):** Install using: `pip install opencv-python`
*   **face_recognition:** Install using: `pip install face_recognition`
*   **NumPy:** Install using: `pip install numpy` (likely already installed with OpenCV or `face_recognition`)

## How to Run

1.  **Prepare your images:** Place the images of the people you want to recognize in a folder (e.g., "known_faces").  The script, as written, assumes the image files are directly in the same directory as the script.  You'll need to adjust the paths if they are in a subfolder.  Name the images with descriptive filenames (e.g., "Soha.jpg", "Harsha.jpg").
2.  **Clone or download the repository (or save the script):** If you have the code in a repository, clone it. Otherwise, save the Python code as a `.py` file (e.g., `face_recognition_realtime.py`).
3.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute it using: `python face_recognition_realtime.py`

## Usage

1.  **Capture video from your webcam:** The script will open a window displaying the feed from your default webcam.
2.  **Recognize faces:** The script will detect faces in each frame and compare them to the known faces you've provided.
3.  **Display names:** If a match is found, the name of the recognized person will be displayed below their face. If no match is found, "Unknown" will be displayed.
4.  **Exit:** Press the 'q' key on your keyboard to close the window and stop the script.

## Code Explanation

*   **Loading known faces:** The script loads images of known people, calculates their face encodings (a numerical representation of the face), and stores them along with their names.  **Important:** The current implementation assumes all the images are in the same directory as the script.  It's much better to use a loop to load images from a specified directory.  See the "Further Development" section for an example.
*   **Capturing video:** `cv2.VideoCapture(0)` opens the default webcam.
*   **Resizing and color conversion:** The frame is resized to improve performance (`fx=0.25`, `fy=0.25`) and converted from BGR (OpenCV's default) to RGB, which `face_recognition` requires.
*   **Face detection and encoding:** `face_recognition.face_locations` finds the locations of faces in the frame. `face_recognition.face_encodings` calculates the face encodings for the detected faces.
*   **Face comparison:** `face_recognition.compare_faces` compares the encodings of the detected faces with the encodings of the known faces.
*   **Drawing bounding boxes and labels:** The script draws rectangles around the detected faces and displays the corresponding names.
*   `process_this_frame`: This variable is used to process every other frame, further improving performance.

## Troubleshooting

*   **Webcam issues:** Ensure your webcam is working and properly connected.
*   **Missing libraries:** Double-check that all required libraries are installed.
*   **Recognition accuracy:** The accuracy of face recognition depends on the quality of the images used for training and the lighting conditions.  Better quality training images lead to better recognition.
*   **Performance:** Face recognition can be computationally intensive.  Resizing the frame helps, but you might still experience slow performance depending on your hardware.

