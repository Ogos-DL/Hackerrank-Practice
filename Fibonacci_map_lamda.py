# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:28:17 2023

@author: augus
"""

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fibo_list = []
    f = 0
    for i in range (n):
        if i == 0:
            f = 0
        elif i < 3:
            f = 1
        else:
            f = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(f)
    return fibo_list
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))