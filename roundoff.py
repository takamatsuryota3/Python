# -*- coding: utf-8 -*-
import math

def my_round(x, d=0):
    p = 10 ** d
    return float(math.floor((x * p) + math.copysign(0.5, x)))/p


x = 3.54

x = my_round(x, 1)
    
print(x) # 1.2import math