# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:21:39 2024

@author: pronaya
"""

n = int(input())

XY = list(map(int, input().split()))
XY_m = XY.copy()

track = []

def find(C, XY, XY_m):
    global track
    if C == XY:
        return True
    if XY_m == C:
        return False
    if C[0]<-50 or C[0]>50 or C[1]<-50 or C[1]>50:
        return False
    
    if(C in track):
        return False
        
   
    track.append(C)
    find([C[0], C[1]+1], [XY[0], XY[1]], XY_m)
    find([C[0]+1, C[1]+1], [XY[0], XY[1]], XY_m)
    find([C[0]+1, C[1]], [XY[0], XY[1]], XY_m)
    find([C[0]+1, C[1]-1], [XY[0], XY[1]], XY_m)
    find([C[0], C[1]-1], [XY[0], XY[1]], XY_m)
    find([C[0]-1, C[1]-1], [XY[0], XY[1]], XY_m)
    find([C[0]-1, C[1]], [XY[0], XY[1]], XY_m)
    find([C[0]-1, C[1]+1], [XY[0], XY[1]], XY_m)
    
    
    
print(find([49,0], XY, XY_m))