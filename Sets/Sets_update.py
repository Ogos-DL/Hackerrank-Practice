# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:44:07 2023

@author: augus
"""

e = int(input())
A = set(map(int,(input().split())))
N = int(input())

for i in range(N):
    #intersection_update,  symmetric_difference_update difference_update
    command = input().split()
    B = set(map(int,(input().split())))
    try:
        if command[0] == "intersection_update":
            A.intersection_update(B)
        elif command[0] == "symmetric_difference_update":
            A.symmetric_difference_update(B)
        elif command[0] == "difference_update":
            A.difference_update(B)
        elif command[0] == "update":
            A.update(B)
    except:
        pass
        
print(sum(A))