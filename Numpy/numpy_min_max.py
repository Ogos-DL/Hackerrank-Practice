# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:30:36 2023

@author: augus
"""

import numpy as np

N,M = map(int,input().split())

array_N = np.array([list(map(int,input().split())) for i in range(N)])

array_N_MIN = np.min(array_N, axis = 1)

MAX = np.max(array_N_MIN, axis = None)

print(MAX)
