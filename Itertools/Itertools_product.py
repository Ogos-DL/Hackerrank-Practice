# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:23:57 2023

@author: augus
"""

from itertools import product
    
A = list(map(int,input().split()))
B = list(map(int,input().split()))
    
    #print as space separated values
    
print(*product(A, B))
