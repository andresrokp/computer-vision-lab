import os
import myvars

path = os.fsencode(myvars.picspath)
print(f'{path}')
    
for file in os.listdir(path):
     filename = os.fsdecode(file)
     print(filename)