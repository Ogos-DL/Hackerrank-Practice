# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:27:08 2023

@author: augus
"""

from collections import deque

n = int(input())
d = deque()

for i in range(n):
    command = input().split()
    try:
        if command[0] == "pop":
            d.pop()
        elif command[0] == "popleft":
            d.popleft()
        elif command[0] == "append":
            d.append(int(command[1]))
        elif command[0] == "appendleft":
            d.appendleft(int(command[1]))
    except:
        pass
    
print(" ".join(map(str,d)))