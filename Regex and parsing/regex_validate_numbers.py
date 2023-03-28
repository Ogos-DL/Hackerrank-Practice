# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:56:49 2023

@author: augus
"""
import re

N = int(input())
regex = r"^[789][0-9]{9}$"
for i in range(N):
    m = re.match(regex,input())
    if m:
        print("YES")
    else:
        print("NO")