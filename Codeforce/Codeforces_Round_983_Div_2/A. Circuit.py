# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:35:36 2024

@author: pronaya
"""


tcase = int(input())
while(tcase):
    n = int(input())
    tmp_a = list(map(int, input().split()))
    
    #print(tmp_a)
    
    on_sw = sum(tmp_a)
    off_sw = 2*n - on_sw
    
    #Finding max
    on_max = 0
    if(on_sw>=off_sw):
        on_max += off_sw
    else:
        on_max += on_sw
        
    #Finding min
    on_min = 0
    on_min = n - (int(off_sw/2) + int(on_sw/2))
    
    
    print(on_min, on_max)

    tcase -= 1