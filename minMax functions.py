# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:25:15 2023

@author: camtr
"""

aList = [1, 2, 3, 4, 5, 6]

def calcMin(List):
    Min = 10
    for i in List:
        if Min > List[i]:
            Min = List[i]
    return Min

calcMin(aList)