# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:55:42 2023

@author: augus
"""

import numpy as np

N = eval(input())

A = np.array([list(map(eval,input().split())) for i in range(N)])

det = np.linalg.det(A)

print(det)