import os
from turtle import width
import myvars
import cv2
import math
import matplotlib.pyplot as plt

print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

path = os.fsencode(myvars.picspath)
print(f'path: {path}')

    
for file in os.listdir(path):
     filename = os.fsdecode(file)
     print('filename: ',filename)
     pic = cv2.imread(f'{myvars.picspath}{filename}')
     resized = cv2.resize(pic, (0,0), fx=0.3, fy=0.3)
     cv2.imshow('resized', resized)
     height = pic.shape[0]
     width = pic.shape[1]
     print('width ',width, ' - height ',height)
     genStatus = pic[10:85, 935:1365]
     cv2.namedWindow(f'gen status {filename}', flags=cv2.WINDOW_GUI_EXPANDED)
     cv2.imshow(f'gen status {filename}', genStatus)
     cantCiclos = genStatus[30:50, 130:207]
     cv2.imshow(f'cant ciclos {filename}', cantCiclos)
     break

key = cv2.waitKey(0)