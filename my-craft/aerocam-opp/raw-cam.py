import cv2
import myvars
import datetime

video = cv2.VideoCapture()
video.open(myvars.url)

date_time = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
print(date_time)

while True:
    _,frame = video.read();
    print(frame.shape)
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    cv2.imshow("capture termoformado", frame)
    date_time = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
    print(date_time)
    key = cv2.waitKey(1);
    if key == ord('q'):
        break