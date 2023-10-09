import cv2

# 替换为你的DVR串流的URL、用户名和密码
url = 'http://admin:a111111@192.168.1.161:80/CH1'

# 打开DVR视频流
cap = cv2.VideoCapture(url)

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频流")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 在这里进行图像处理
        # 例如，可以使用OpenCV函数对frame进行分析和处理
        cv2.imshow('DVR Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
