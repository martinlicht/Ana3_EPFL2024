#!/usr/bin/python3
"""
Description: Display a Fourier series
"""

from common import *
# Import math Library
import math 

x_min, x_max = -2, 2
y_min, y_max = -2, 2

T = 1

M = 1000 # partitionsfeinheit 
h = (x_max - x_min)/M

xs = [ x_min + i * h for i in range(0,M+1) ]
ys = [ x_min + i * h for i in range(0,M+1)  ]





def get_coefficients_squarewave( counter ):
    a_0 = 0
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        a[m] = 0 
        if n % 2 == 0 : continue
        b[m] = 4 / math.pi * 1/(n)
    return a_0, a, b

def get_coefficients_sawtooth( counter ):
    a_0 = 0.5
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        a[m] = 0 
        b[m] = -1/(math.pi*(n))
    return a_0, a, b

def get_coefficients_triangle( counter ):
    a_0 = 1 / 2
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        if n % 2 == 0 : continue
        a[m] = -4 / ( math.pi * math.pi * n*n) 
        b[m] = 0
    return a_0, a, b

def get_coefficients_diraccomb( counter ):
    a_0 = 0
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        a[m] = 1. / ( math.pi ) 
        b[m] = 0
    return a_0, a, b

def get_coefficients_exercise1( counter ):
    a_0 = 0
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        if n == 1 or n % 2 == 0: continue
        a[m] = 0.
        b[m] = 1. / ( n*n ) 
    return a_0, a, b

def get_coefficients_exercise2( counter ):
    a_0 = 0
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        if n % 2 == 0: continue
        a[m] = (-1.)**((n+1)/2) / ( n*n*n ) 
        b[m] = 0
    return a_0, a, b

def get_coefficients_exercise3( counter ):
    a_0 = 0
    a = [ 0 for m in range(0,counter) ]
    b = [ 0 for m in range(0,counter) ]
    for m in range(0,counter):
        n = m+1
        a[m] = (-1.)**(n+1) / ( n*n ) 
        b[m] = 0
    return a_0, a, b




plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)

N = 60
counter = 0
while counter < N:
    
    a_0, a, b = get_coefficients_sawtooth( counter )
    a_0, a, b = get_coefficients_squarewave( counter )
    a_0, a, b = get_coefficients_triangle( counter )
    a_0, a, b = get_coefficients_exercise3( counter )
    a_0, a, b = get_coefficients_exercise2( counter )
    # a_0, a, b = get_coefficients_diraccomb( counter )

    # print( a_0, a, b )

    for i in range(0,len(ys)):
        value = a_0
        for m in range(0,counter):
            n = m+1
            value = value + a[m] * math.cos( 2 * math.pi * n * xs[i] / T )
            value = value + b[m] * math.sin( 2 * math.pi * n * xs[i] / T )
        ys[i] = value 

    line = plt.plot( xs, ys, color='blue', label='y', visible=True )

    fig = plt.gcf()
    # fig.set_size_inches(16, 9)
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    plt.pause(1.00)
    if counter == 0: plt.pause(5.00)
    plt.title ( "N = {}".format(counter) )

    line.pop(0).remove()

    counter = counter + 1
        
plt.show()
