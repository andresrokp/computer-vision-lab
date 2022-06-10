import os
from turtle import width
import myvars as mv
import cv2
import math
import matplotlib.pyplot as plt
import pytesseract as pts

print("-\n--\n---\n----\n-----\n----\n---\n--\n-")


path = os.fsencode(mv.picspath)
print(f'path: {path}')
pts.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    
for file in os.listdir(path):
     filename = os.fsdecode(file)
     print('\n> filename: ',filename)
     
     wholeScreen = cv2.imread(f'{mv.picspath}/{filename}')
     resized = cv2.resize(wholeScreen, (0,0), fx=0.5, fy=0.5)
     # cv2.imshow('resized', resized)
     
     chunkScreenNumber = wholeScreen[mv.screenNumRange]
     gray = cv2.cvtColor(chunkScreenNumber, cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray, (3, 3), 0)
     # thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]
     thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
     numScreenNumber = pts.image_to_string(chunkScreenNumber).strip()
     print(numScreenNumber)   
     cv2.imshow(f'cant ciclos {filename}', thresh)

     match numScreenNumber:
          case '1103':
               print('Calefacción filas longitudinales')
          case '2003':
               print('Visión general de parámetros de presión')
          case '2002':
               print('Visión general parámetros 3')
          case '2007':
               print('Tracción de lámina')
          case '2301':
               print('Diagramas de actuadores')
          case _:
               print('OTRA PANTALLA')
     
     # break

key = cv2.waitKey(0)