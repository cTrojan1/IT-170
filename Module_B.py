# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:12:03 2023

@author: camtr
"""

msg = "I am Module_B"

def showMe():
    print(msg)
    
def sayHello():
    print("I am Module_B,  glad to be imported")
    
if __name__ == "__main__":
    print("Module_B is executed by itself")
    showMe()
    
else:
    print("Module_B is imported")
    sayHello()
    