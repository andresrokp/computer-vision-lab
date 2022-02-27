import cv2
import myvars


print("-\n--\n---\n----\n-----\n------\n-------\n--------\n---------\n----------\n-----------\n------------\n-------------\n--------------\n-------------\n------------\n-----------\n----------\n---------\n--------\n-------\n------\n-----\n----\n---\n--\n-")

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

img = cv2.imread(myvars.cocoImg)
print(img.shape)
cnn = cv2.dnn_DetectionModel(myvars.weights, myvars.config);
print(cnn)

cnn.setInputSize(447, 797);
# cnn.setInputScale(1.0/127.5);
# cnn.setInputMean((127.5, 127.5, 127.5));
cnn.setInputSwapRB(True)

classId, confs, boxes = cnn.detect(img, confThreshold=0.5)

detectResult = zip(classId.flatten(), confs.flatten(),boxes)
print(detectResult)


for classId_x, conf_x, box_x in detectResult:
    print (classId_x, conf_x, box_x)

cv2.imshow("the image", img)

key = cv2.waitKey(0)


