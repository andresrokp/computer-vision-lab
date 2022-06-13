import os
from shutil import copyfile
import shutil

print("-\n--\n---\n----\n-----\n----\n---\n--\n-\n")

dirName = "a-ton-of-images-i-BEGIN-with"
photoName = "termoCaptura"

counter = 0;
fileNameList = os.listdir(dirName);
# print("fileNameList : ",fileNameList)
newFolderName = dirName + "-now-RENAMED";

if not os.path.exists(newFolderName):
    os.makedirs(newFolderName);
    print("created");
else:
    shutil.rmtree(newFolderName);
    print("cleared");

for fileName in fileNameList:
    if fileName.endswith(".jpg"):
        counter+=1;
        newFileName = f'{photoName}_{counter}.jpg';
        print(newFileName)
        copyfile(os.path.join(dirName,fileName) , os.path.join(newFolderName, newFileName));

print("Total copied and renamed files: ", counter)