# by: andresrokp
# repo: 
# goal: migrate an spreadsheet data from one order to another
# lic: an open crap for anyone to use :)
# gracias

import os
import myvars as mv

print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

with open(f'{mv.textPath}\\pla test','r') as termoFile:
    termoLines = termoFile.readlines()
    name = termoLines[0]
    # date = termoLines
    for line in termoLines[0:-1]:
        data = line.split(': ')[1][0:-1]
        print(data)
