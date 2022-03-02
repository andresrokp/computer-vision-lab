import os
from turtle import width
import myvars
import cv2
import math

print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

path = os.fsencode(myvars.picspath)
print(f'path: {path}')
    
for file in os.listdir(path):
     filename = os.fsdecode(file)
     print('filename: ',filename)
     pic = cv2.imread(f'{myvars.picspath}{filename}')
     height = pic.shape[0]
     width = pic.shape[1]
     print('width ',width, ' - height ',height)
     genStatus = pic[10:85, 935:1365]
     cv2.imshow(f'{filename}', genStatus)
     # break

key = cv2.waitKey(0)