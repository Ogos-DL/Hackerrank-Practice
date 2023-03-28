# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:20:02 2023

@author: augus
"""

n = int(input())
s = set(map(int,input().split()))
N = int(input())

for i in range(N):
    #pop, remove and/or discard
    command = input().split()
    try:
        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            s.remove(int(command[1]))
        elif command[0] == "discard":
            s.discard(int(command[1]))
    except:
        pass
        
print(sum(s))