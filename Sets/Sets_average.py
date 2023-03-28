# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 09:30:31 2023

@author: augus
"""

def average(array):
    # your code goes here
    sum_distinct = sum(set(array))
    count_distinct = len(set(array))
    average = round(sum_distinct / count_distinct, 3)
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)   
    print(result)