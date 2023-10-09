import cv2

# using public file path
from commonConfig import dataPath

# Create a background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Open a video capture stream (replace 'your_video_file.mp4' with the video file path)
cap = cv2.VideoCapture(dataPath)

# Set the window name
cv2.namedWindow('Moving Object Detection', cv2.WINDOW_NORMAL)  # Create a resizable window
cv2.resizeWindow('Moving Object Detection', 800, 600)  # Set the window size

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Apply background subtraction to the frame
    fgmask = fgbg.apply(frame)

    # Threshold the foreground mask to segment moving objects
    _, thresh = cv2.threshold(fgmask, 127, 255, cv2.THRESH_BINARY)

    # Find contours of the moving objects
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the detected moving objects
    for contour in contours:
        if cv2.contourArea(contour) > 10000:  # Adjust the area threshold as needed
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the original frame with moving object detection
    cv2.imshow('Moving Object Detection', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
