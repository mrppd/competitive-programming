# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:14:34 2024

@author: pronaya
"""


tcase = int(input())

nb = [[0, 1], [0, -1], [-1, 0], [1, 0]] #, [-1, -1], [-1, 1], [1, -1], [1, 1]

while(tcase):
    
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    
    a = []
    
    for i in range(n):
        ak = list(map(int, input().split()))
        a.append(ak)
    

    while(1):
        change = 1
        for i in range(n):
            for j in range(m):
                gr = 1
                mx_nb = -1
                for k in range(4):
                    ni = i+nb[k][0]
                    nj = j+nb[k][1]
                    if(ni>=0 and nj>=0 and ni<n and nj<m):
                        mx_nb = max(mx_nb, a[ni][nj])
                        if (a[i][j]<=a[ni][nj]):
                            #print(a[i, j])
                            wh = a[ni][nj]
                            gr = 0
                            break
                if(gr):
                    a[i][j] = min(mx_nb, a[i][j])
                    change = 0
                    break
            if(change==0):
                break
        
        if(change):
            break
                    
            
    for i in range(n):
        for j in range(m):
            if(j+1==m):
                print(a[i][j], end="")
            else:
                print(a[i][j], end=" ")
        
        print('')
            
 
    #print(a)
    
    
    tcase -= 1
    
