# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:29:56 2023

@author: augus
"""
N = int(input())
L = list(map(int,input().split()))


print(all(i > 0 for i in L) and any(str(i) == str(i)[::-1] for i in L))


   