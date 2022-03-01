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
_,capture = video.read()
capture = cv2.resize(capture, (0,0), fx=0.4, fy=0.4)
width = capture.shape[0]
height = capture.shape[1]
frame = capture


cnn = cv2.dnn_DetectionModel(myvars.weights, myvars.config);


# while True:
#     _, frame = video.read()
#     frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
#     cv2.imshow("sec cam video", frame)
#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break

cnn.setInputSize(width, height);
cnn.setInputScale(1.0/127.5);
cnn.setInputMean(120);
cnn.setInputSwapRB(True)

classId, confs, boxes = cnn.detect(capture, confThreshold=0.3)

detectResult = zip(classId.flatten(), confs.flatten(),boxes)
print(detectResult)


for classId_x, conf_x, box_x in detectResult:
    print (classId_x, conf_x, box_x)
    cv2.rectangle(capture,box_x,color=(0,255,0),thickness=2)
    cv2.putText(frame
                ,f'{CocoClasses[classId_x-1]} @ {conf_x}'
                ,(box_x[0], box_x[1]-10)
                , cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0,255,0), 2
                );

cv2.imshow("capture termoformado", frame)
key = cv2.waitKey(0)

# if key == ord('q'):
#     break

video.release()
cv2.destroyAllWindows()
