#!/usr/bin/python
import random
x = 1
a = []
while x <= 100:
    b = random.randrange(1,100)
    a.append(b)
    x += 1
#print a
c = []
for i in range(100):
    b = random.randrange(1,100)
    c.append(b)

print 'c = ', c

def isSorted(ml):
    """paixu"""
    for i in range(len(ml)-1):
        if ml[i] > ml[i+1]:
            return False
        return True

isSorted(c)
print 'd = ', d

