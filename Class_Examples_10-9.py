# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 15:46:22 2023

@author: camtr
"""

def oneline_func(k):
    return k*2

LambdaDouble = lambda k: k*2

x = 10
y = (oneline_func(x))

print(f"Return from oneline_func(): {y}")

y = LambdaDouble(x)

print(f"Return from LambdaDouble(): {y}")
