# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:08:58 2023

@author: augus
"""

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    
    # reset the current values
    defaults = {"even": 0, "odd": 1}
    stream.current = defaults[stream_name]
    
    for _ in range(n):
        print(stream.get_next())



queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

    