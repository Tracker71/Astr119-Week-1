# -*- coding: utf-8 -*-

"""
while loop
consider object thrown up into the air 
Find maximum height

"""
import numpy as np
import matplotlib.pyplot as plt
v0= 5 #m/s
g = 9.8
n = 2000 # time steps
a_t = np.linspace( 0, 1, n)
#computations
y = v0*a_t - .5*g*a_t**2
print( a_t)
print ( y)
# find max heght in while loop
i=1
# y[-1] last entry in array
while y[i] > y[i-1]:
    largest_height = y[i]
    i += 1
    
    
print( "max. height: %10.2f"%( largest_height))

plt.plot( a_t, y)
plt.show()
#To show graph better type in console "auto", to bring it back to console "inline"