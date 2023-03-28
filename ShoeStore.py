# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 12:18:53 2023

@author: augus
"""
from collections import Counter

n_shoes = int(input())
shoe_sizes = map(int, input().split())
n_customers = int(input())

shoe_stock = Counter(shoe_sizes)

shoe_size_list = []
earnings = 0
for i in range(n_customers):
    wanted_size, price = map(int, input().split())
    if shoe_stock.get(wanted_size,0) != 0:
            earnings += price
            shoe_stock[wanted_size] = shoe_stock[wanted_size] - 1

print(earnings)