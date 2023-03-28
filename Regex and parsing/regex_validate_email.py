# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:37:57 2023

@author: augus
"""
import email.utils
import re

N = int(input())

regex = r"^([a-z]+[a-z0-9-_.]*)@([a-z]+)\.([a-z]{1,3})$"

for i in range(N):
    input_data = (input())
    e_mail = email.utils.parseaddr(input_data)[1]
    m = re.match(regex,e_mail)
    if m:
        print(input_data)
    else:
        continue
    
    
#this <is@valid.com>
#this <is_som@radom.stuff>
#this <is_it@valid.com>
#this <_is@notvalid.com>
    

