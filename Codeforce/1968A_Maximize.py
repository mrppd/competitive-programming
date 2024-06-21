# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:46:24 2024

@author: pronaya
"""

#starting again 


def gcd(a,b):
     
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a%b)


tcase = int(input())
while(tcase):
    x = int(input())
    
    y = 1
    sol = 0
    res_y = 1
    while (y<x):
        tmp_sol = gcd(x, y) + y
        #print('-', y, tmp_sol)
        if(tmp_sol > sol):
            sol = tmp_sol
            res_y = y
        y += 1
    
    print(res_y)
    tcase -= 1