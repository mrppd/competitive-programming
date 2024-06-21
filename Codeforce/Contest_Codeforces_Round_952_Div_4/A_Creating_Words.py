# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:26:27 2024

@author: pronaya
"""

tcase = int(input())
while(tcase):
    x = input()
    inp = x.split()
    list_inp1 = list(inp[0])
    list_inp2 = list(inp[1])
    tmp = list_inp1[0]
    list_inp1[0]= list_inp2[0]
    list_inp2[0] = tmp
    
    print(''.join(list_inp1), ''.join(list_inp2))
    tcase -= 1
