import os
import shutil
from shutil import copyfile
import random

print("-\n--\n---\n----\n-----\n----\n---\n--\n-\n")

inputDirName = 'oxxo_images_renamed'
trainRatio = 0.85
validationRatio = 0.15
outputDirName = 'datasets'


if not os.path.exists(outputDirName):
    os.makedirs(outputDirName)
else:
    shutil.rmtree(outputDirName)

fileList = os.listdir(inputDirName)
print(len(fileList))

if len(fileList) == 0:
    print(f'{inputDirName}/  is empty')

trainDir = f'{outputDirName}/train'
validDir = f'{outputDirName}/valid'
testDir = f'{outputDirName}/test'

if not os.path.exists(trainDir):
    os.makedirs(trainDir)

if not os.path.exists(validDir):
    os.makedirs(validDir)

if not os.path.exists(testDir):
    os.makedirs(testDir)



