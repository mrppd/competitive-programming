# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:11:20 2024

@author: pronaya
"""
import numpy as np

N = int(input())

n = 3**N
m = 3**N
k = N
karpet = np.ndarray(shape=(n,m), dtype=int)
karpet.fill(0)


def solve(x, y, k):
    if(k==0):
        karpet[x,y]=1
    else:
        l = 3**(k-1)
        solve(x, y, k-1)
        solve(x+l, y, k-1)
        solve(x+2*l, y, k-1)
        
        solve(x, y+l, k-1)
        solve(x+2*l, y+l, k-1)
        
        solve(x, y+2*l, k-1)
        solve(x+l, y+2*l, k-1)
        solve(x+2*l, y+2*l, k-1)


solve(0, 0, k)

for i in range(m):
    for j in range(n):
        if(karpet[i, j]==1):
            print('#', sep='', end='')
        else:
            print('.', sep='', end='')
            
    print('')

