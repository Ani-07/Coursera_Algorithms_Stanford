# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:22:09 2020

@author: Anirudh Raghavan
"""

abcd = 
################################################################


def multi(ac,bd,abcd,n):
    print(ac,bd,abcd,n)
    adbc = abcd - ac - bd
    print(10**n*ac,10**(n/2)*adbc,bd)
    product = 10**n*ac + (10**(n/2))*adbc + bd
    
    return product



def kart(x,y):
    
    x = str(x)
    n = len(x)
    y = str(y)
    m = len(y)
    
    if n > m:
        y = '0'*(n-m) + y
    elif n < m:
        x = '0'*(m-n) + x
    
    e = n//2
        
    a = x[:e]
    b = x[e:]
        
    c = y[:e]
    d = y[e:]
    
    
    a_b = str(int(a)+int(b))
    c_d = str(int(c)+int(d))
    
    # Compute required products using kart
        
    if len(a) > 1 and len(c) > 1:
        ac = kart(a,c)
    else:
        ac = int(a)*int(c)
        
    if len(b) > 1 and len(d) > 1:
        bd = kart(b,d)
    else:
        bd = int(b)*int(d)
        
    if len(a_b) > 1 and len(c_d) > 1:
        abcd = kart(a_b,c_d)
    else:
        abcd = int(a_b)*int(c_d)
        
    k = 2*len(b)
    
    product = multi(ac,bd,abcd,k)
    
    return product
    
    
kart(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
    
    


