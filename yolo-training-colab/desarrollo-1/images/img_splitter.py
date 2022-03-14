import os
import shutil
from shutil import copyfile
import random

print("-\n--\n---\n----\n-----\n----\n---\n--\n-\n")

inputDirName = 'oxxo_images_renamed'
trainRatio = 0.80
validRatio = 0.15
outputDirName = 'datasets'


if not os.path.exists(outputDirName):
    os.makedirs(outputDirName)
else:
    shutil.rmtree(outputDirName)

fileList = os.listdir(inputDirName)
filesQnt = len(fileList)

if filesQnt == 0:
    print(f'{inputDirName}/  is empty')

trainDir = f'{outputDirName}/train'
validDir = f'{outputDirName}/valid'
testDir = f'{outputDirName}/test'

trainCounter = 0
validCounter = 0
testCounter = 0

if not os.path.exists(trainDir):
    os.makedirs(trainDir)

if not os.path.exists(validDir):
    os.makedirs(validDir)

if not os.path.exists(testDir):
    os.makedirs(testDir)


random.shuffle(fileList)

for idx, fileName in enumerate(fileList):
    if fileName.endswith('.jpg'):
        relPosition = idx/filesQnt
        print(idx,' ',filesQnt,' ',relPosition)
        if relPosition<trainRatio:
            print('Train')
            trainCounter += 1;
        if trainRatio <= relPosition < (trainRatio+validRatio):
            print('Validation')
            validCounter += 1;
        if (trainRatio+validRatio) <= relPosition:
            print('Test')
            testCounter += 1;

print('\n----\n')
print(f'trainCounter = {trainCounter}')
print(f'validCounter = {validCounter}')
print(f'testCounter = {testCounter}')



