# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:47:42 2023

@author: camtr
"""
import random

# a = {1,2,3,4,5}
# b = {3,4,5,6,7}
# print(a.union(b)) # adds sets a and b together (a|b)
# print(a.intersection(b)) # adds both sets together only showing what they both have (a&b)
# print(a.difference(b)) # Shows items in a and not b (a-b)

inventoryDict = {
'NetGear' : {'switch' : ['5-Port Gigabit Ethernet Unmanaged Switch:300:4.2','18-Port Gigabit Ethernet Unmanaged Switch:1800:4.3',' 36-Port Gigabit Ethernet Unmanaged Switch:3000:4.2']},
'LinkSys' : {'switch' : ['6-Port Gigabit Ethernet Unmanaged Switch:1200:3.7',' 24-Port Gigabit Ethernet Unmanaged Switch:2200:3.3',' 48-Port Gigabit Ethernet Unmanaged Switch:3200:4.1']},
'D-Link' : {'switch' : ['12-Port Gigabit Ethernet Unmanaged Switch:700:4.1',' 18-Port Gigabit Ethernet Unmanaged Switch:2000:4.9',' 24-Port Gigabit Ethernet Unmanaged Switch:2200:4.3']},
'Buffalo' : {'switch' : ['8-Port Gigabit Ethernet Unmanaged Switch:400:4.3',' 18-Port Gigabit Ethernet Unmanaged Switch:600:4.8',' 36-Port Gigabit Ethernet Unmanaged Switch:1200:4.3']},
'Jupiter' : {'router' : ['2-Port Gigabit manageable router:1200:3.3',' 2-Port Gigabit VoIP router:2000:3.3',' 4-Port Gigabit Enterprise WAN router:200:4.3']}
}

for vendorKey in inventoryDict.keys():
    productionDict = inventoryDict[vendorKey]
    for productKey in productionDict.keys():
        deviceList = productionDict[productKey]
        for device in deviceList:
            itemInfoTuple = device.split(':')
            for itemInfo in itemInfoTuple:
                if "18-Port" in itemInfo[0].split():
                    print(itemInfo)


# for key in inventoryDict.keys():
#     print(inventoryDict[key])
    


# aList = list(range(1, 21))
# print(aList)

# numOfSamples = 5

# for numSample in range(numOfSamples):
#     index = random.randint(0, len(aList)-1)
#     print(aList[index])
    
