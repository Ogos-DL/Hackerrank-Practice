# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:37:17 2023

@author: augus
"""

import numpy as np

N,M = map(int,input().split())

array_N = np.array([list(map(int,input().split())) for i in range(N)])

print(np.mean(array_N, axis = 1))
print(np.var(array_N, axis = 0))
print(np.around(np.std(array_N, axis = None),decimals = 11))