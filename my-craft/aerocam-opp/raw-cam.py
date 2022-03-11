import cv2
import myvars
import datetime

video = cv2.VideoCapture()
video.open(myvars.url)

dateAndTime = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
print(dateAndTime)

while True:
    _,frame = video.read();

    print(frame.shape)
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    cv2.imshow("capture termoformado", frame)
    dateAndTime = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
    print(dateAndTime)
    key = cv2.waitKey(1);
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite(f'screensRaw/{dateAndTime}.jpg',frame)