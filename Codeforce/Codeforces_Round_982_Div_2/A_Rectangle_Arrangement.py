# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:23:52 2024

@author: prona
"""

tcase = int(input())
while(tcase):
    n = int(input())
    #a=[]
    x = 0
    y = 0
    for i in range(n):
        tmp_a = list(map(int, input().split()))
        #a.append(tmp_a)
        #print(tmp_a)
        if(x < tmp_a[0]):
            x = tmp_a[0]
        if(y < tmp_a[1]):
            y = tmp_a[1]
            
    print((x+y)*2)
    
    tcase -= 1   