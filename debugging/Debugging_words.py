# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:44:21 2023

@author: augus
"""

N = int(input())
words = input().split()

def score_words(words):
    vowels = ["a","e","i","o","u","y"]
    score = 0
    for word in words:
        count = 0
        for i in word:
            if i in vowels:
                count += 1
                
        if count%2 == 0:
            score += 2
        else:
            score += 1
        
    return score

print(score_words(words))    