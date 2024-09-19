# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:11:24 2023

@author: camtr
"""
import re

msg = "Num 309-438-0000. My cell is 224-111-2222. My Chicago office: 312-111-2222"

phoneNumberRE = r"(?P<areaCode>\d{3})-(?P<branchID>\d\d\d)-(?P<lineID>\d\d\d\d)"
phoneNumberREObj = re.compile(phoneNumberRE)
# matchList = phoneNumberREObj.findall(msg)

# for match in matchList:
#     print("A phone number found: " + match)

    
matchObj = phoneNumberREObj.search(msg)
while matchObj != None:
    matchStr = matchObj.group()
    print(matchObj.group())
    index = msg.find(matchStr)
    #if len(msg) - index + len(matchStr) >=12:
    matchObj = phoneNumberREObj.search(msg[index+len(matchStr) :])

print("Done")