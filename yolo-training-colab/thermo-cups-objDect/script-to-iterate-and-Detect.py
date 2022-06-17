import cv2
import myvars
import os

print("-\n--\n---\n----\n-----\n------\n-------\n--------\n---------\n----------\n-----------\n------------\n-------------\n--------------\n-------------\n------------\n-----------\n----------\n---------\n--------\n-------\n------\n-----\n----\n---\n--\n-")

classesList = ['monoTapon'];
configFilePath = f'{myvars.resultsPath}/custom-yolov4-detector.cfg';
weightsFilePath = f'{myvars.resultsPath}/custom-yolov4-detector_best.weights';
imgsFilesPath = myvars.imgsPath;

imgFileNamesList = os.listdir(imgsFilesPath)[0:-1];

print(imgFileNamesList);

img = cv2.imread(f'{imgsFilesPath}/CAP-11032022-19-07-17.jpg')

print(img.shape)
cnn = cv2.dnn_DetectionModel(weightsFilePath, configFilePath);
print(cnn)

cnn.setInputSize(447, 797);
cnn.setInputScale(1.0/127.5);
cnn.setInputMean(1);
cnn.setInputSwapRB(True)

classId, confs, boxes = cnn.detect(img, confThreshold=0.3)

print(len(classId))

if len(classId) != 0:
    detectResult = zip(classId.flatten(), confs.flatten(),boxes)
    print(detectResult)


    for classId_x, conf_x, box_x in detectResult:
        print (classId_x, conf_x, box_x)
        cv2.rectangle(img,box_x,color=(0,255,0),thickness=2)
        cv2.putText(img
                    ,f'{classesList[classId_x-1]} @ {conf_x}'
                    ,(box_x[0], box_x[1]-10)
                    , cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0,255,0), 2
                    );
else:
    print("\nx x x NO SE ENCONTRÓ OBJETO x x x\n\n")

cv2.imshow("the image", img)
key = cv2.waitKey(0)

