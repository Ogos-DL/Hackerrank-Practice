# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:49:47 2023

@author: augus
"""

n,m = map(int,input().split())
array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happiness = 0

for i in array:
    if i in A:
        happiness += 1
    if i in B:
        happiness += -1 
print(happiness)
        