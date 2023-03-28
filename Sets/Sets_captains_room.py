# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:56:31 2023

@author: augus
"""

from collections import Counter

K = int(input())
room_nmbrs = list(map(int,input().split()))

s = Counter(room_nmbrs)

value = [i for i in s if s[i]==1]

print(value[0])