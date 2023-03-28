# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:16:19 2023

@author: augus
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
rows, width = map(int, input().split())

# Print the pattern having a top triangle
for i in range (0, int (rows / 2)):
    pattern = ".|." * ((2 * i) + 1)
    print (pattern.center (width, '-'))
      
# Print GeeksforGeeks in the center
print ("WELCOME".center (width, '-'))
      
# Print the pattern having 
# an inverted triangle
i = int (rows / 2)
while i > 0:
    pattern = ".|." * ((2 * i) - 1)
    print (pattern.center (width, '-'))
    i = i-1