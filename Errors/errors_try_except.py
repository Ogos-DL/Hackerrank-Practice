# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:18:39 2023

@author: augus
"""



for i in range(int(input())):
    a,b = input().split()
    try:
        a, b = int(a), int(b)
        div = a // b
    except (ZeroDivisionError,ValueError) as e:
        print("Error Code:",e)
    else:
        print(div)