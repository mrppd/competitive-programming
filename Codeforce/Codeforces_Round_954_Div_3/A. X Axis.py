# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 16:35:08 2024

@author: pronaya
"""

tcase = int(input())


while(tcase):
    
    x = list(map(int, input().split()))
    
    small_a = 9999999999
    min_f_a = 9999999999
    for a in x:
        f_a = abs(x[0]-a)+abs(x[1]-a)+abs(x[2]-a)
        if(f_a<min_f_a):
            min_f_a = f_a
            small_a = a
    
    print(small_a)
    
    tcase -= 1