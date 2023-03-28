# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:46:06 2023

@author: augus
"""

import calendar

week_list = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

date = list(map(int,input().split()))

result = calendar.weekday(year = date[-1],month = date[0], day = date[1])

print(week_list[result])



