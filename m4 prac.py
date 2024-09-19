# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:39:38 2023

@author: camtr
"""

stuRecords = {'Alice' : ('A', 'B', 'A', 'B'),  
              'Bob' : ('A', 'B', 'C', 'B'), 
              'Cindy' : ('A', 'B', 'A', 'A'),
              'Dan' : ('A', 'B', 'B', 'B')}

#Ex; Dictionary key loop to check connected values (grades)
selectedStuList = [key for key,  value in stuRecords.items() if value.count('A') >= 2]
print(selectedStuList)

print(r"I'm \t Cindy")# the 'r' before the "" means raw string,  
                      # this will not be modified by \ operators such as \t