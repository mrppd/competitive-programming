# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:23:01 2024

@author: pronaya
"""


def isGood(a, n, sum_p, max_e):
    
    sum_p = sum_p + a[-1]
    max_e = max(max_e, a[-1])
    if((sum_p-max_e) == max_e):
        return 1, sum_p, max_e
        
    # for i in range(n):
    #     tmp_a = a[i]
    #     a[i] = 0
        
    #     par_sum = 0
    #     for j in range(n):
    #     if(sum(a)==tmp_a):
    #         return 1
    #     a[i] = tmp_a

    return 0, sum_p, max_e

tcase = int(input())
while(tcase):
    n = int(input())
    
    a = list(map(int, input().split()))
 
    cnt = 0    
    sum_p = 0
    max_e = 0
    for i in range(n):
        #res,sum_p, max_e = isGood(a[0:i+1], i+1, sum_p, max_e)
        sum_p += a[i]
        max_e = max(max_e, a[i])
        if((sum_p-max_e) == max_e):
            cnt += 1
    
    print(cnt)
    
    tcase -= 1