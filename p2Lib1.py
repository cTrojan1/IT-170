# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:47:49 2023

@author: camtr
"""
import math

def sumList(dList):
    Sum = sum(dList)
    return Sum

def meanList(dList, sumList):
    mean = sumList/len(dList)
    return mean

def minMaxList(dList):
    Max = max(dList)
    Min = min(dList)
    return Min, Max
    
def stdevList(dList):
    mean_value = meanList(dList, sumList(dList))
    variance = sum((x - mean_value) ** 2 for x in dList) / len(dList)
    return math.sqrt(variance)
