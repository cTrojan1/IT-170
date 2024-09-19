# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:12:03 2023

@author: camtr
"""

from Module_B import *

msg = "I am Module_A"

def showMe():
    print(msg)
    
def sayHello():
    print("I am Module_A,  glad to be imported")
    
if __name__ == "__main__":
    print("Module_A is executed by itself")
    showMe()
    
else:
    print("Module_A is imported")
    sayHello()
    