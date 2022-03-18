import cv2
import myvars
import math
import datetime
import threading

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

def detectObj(frame):    
    classId, confs, boxes = cnn.detect(frame, confThreshold=0.3)
    detectResult = zip(classId.flatten(), confs.flatten(),boxes)
    print(detectResult)
    for classId_x, conf_x, box_x in detectResult:
        print (CocoClasses[classId_x], conf_x, box_x)
        cv2.rectangle(frame,box_x,color=(0,255,0),thickness=2)
        cv2.putText(frame
                    ,f'{CocoClasses[classId_x]} @ {conf_x}'
                    ,(box_x[0], box_x[1]-10)
                    , cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0,255,0), 2
                    );
    
    cv2.imshow("capture", frame)

    return frame

    


video = cv2.VideoCapture()
video.open(myvars.url1)
_,frame = video.read()
scale = 0.4
frame = cv2.resize(frame, (0,0), fx=scale, fy=scale)
width = frame.shape[0]
height = frame.shape[1]

cnn = cv2.dnn_DetectionModel(myvars.weights, myvars.config);
cnn.setInputSize(width, height);
cnn.setInputScale(1.0/127.5);
cnn.setInputMean(120);
cnn.setInputSwapRB(True)

while True:
    _, frame = video.read()
    frame = cv2.resize(frame, (0,0), fx=scale, fy=scale)
    frame = frame[math.floor(0.1*width):math.floor(0.6*width), math.floor(0.1*height):math.floor(0.5*height)]
    # print(frame.shape)
    cv2.imshow("video frames", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('s'):
        date_time = datetime.datetime.now().strftime("CAP-%d%m%Y-%H-%M-%S")
        # x = threading.Thread(target=detectObj, args=(frame))
        # detectedCapture = x.start()
        cv2.imwrite(f"screensYolo/{date_time}.png", detectObj(frame))

video.release()
cv2.destroyAllWindows()

