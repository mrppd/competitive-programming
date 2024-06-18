# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:58:31 2024

@author: pronaya
"""



tcase = int(input())
while(tcase):
    n = list(map(int, input().split())) 
    a = min(n[0], n[1])
    b = max(n[0], n[1])
    c = min(n[2], n[3])
    d = max(n[2], n[3])
    
    updw1 = 0 
    updw2 = 0
    
    if(c>a and c<b):
        updw1 = 1
    else:
        updw1 = -1 
    
    if(d>a and d<b):
        updw2 = 1
    else:
        updw2 = -1
     
    #print(updw1, updw2)
        
    if(updw1==updw2):
        print("NO")
    else:
        print("YES")
        
        
    tcase -= 1