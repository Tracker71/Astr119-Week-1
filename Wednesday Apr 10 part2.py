# -*- coding: utf-8 -*-
"""

1) create synthetic well pressure time series
2) compute

"""
import numpy as np
import matplotlib.pyplot as plt



#=======================================================================
#           parameters
#=======================================================================
iWell = 10
iMeas = 12

#=======================================================================
#           create synthetic
#=======================================================================
a_mu_syn = np.random.random_integers( 20, 40, iWell)
a_std_syn= np.random.random_integers( 1, 10, iWell)*.1

m_Data = np.array( [])
for i in range ( iWell):
    if i == 0:
        m_Data = a_mu_syn[i] + a_std_syn[i]*np.random.random( iMeas)
    else:
        m_Data = np.vstack((m_Data, a_mu_syn[i] + a_std_syn[i]*np.random.random( iMeas)))

print( m_Data.mean( axis = 1))
print( m_Data.std( axis= 1))
#=======================================================================
#           statistics
#=======================================================================
a_mean = np.dot( m_Data, np.ones( iMeas, dtype = float).reshape(iMeas))     
#test code performance
print( 'syn results', np.round( a_mu_syn, 2))
print( 'comp means', np.round( a_mean.flatten(),2))
