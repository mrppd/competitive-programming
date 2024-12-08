# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:06:07 2024

@author: prona
"""


tcase = int(input())
while(tcase):
    tmp_a = list(map(int, input().split()))
    n = tmp_a[0]
    k = tmp_a[1]
    
    med_no  = int(n/2)
    if k+med_no>n or k-med_no<1:
        print(-1)
    else:
        print(n)
        for i in range(k-med_no, k):
            print(i, end=' ')
            
        for j in range(k, k+med_no+1):
            print(j, end=' ')
        print('')   
    tcase -= 1