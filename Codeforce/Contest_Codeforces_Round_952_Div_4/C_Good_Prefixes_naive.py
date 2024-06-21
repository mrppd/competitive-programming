# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:23:01 2024

@author: prona
"""


# def isGood(a, n):
#     for i in range(n):
#         tmp_a = a[i]
#         a[i] = 0
#         if(sum(a)==tmp_a):
#             return 1
#         a[i] = tmp_a
#     else:
#         return 0

tcase = int(input())
while(tcase):
    n = int(input())
    
    a = list(map(int, input().split()))
 
    cnt = 0    
    for i in range(n):
        for j in range(i+1):
            tmp_a = a[j]
            a[j] = 0
            if(sum(a[0:i+1])==tmp_a):
                cnt += 1
                a[j] = tmp_a
                break
            a[j] = tmp_a
        #if(isGood(a[0:i+1], i+1)):
            #cnt += 1
    
    print(cnt)
    
    tcase -= 1