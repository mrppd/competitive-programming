# -*- coding: utf-8 -*-
"""
Created on Thu May 23 01:30:10 2024

@author: pronaya
"""

#starting again 

tcase = int(input())
while(tcase):
    nop = int(input())
    al = []
    bl = []
    al = list(map(int,input().split()))
    bl = list(map(int,input().split()))
    # for i in range(nop):
    #     a = int(input())
    #     al.append(a)
    # for j in range(nop):
    #     b = int(input())
    #     bl.append(b)        

    count = 0
    i = 0
    while i<nop:
        # print(al)
        # print(bl)    
        if(al[i]>bl[i]):
            for j in range(nop-2, i-1, -1):
                al[j+1]=al[j]
            al[i]=bl[i]
            count += 1
        i += 1
    print(count)
    tcase -= 1
 

 
    
 
    
 
    
 
