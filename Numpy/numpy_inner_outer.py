# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:42:23 2023

@author: augus
"""

import numpy as np

A = np.array(list(map(int,input().split())))
B = np.array(list(map(int,input().split())))

print(np.inner(A,B))
print(np.outer(A,B))
