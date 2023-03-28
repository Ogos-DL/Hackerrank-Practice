# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 13:05:16 2023

@author: augus
"""
def solve(s):
        s = s.split(" ")
        return ' '.join([j.capitalize() for j in s])

s = input()
print(solve(s))