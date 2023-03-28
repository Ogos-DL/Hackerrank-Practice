# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:23:50 2023

@author: augus
"""

A = set(map(int,input().split()))

n = int(input())

check_list = []

for i in range(n):  
    check = False
    s = set(map(int,input().split()))     
    if (s.intersection(A) == s and (len(A) > len(s))):
        check = True
        s = set()
    check_list.append(check)
    
if all(check_list) == True:
    print(True)
else:
    print(False)
    
