# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:06:14 2023

@author: augus
"""

import numpy as np

shape = tuple(map(int,input().split()))
array_zeros = np.zeros(shape, dtype = int)
array_ones = np.ones(shape, dtype = int)

#array_M = np.array([list(map(int,input().split())) for i in range(M)])

print(shape)

print(array_zeros)  

print(array_ones)