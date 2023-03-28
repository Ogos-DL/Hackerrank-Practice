# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 09:45:39 2023

@author: augus
"""

import numpy as np

N,M,P = map(int,input().split())
array_N = np.array([list(map(int,input().split())) for i in range(N)])
array_M = np.array([list(map(int,input().split())) for i in range(M)])

#print(type(array_M))
#print(type(array_N))

print(np.concatenate((array_N,array_M)))

#print(np.transpose(array))
#print(array.flatten())