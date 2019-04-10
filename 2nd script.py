# -*- coding: utf-8 -*-
"""
 - create a list and append squared
   numbers to list
   
"""
lSquares = []
# Loop ovver natural numbers,
# square, add to list
# range( start, stop, increment)
for x in range( 1, 10, 1):
    lSquares.append( x**2)
print( lSquares)
print x
#print( lSquares)
