# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:10:37 2023

@author: augus
"""

from collections import OrderedDict

n = int(input())

words = [input() for i in range(n)] 

counts = OrderedDict()

for word in words:
    counts[word] = counts.get(word,0) + 1
    
print(len(counts.keys()))
print(" ".join(map(str,counts.values())))