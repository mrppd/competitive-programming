# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:01:50 2024

@author: pronaya
"""


tcase = int(input())
while(tcase):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    mx_ = -1
    mn_ = 1000000001
    for i in range(n-1):
        #mx_ = a[i]    
        mx_ = max(a[i], a[i+1])
        mn_ = min(mn_, mx_)
    
    
    print(mn_-1)
    tcase -= 1

