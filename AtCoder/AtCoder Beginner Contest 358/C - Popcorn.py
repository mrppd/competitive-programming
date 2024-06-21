# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:06:36 2024

@author: pronaya
"""

nm = list(map(int, input().split())) 
n = nm[0]
m = nm[1]

fla_flag = [0] * m
stand_flag = [0] * n

sl = []
for i in range(n):
    s = input()
    sl.append(list(s))


def find():
    global fla_flag, stand_flag
    if (sum(fla_flag)==m):
        return 0
    
    tmp_path = 999999999

    for i in range(n):
        if (stand_flag[i]==0):
            fla_flag_prev = fla_flag.copy()
                
            for j in range(m):
                if(sl[i][j]=='o'):
                    fla_flag[j]=1
                        
            stand_flag[i] = 1
            
            tmp_path = min(tmp_path, 1 + find())
            
            stand_flag[i] = 0
        
            fla_flag = fla_flag_prev.copy() 
                    
    return tmp_path



print(find())