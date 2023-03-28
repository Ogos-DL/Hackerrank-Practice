# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:37:36 2023

@author: augus
"""

from collections import defaultdict

d = defaultdict(list)

n,m = list(map(int,input().split()))
[d["A"].append(input()) for i in range(n)]
[d["B"].append(input()) for i in range(m)]

for i in d['B']:
    if i in d['A']:
        for j in range(len(d['A'])):
            if i == d['A'][j]:
                print(j+1, end = " ")
        print()
    else:
        print(-1)