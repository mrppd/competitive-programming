# -*- coding: utf-8 -*-
"""
Created on Thu May 23 01:30:10 2024

@author: pronaya
"""

#starting again

def toString(List): 
    return ''.join(List) 

def permute(a, l, r, sr): 
    if l == r: 
        if toString(a)!=sr:    
            #print(toString(a))
            return True, toString(a)
        else:
            #print('no')
            return False, sr         
    else: 
        for i in range(l, r): 
            a[l], a[i] = a[i], a[l] 
            ret, ss  = permute(a, l+1, r, sr) 
            a[l], a[i] = a[i], a[l]  # backtrack
            if ret:
                return ret, ss
    
    return False, sr  
    

tcase = int(input())
while(tcase):
    s = input()
    cs = s[0]
    flag = False
    for c in s:
        if cs!=c:
            flag = True
            break
    if flag:        
        ret = permute(list(s), 0, len(s), s)
        #print(ret)
        if(ret[0]):
            print('YES')
            print(ret[1])
        else:
            print('NO')
    else:
        print('NO')

    tcase -= 1
    
