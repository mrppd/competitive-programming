# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:09:21 2024

@author: pronaya
"""

def gcd(a,b):
     
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd(b, a%b)

def get_gcd_array(p_a):
    res = True
    prev_gcd = -1
    for i in range(len(p_a)-1):
        gcd_v = gcd(p_a[i], p_a[i+1])     
        if prev_gcd>gcd_v:
            res = False
            break
        prev_gcd = gcd_v
    return res

tcase = int(input())
while(tcase):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    
    res = False
    rem_ind = -1
    temp_gcd = -1
    for i in range(n-1):
        gcd_v = gcd(a[i], a[i+1])
        
        if len(a)>=1:
            if temp_gcd>gcd_v:
                rem_ind = i
                break
            
        temp_gcd=gcd_v

    if rem_ind == -1:
        print("YES")
        tcase -= 1
        continue
    
    p_a1 = a.copy()
    p_a2 = a.copy()
    p_a3 = a.copy()
    if rem_ind>0:
        p_a1.pop(rem_ind-1)
    p_a2.pop(rem_ind)
    if rem_ind<n-1:
        p_a3.pop(rem_ind+1)
        
    # print( get_gcd_array(p_a1))
    # print( get_gcd_array(p_a2))
    # print( get_gcd_array(p_a3))
    
    if get_gcd_array(p_a1) or get_gcd_array(p_a2) or get_gcd_array(p_a3):
        print("YES")
    else:
        print("NO")
        
    tcase -= 1
        
    
