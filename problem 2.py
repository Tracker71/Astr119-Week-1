# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:47:16 2019

@author: Brady
"""

#problem 2
import numpy as np
total = 0 
n = [10, 50, 100, 1000]
for j in list(n):
    for i in range(j+1):
        term = 8./( (4. *i+1.)*(4. *i+3.))
        total = total + term
    
        print("term:" + str(term))
print(total)
print(np.pi-total)

