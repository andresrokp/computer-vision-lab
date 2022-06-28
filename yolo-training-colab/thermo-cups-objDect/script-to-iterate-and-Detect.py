import itertools
import cv2
import myvars
import os

print("-\n--\n---\n----\n-----\n------\n-------\n--------\n---------\n----------\n-----------\n------------\n-------------\n--------------\n-------------\n------------\n-----------\n----------\n---------\n--------\n-------\n------\n-----\n----\n---\n--\n-")

# Declaración de nombres propios // Input variables declaration
classesList = ['monoTapon'];
configFilePath = f'{myvars.resultsPath}/custom-yolov4-detector.cfg';
weightsFilePath = f'{myvars.resultsPath}/custom-yolov4-detector_best.weights';
imgsFilesPath = myvars.imgsPath;

imgFileNamesList = os.listdir(imgsFilesPath)[15:25];

print(imgFileNamesList);

cnn = cv2.dnn_DetectionModel(weightsFilePath, configFilePath);
cnn.setInputSize(447, 797);
cnn.setInputScale(1.0/127.5);
cnn.setInputMean(1);
cnn.setInputSwapRB(True)

for imgName in imgFileNamesList:

    img = cv2.imread(f'{imgsFilesPath}/{imgName}')

    # Config de la Red Neur Conv // Conv Neural Net set up

    # Lanzamiento de la detección // running detection
    classId, confs, boxes = cnn.detect(img, confThreshold=0.3);

    # non maxima supression // non maxima supression
    
    print ("\n\n",imgName);
    if len(classId) != 0: # evitando nulls // avoiding nulls
        bestBoxes = cv2.dnn.NMSBoxes(boxes, confs, 0.3, 0.4)
        detectResult = zip(classId.flatten(), confs.flatten(),boxes)
        
        # Iterando sobre cada resultado // iteratin over each detection
        print('original\n',classId, confs, boxes)
        # ToDo
        # Take a representative length of top left corner
        # some how group by it
        # take the max confidence of each group
        # maybe use the index for reference or mayme assemply anoter matrix
        for i_bx in bestBoxes:
            # print(type(classId_x), type(conf_x), type(box_x),type([classId_x, conf_x, box_x]))
            print ('a box\n',classId[i_bx], confs[i_bx], boxes[i_bx])
            cv2.rectangle(img,boxes[i_bx],color=(0,255,0),thickness=2)
            cv2.putText(img
                        ,f'{classesList[classId[i_bx]]} @ {confs[i_bx]}'
                        ,(boxes[i_bx][0], boxes[i_bx][1]-10)
                        , cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0,255,0), 2
                        );
    else:
        print("x x x NO SE ENCONTRÓ OBJETO x x x")

    cv2.imwrite(f'termoYoloDetections/{imgName}', img)
key = cv2.waitKey(0)

