import cv2
import myvars
import datetime

video = cv2.VideoCapture()
video.open(myvars.url1)

dateAndTime = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
print(dateAndTime)

counter = 0;
while True:
    _,frame = video.read();

    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    cv2.imshow("capture termoformado", frame)
    dateAndTime = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
    counter+=1
    print(counter)
    key = cv2.waitKey(1);
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite(f'screensRaw/{dateAndTime}.jpg',frame)