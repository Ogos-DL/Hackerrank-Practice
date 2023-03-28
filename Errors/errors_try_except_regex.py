# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 14:37:46 2023

@author: augus
"""

import re

for i in range(int(input())):
    a = input()
    try:
        re.compile(a)
    except re.error:
        print(False)
    else:
        print(True)