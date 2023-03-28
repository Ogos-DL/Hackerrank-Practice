# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:31:10 2023

@author: augus
"""

thickness = 5

p = "H"


#TOP CONE
for i in range (thickness):
    #pattern = + * ((2 * i) + 1)
    print((p*i).rjust(thickness-1)+p+(p*i).ljust(thickness-1))
        
#Top Pillars
for i in range(thickness+1):
    print((p*thickness).center(thickness*2)+(p*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((p*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((p*thickness).center(thickness*2)+(p*thickness).center(thickness*6))


#BOTTOM CONE
for i in range (thickness):
    print(((p*(thickness-i-1)).rjust(thickness)+p+(p*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))