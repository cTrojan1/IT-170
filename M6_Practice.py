# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:11:13 2023

@author: camtr
"""
from pathlib import Path
import sys
import os

# print(sys.platform)

print(Path.cwd())
# os.chdir(". .")
# print(Path.cwd())
# os.makedirs(Path.cwd()/Path("newProject"))

# print(os.listdir(Path.cwd()))
# print(os.path.getsize(Path.cwd()))

# p = Path.cwd("numbers.txt")
# print(p.read_text())
# p.write_text("This was added through M6_Practice")
stuRecord = open("stuRecord.txt")
stuRecordList = stuRecord.readlines()
stuRecordDict = {}

for stuRecord in stuRecordList:
    print(stuRecord)


# File to dictionary of average scores
for stuRecord in stuRecordList:
    if "\n" in stuRecord:
        stuRecordStr = stuRecord[:-1]
    else: 
        stuRecordStr = stuRecord
    stuList = stuRecordStr.split()
    stuRecordDict[stuList[0]] = (int(stuList[1]) + int(stuList[2]))/2
print(stuRecordDict)
    
# Writes the formatted dictionary to a new file
stuFinalRecordFile = open("stuFinalRecord.txt", "a")
for name, value in stuRecordDict.items():
    stuFinalRecordFile.write(f"{name} has {value}.\n")
stuFinalRecordFile.close()