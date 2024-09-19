# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:39:36 2023

@author: camtr
"""

stuGradList = [["Alice", 90, 88, 78, 80, 87, 92],
                ["Bob", 70, 65, 88, 85, 79, 84],
                ["Cindy", 95, 80, 90, 100, 84, 95],
                ["Dan", 90, 90, 80, 78, 85, 82],
                ["Ellen", 85, 90, 80, 78, 85, 82]]

# stuGradList.append(["Frank", 75, 80, 80, 98, 85, 87])

# print(stuGradList)

# for stuEntry in stuGradList:
#     stuName, *gradeList = stuEntry
#     print("{0}'s final is {1}".format(stuName, gradeList[-1]))

# for idx in range(len(stuGradList)):
#     print(stuGradList[idx])
#     for i in range (len(stuGradList[idx])):
#         print(stuGradList[idx][i])
    
# newList = stuGradList[-3:-5:-1]
# for item in newList:
#     print(item)

# for index, item in enumerate(stuGradList):
#     print("The student record {1} has index {0}".format(index, item))
    
# stuNameList = ["Alice", "Bob", "Cindy"]
# quiz1 = [90, 70, 95]
# quiz2 = [88, 65, 80]

# partialRecord = zip(stuNameList, quiz1, quiz2)
# print(list(partialRecord))

name, *grade = zip(*stuGradList)
print(name)
# print(*quizzes)
print(grade)

stuGradDict = {}

for key, value in zip(name, grade):
    stuGradDict[key] = value
    
print(stuGradDict)
    