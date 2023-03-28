# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:40:17 2023

@author: augus
"""

def print_formatted(number):
    # your code goes here
    pad = len(bin(number)[2:])
    for i in range(1,number+1):
        dec = str(i).rjust(pad, " ")
        octal = str(oct(i)[2:]).rjust(pad, " ")
        hexa = str(hex(i)[2:]).upper().rjust(pad, " ")
        binary = str(bin(i)[2:]).rjust(pad, " ")
        print(dec,octal,hexa,binary)
if __name__ == '__main__':
    n = int(input())    
    print_formatted(n)