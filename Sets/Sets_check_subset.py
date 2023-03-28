# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:17:48 2023

@author: augus
"""

T = int(input())
A = set(map(int,input().split()))

for i in range(T):
    
    n_A = int(input())
        
    n_A = int(input())
    B = set(map(int,input().split()))
    
    if A.intersection(B) == A:
        print(True)
    else:
        print(False)