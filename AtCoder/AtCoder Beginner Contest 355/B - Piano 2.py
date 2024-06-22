# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:04:50 2024

@author: pronaya
"""

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A + B
C.sort()

res = 0
for i in range(len(C)-1):
    if(C[i] in A and C[i+1] in A ):
        res = 1


if(res):
    print("Yes")
else:
    print("No")
        
        
        

