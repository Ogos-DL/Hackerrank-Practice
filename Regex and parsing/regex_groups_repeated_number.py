# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 18:20:20 2023

@author: augus
"""
import re

S = "..12345678910111213141516171820212223"

m = re.search(r"([a-zA-Z0-9])\1",S)

if m:
    print(m.group(1))

else:
    print(-1)