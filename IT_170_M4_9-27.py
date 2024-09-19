# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 16:32:20 2023

@author: camtr
"""

strList = ["a", "go", 'car', 'door', 'string']
newList = [item for item in strList if len (item) <= 2] # strList if 'r' in item]
print(newList)

stuRecords = [['Alice', ('A', 'B', 'A')], ['Bob', ('A', 'C', 'A')], ['Cindy', ('B', 'C', 'C')]]
nameWithTwoAs = [stu[0] for stu in stuRecords if stu[1].count('A')>=2] #S's means grades