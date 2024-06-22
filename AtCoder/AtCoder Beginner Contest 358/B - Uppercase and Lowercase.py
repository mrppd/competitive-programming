# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:44:25 2024

@author: pronaya
"""

s = list(input())

countU = 0
countL = 0

for c in s:
    if(c.isupper()):
        countU += 1
    if(c.islower()):
        countL += 1
        
if(countU > countL):
    s = (''.join(s)).upper()
else:
    s = (''.join(s)).lower()
    
    
print(s)

