# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:26:54 2024

@author: pronaya
"""

NA = list(map(int, input().split()))
N = NA[0]
A = NA[1]
T = list(map(int, input().split()))

clock = 0

for i in range(N):
    if(clock >= T[i]):
        clock += A
        print(clock)
    else:
        clock = T[i] + A 
        print(clock)
        
