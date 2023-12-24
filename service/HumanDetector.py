import cv2
import os

# Path to the input video file
video_path = "./sampleVideo/sample.mp4"

# Extract the filename without extension from the video path
video_filename = os.path.splitext(os.path.basename(video_path))[0]

# Directory to store the snapshots
snapshot_dir = 'snapshot'
os.makedirs(snapshot_dir, exist_ok=True)

# Path to the Haar Cascade Classifier for full-body detection
haarcascade_path = 'haarcascade_fullbody.xml'
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haarcascade_path)

# Open the video capture
cap = cv2.VideoCapture(video_path)

# Interval between frames for processing (every 30 frames in this case)
frame_interval = 30
current_frame = 0

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Process every 'frame_interval' frames
    if current_frame % frame_interval == 0:

        # Convert the frame to grayscale for better detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect bodies (full-body detection) in the frame
        bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected bodies and save snapshots
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Save the snapshot with a filename indicating the snapshot number
            snapshot_path = os.path.join(snapshot_dir, f'snapshot_{len(os.listdir(snapshot_dir)) + 1}.jpg')
            cv2.imwrite(snapshot_path, frame)
            print(f'Snapshot saved: {snapshot_path}')

    # Increment the frame counter
    current_frame += 1

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()