import cv2
import myvars
import os
import iteratorModules as itmd

print("-\n--\n---\n----\n-----\n------\n-------\n--------\n---------\n----------\n-----------\n------------\n-------------\n--------------\n-------------\n------------\n-----------\n----------\n---------\n--------\n-------\n------\n-----\n----\n---\n--\n-")

# Declaración de nombres propios // Input variables declaration
classesList = ['monoTapon'];
configFilePath = f'{myvars.resultsPath}/custom-yolov4-detector.cfg';
weightsFilePath = f'{myvars.resultsPath}/custom-yolov4-detector_best.weights';
imgsFolderPath = myvars.imgsPath; # OJO: a veces toma la carpeta de los Bads

imgFileNamesList = os.listdir(imgsFolderPath)[:-1];

cnn = cv2.dnn_DetectionModel(weightsFilePath, configFilePath);
cnn.setInputSize(447, 797);
cnn.setInputScale(1.0/127.5);
cnn.setInputMean(1);
cnn.setInputSwapRB(True)

for imgName in imgFileNamesList:

    imgPath = f'{imgsFolderPath}/{imgName}';
    print("\n\n",imgName);
    img = cv2.imread(imgPath);
    isGoodShoot = True # itmd.isGoodShoot(img);
    
    if isGoodShoot:
        classId, confs, boxes = cnn.detect(img, confThreshold=0.3);
        if len(classId)!=0: # evitando nulls // avoiding nulls
            bestBoxes = cv2.dnn.NMSBoxes(boxes, confs, 0.3, 0.4)
            print('original\n',classId, confs, boxes)
            for i_bx in bestBoxes:
                print ('a box\n',classId[i_bx], confs[i_bx], boxes[i_bx])
                cv2.rectangle(img,boxes[i_bx],color=(0,255,0),thickness=2)
                cv2.putText(img
                            ,f'mT @ {int(confs[i_bx]*100)}%'
                            ,(boxes[i_bx][0], boxes[i_bx][1]-15)
                            , cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1
                            );
        else:
            print("x x x NO SE ENCONTRÓ OBJETO x x x")
        cv2.imwrite(f'termoYoloDetections/{imgName}', img)

key = cv2.waitKey(0)

