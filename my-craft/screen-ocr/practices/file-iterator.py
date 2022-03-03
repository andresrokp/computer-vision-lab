import os
from turtle import width
import myvars as mv
import cv2
import math
import matplotlib.pyplot as plt

print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

path = os.fsencode(mv.picspath)
print(f'path: {path}')

    
for file in os.listdir(path):
     filename = os.fsdecode(file)
     print('filename: ',filename)
     
     wholeScreen = cv2.imread(f'{mv.picspath}{filename}')
     resized = cv2.resize(wholeScreen, (0,0), fx=0.5, fy=0.5)
     # cv2.imshow('resized', resized)
     
     chunkScreenNumber = wholeScreen[mv.screenNumRange]
     
     cv2.imshow(f'cant ciclos {filename}', chunkScreenNumber)
     # break

key = cv2.waitKey(0)