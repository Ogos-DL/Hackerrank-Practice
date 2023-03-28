# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:54:52 2023

@author: augus
"""

from collections import OrderedDict

ordered_dictionary = OrderedDict()

n = int(input())
item_list = []

for i in range(n):
    item_list = list(map(str,input().split()))
    price = int(item_list[-1])
    item_list.pop()
    item_name = " ".join(item_list)
    if item_name not in ordered_dictionary.keys():
                ordered_dictionary[item_name] = price
    else:
                ordered_dictionary[item_name] +=price
    
[print(k,v) for k,v in ordered_dictionary.items()]