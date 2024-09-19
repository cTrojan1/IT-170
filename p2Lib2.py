# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:38:24 2023

@author: camtr
"""

import random

def sampling(dList, sampleSize, replace: bool):
    x = 0
    if replace == True:
        while x != 5: # With replacement
            rand = random.choices(dList, k=sampleSize)
            place = sum(map(int, rand))
            hold = place / sampleSize
            x = x+1
            return rand
    
    elif replace == False:
        while x != 5: #Without replacemet
            rand = random.sample(dList, sampleSize)
            place = sum(map(int, rand))
            hold = place / sampleSize
            x = x+1
            return rand