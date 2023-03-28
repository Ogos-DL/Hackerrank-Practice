# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:37:25 2023

@author: augus
"""

from itertools import combinations

n,m = input().split()   

list_n = [*n]
list_n.sort()

for i in range(1,int(m)+1):
    comb = list(combinations(list_n,i))

    [print("".join(j)) for j in comb]