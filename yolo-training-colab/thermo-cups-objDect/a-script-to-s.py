import os
import shutil
from shutil import copyfile
import random

print("-\n--\n---\n----\n-----\n----\n---\n--\n-\n")

inputDirName = 'oxxo_images_renamed'
trainRatio = 0.85
validRatio = 0.10
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
allImgCounter = 1

if not os.path.exists(trainDir):
    os.makedirs(trainDir)

if not os.path.exists(validDir):
    os.makedirs(validDir)

if not os.path.exists(testDir):
    os.makedirs(testDir)


random.shuffle(fileList)

for fileName in fileList:
    print(fileName, end=' ')
    if fileName.endswith('.jpg'):
        relPosition = allImgCounter/((filesQnt-1)/2)  # afr :: keep an aye on the -1 is for the classes.txt file
        print(allImgCounter,' ',relPosition)
        justTheName = fileName.split('.')[0]
        if relPosition<trainRatio:
            print('Train')
            copyfile(os.path.join(inputDirName,justTheName+'.jpg'),os.path.join(trainDir,justTheName+'.jpg'))
            copyfile(os.path.join(inputDirName,justTheName+'.txt'),os.path.join(trainDir,justTheName+'.txt'))
            trainCounter += 1;
        if trainRatio <= relPosition < (trainRatio+validRatio):
            print('Validation')
            copyfile(os.path.join(inputDirName,justTheName+'.jpg'),os.path.join(validDir,justTheName+'.jpg'))
            copyfile(os.path.join(inputDirName,justTheName+'.txt'),os.path.join(validDir,justTheName+'.txt'))
            validCounter += 1;
        if (trainRatio+validRatio) <= relPosition:
            print('Test')
            copyfile(os.path.join(inputDirName,justTheName+'.jpg'),os.path.join(testDir,justTheName+'.jpg'))
            copyfile(os.path.join(inputDirName,justTheName+'.txt'),os.path.join(testDir,justTheName+'.txt'))
            testCounter += 1;
        allImgCounter += 1;

print('\n----\n')
print(f'trainCounter = {trainCounter}')
print(f'validCounter = {validCounter}')
print(f'testCounter = {testCounter}')





