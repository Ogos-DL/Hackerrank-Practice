# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 10:17:10 2023

@author: augus
"""

import numpy as np


A = np.array(list(map(eval,input().split())))

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))


