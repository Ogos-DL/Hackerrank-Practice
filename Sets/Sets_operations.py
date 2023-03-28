# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:29:51 2023

@author: augus
"""

M = int(input())
a = set(map(int,(input().split())))
N = int(input())
b = set(map(int,(input().split())))

c = a.difference(b) 
d = b.difference(a)
e = list(c.union(d))
e.sort()

for i in e:
    print(i)