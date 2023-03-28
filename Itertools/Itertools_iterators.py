# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:03:04 2023

@author: augus
"""

from itertools import combinations

N = 4 #int(input())
L = "a a c d".split() #input().split()
K = 2 #int(input())



a_occur = 0
x = 0

for i in (combinations(L,K)):
    x += 1
    if "a" in i:
        a_occur += 1

result = a_occur / x

print(round(result,4))
                    