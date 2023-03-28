# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:40:10 2023

@author: augus
"""

import numpy as np

def list_into_array_reshape(list_arr):

    
    list_arr_int = [eval(i) for i in list_arr]
    array_arr = np.array(list_arr_int)
    
    return np.reshape(array_arr,(3,3))


arr = input().strip().split(' ')  
result = list_into_array_reshape(arr)
print(result)
