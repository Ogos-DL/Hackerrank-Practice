# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:06:21 2023

@author: augus
"""

from collections import namedtuple

N, Students ,marks = int(input()),namedtuple("Student",input()),0
for i in range(N):
        marks+=int(Students(*input().split()).MARKS)
print(marks/N)  