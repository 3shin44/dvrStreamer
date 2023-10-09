import cv2
from commonConfig import dataPath


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


video_capture = cv2.VideoCapture(dataPath)

cv2.namedWindow('Video', cv2.WINDOW_NORMAL) 


cv2.resizeWindow('Video', 800, 600)  


while video_capture.isOpened():
    # 读取一帧
    ret, frame = video_capture.read()
    
    if not ret:
        break
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    cv2.imshow('Video', frame)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
