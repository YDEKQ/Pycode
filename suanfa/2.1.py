#!/usr/bin/python
#coding:utf-8
def insertion_sort(A):
    """docstring for insertion_sort"""
    n = len(A)
    for j in range(1,n):
        save = A[j]
        #print save
        i = j- 1
        while i >=0 and A[i] > save:
            A[i+1] = A[i]
            #print 'i',i
            #print 'A[i+1]' ,A[i+1]
            i = i - 1
        A[i+1] = save

a = [5,2,4,6,1,3]
print a
insertion_sort(a)
print a
