# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:35:39 2023

@author: augus
"""

import numpy as np

N = int(input())

A = np.array([list(map(int,input().split())) for i in range(N)])
B = np.array([list(map(int,input().split())) for i in range(N)])

print(np.dot(A,B))