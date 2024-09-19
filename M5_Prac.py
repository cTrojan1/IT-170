# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:47:56 2023

@author: camtr
"""

def saySth (meg):
    print(meg)

# FUNCTION #1

# def add (x, y):
#     print(f"x = {x} ; y = {y}")
#     return x + y

# FUNCTION #2

# def add (x, y = 5, z = 'hello'):
#      result = z + str(x+y)
#      return result


#print(add(20, 3)) func. 1

# Func. 2

#saySth(add(13, 5))
#saySth(add(y = 30, x = 12))

#saySth(add(300, z = "The result is: "))

#FUNCTION #3 (VarArgs)
#1, 3, 5 are tuples 
# A and B are dictionary items because the letters are keys for their values)

# def func(*varPos, **varKey):
#     print(varPos)
#     print(varKey)
    
# func(1, 3, 5, a = 10, b = 20)

#FUNCTION #4
#returns A, B, A, C as tuple in list
#*varPos and **varKey can be named anything

def func(*anything, **goes):
    print(anything)
    print(goes.keys())
    
func('A', 'B', 'A', 'C', a = 10, b = 20)