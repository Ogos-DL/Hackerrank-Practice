# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:35:20 2023

@author: augus
"""

from itertools import permutations

n,m = input().split()

list_n = [*n]
list_n.sort()

perm = list(permutations(list_n,int(m)))

[print("".join(i)) for i in perm]