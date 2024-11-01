# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:40:24 2024

@author: prona
"""


tcase = int(input())
while(tcase):
    n = int(input())
    tmp_a = list(map(int, input().split()))
    arr_a = []
    k = 0
    se_k = 0
    p = 0
    q = 0
    for i in range(n-1):
        dif = abs(tmp_a[i+1]-tmp_a[i])
        arr_a.append(dif)
        if dif>k:
            k=dif
            p=i
            q=i+1
            
    arr_a.sort(reverse=True)
    
    mid = int(abs(tmp_a[p]+tmp_a[q])/2)
    kk = min(abs(mid-tmp_a[p]), abs(mid-tmp_a[q]))       
    print(p, q, k, kk)
    if n>2:
        print(max(kk, arr_a[1]))
    elif n==1:
        print(1)
    else:
        print(max(abs(mid-tmp_a[p]), abs(mid-tmp_a[q])))
        
    
    tcase -= 1   