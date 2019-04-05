# -*- coding: utf-8 -*-
# anaconda2/python2.7
"""
    Compute annual $amount on svings
    invested at f_interest over i_years
    variables:
        i_years = durations of investment
        f_interest = interest rate
        f_iniInest = initial investment
"""
#import numpy

#==================================================
#               define variables
#==================================================
i_years =30
f_interest = 0.1
f_iniInvest= 1e4



#==================================================
#               do computation- savings
#==================================================
def annual_return(f_iniInvest, f_interest, i_years ):
    currInvest = f_iniInvest
    for i in range( i_years):
        fgrowth = f_interest * currInvest
        print( 'Year', i+1, 'savings', currInvest, 'interest per year', fgrowth )
        currInvest += fgrowth
    return currInvest
# add a function call
annual_return( f_iniInvest, f_interest, i_years)