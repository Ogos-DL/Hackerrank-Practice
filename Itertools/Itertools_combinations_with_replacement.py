# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:46:26 2023

@author: augus
"""

from itertools import combinations_with_replacement

n,m = input().split()

list_n = [*n]
list_n.sort()


comb = list(combinations_with_replacement(list_n,int(m)))

[print("".join(j)) for j in comb]