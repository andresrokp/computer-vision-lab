import os
import myvars
import cv2
import time


print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

path = os.fsencode(myvars.picspath)
print(f'path: {path}')
    
for file in os.listdir(path):
     filename = os.fsdecode(file)
     print('filename: ',filename)
     pic = cv2.imread(f'{myvars.picspath}{filename}')
     cv2.imshow(f'{filename}', pic)

key = cv2.waitKey(0)