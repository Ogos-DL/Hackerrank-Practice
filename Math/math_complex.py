# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:03:38 2023

@author: augus
"""
import cmath

#Input complex number on format "1+2j"
n = input()

n_comp = complex(n)
#print(n_comp.real,n_comp.imag)

print(abs(n_comp))
print(cmath.phase(n_comp))