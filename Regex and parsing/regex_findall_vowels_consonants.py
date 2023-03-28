# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 09:25:40 2023

@author: augus
"""

import re

S = "abaabaabaabaaefEAEOUOIouf"

m = re.findall(r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",S)

if m:
    for i in m:
        print(i)

else:
    print(-1)


#"abaabaabaabaae"
#abaabaabaabaaei
#abaabaabaabaaefEAEOUOIouf
