# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:53:23 2024

@author: pronaya
"""

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]

A = list(map(int, input().split()))

for i in range(N):
    X = list(map(int, input().split()))
    
    for j in range(M):
        A[j] = max(0, A[j]-X[j])
        
if(sum(A)==0):
    print("Yes")
else:
    print("No")