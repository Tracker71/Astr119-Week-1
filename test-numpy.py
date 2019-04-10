# -*- coding: utf-8 -*-
"""
script that tests numpy functionality

"""
import numpy
N    = 10 #number of elements in vector
start = 1
stop = 10 # stopping value of vector -1
step = 1


aV = numpy.arange( 1, 10, 1)
print( aV)

aV = numpy.arange( start, stop, step)
aV2 = numpy.linspace( start, stop, N, dtype = int)