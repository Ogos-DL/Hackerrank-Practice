# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:59:16 2023

@author: augus
"""

N,X = input().split()

N,X = int(N), int(X)

mark_sheet = []

for i in range(X):
    #for j in range(X):
    marks = list(map(eval,input().split()))
    mark_sheet.append(marks)

zip_sheet = list(zip(*mark_sheet))

for i in range(N):
    avg = sum(zip_sheet[i]) / len(zip_sheet[i])
    print(float(avg))
