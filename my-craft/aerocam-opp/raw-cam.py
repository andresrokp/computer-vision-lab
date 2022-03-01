import cv2
import myvars

video = cv2.VideoCapture()
video.open(myvars.url)

while True:
    _,frame = video.read();
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    cv2.imshow("capture termoformado", frame)
    key = cv2.waitKey(1);
    if key == ord('q'):
        break