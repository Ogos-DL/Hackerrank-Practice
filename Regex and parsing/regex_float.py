# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:12:51 2023

@author: augus
"""

import re

re_check = "^[+-]?[0-9]*\.[0-9]+$"

T = int(input())

for i in range(T):
    if(re.search(re_check,input())): 
        print(True) 
          
    else: 
        print(False)
        
      #  "^[+-]?[0-9]*\.[0-9]+$"
        
    #    '[+-]?[0-9]+\.[0-9]+'