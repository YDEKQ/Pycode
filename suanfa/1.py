#!/usr/bin/python
import math

n = 1
'''
while True:
    a = 8 * math.log10(n)
    if (a == n):
        print n
    elif (n >100000):
        break

    else:
        print n
        print a
        n = n + 1
'''
while n < 100000:
    b = 100*n*n
    a = pow(2,n)
    if (a >= b):
        print n
        print a
        print b
    n += 1
