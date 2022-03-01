import cv2
import myvars

print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

CocoClasses = ['person','bicycle','car','motorbike','aeroplane','bus','train',
            'truck','boat','traffic light','fire hydrant','stop sign',
            'parking meter','bench','bird','cat','dog','horse','sheep','cow',
            'elephant','bear','zebra','giraffe','backpack','umbrella',
            'handbag','tie','suitcase','frisbee','skis','snowboard',
            'sports ball','kite','baseball bat','baseball glove','skateboard',
            'surfboard','tennis racket','bottle','wine glass','cup','fork',
            'knife','spoon','bowl','banana','apple','sandwich','orange',
            'broccoli','carrot','hot dog','pizza','donut','cake','chair',
            'sofa','pottedplant','bed','diningtable','toilet','tvmonitor',
            'laptop','mouse','remote','keyboard','cell phone','microwave',
            'oven','toaster','sink','refrigerator','book','clock','vase',
            'scissors','teddy bear','hair drier','toothbrush'];

video = cv2.VideoCapture()
video.open(myvars.url)

while True:
    _, frame = video.read()
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    cv2.imshow("sec cam video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
