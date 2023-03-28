# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:55:32 2023

@author: augus
"""

from itertools import groupby

S = [*input()]


for k, g  in groupby(S):
    print(f"({len(list(g))}, {str(k)})", end = " ")