# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:54:59 2021

@author: Sixteen
"""

def solveMDP(probs ,mR, s1Reward, s4Reward):
    
    ax = 0;
    ay = 0;
    bx = 0;
    by = 0;

    #u,v,w,x=0;
    u=0;
    v=0;
    w=0;
    x=0;
    
    while True:
        pass
    
        ax = probs[0]*(mR+s4Reward)+(1-probs[0])*(mR+max(bx,by));
        ay = (1-probs[1])*(mR+s4Reward)+probs[1]*(mR+max(bx,by));
        bx = (1-probs[0])*(mR+s1Reward)+probs[0]*(mR+max(ax,ay));
        by = probs[1]*(mR+s1Reward)+(1-probs[1])*(mR+max(ax,ay));
        
        if ax-u<0.00001 and ay-v<0.00001 and bx-w<0.00001 and by-x<0.00001:
            break
        
        u = ax;
        v = ay;
        w = bx;
        x = by;
    
    A = [bx,by,ax,ay]
    for x in range (0,4):
        A[x] = round(A[x],6);
    
    return A;

print(solveMDP([0.9, 0.9], -0.1, -1, 1))
    
def solveGD(r, x, e):
   
    temp = x
    n = 0
    
    while True:
        pass
        
        x = x - r*(4*pow(x, 3)+9*pow(x, 2)-40*x+1)
        n = n+1
        
        if x-temp<e:
            break
        temp = x
        
    A = [round(x, 6), n]
    return A


print(solveGD(0.0001, -7, 0.0001))