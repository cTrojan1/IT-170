# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:15:12 2023

@author: camtr
"""

stuRecDict = {"Alice":90, "Bob":92, "Cindy":98}

print(stuRecDict)

for key in stuRecDict.keys():
    #print(key)
    print("{} got {}.".format(key, stuRecDict[key]))
    
for value in stuRecDict.values():
    print(value)
    
for item in stuRecDict.items():
    print(item[0])
    
for key, value in stuRecDict.items():
    print("{} got {}.".format(key, value))
    
