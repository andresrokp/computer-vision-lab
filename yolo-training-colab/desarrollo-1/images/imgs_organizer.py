import os
import random
from shutil import copyfile
import shutil

print("-\n--\n---\n----\n-----\n----\n---\n--\n-\n")

dirName = "oxxo_images"
className = "Oxxo"

counter = 0;
fileNameList = os.listdir(dirName);
# print("fileNameList : ",fileNameList)
newFolderName = dirName + "_renamed";

if not os.path.exists(newFolderName):
    os.makedirs(newFolderName);
    print("created");
else:
    shutil.rmtree(newFolderName);
    print("cleared");

for fileName in fileNameList:
    if fileName.endswith(".jpg"):
        counter+=1;
        newFileName = f'{className}_{counter}.jpg';
        print(newFileName)
        copyfile(os.path.join(dirName,fileName) , os.path.join(newFolderName, newFileName));

print("Total copied and renamed files: ", counter)