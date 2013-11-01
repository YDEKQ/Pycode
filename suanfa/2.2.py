#!/usr/bin/python
#coding:utf-8

'''
合并排序
merge(A,p,q,r) A 是数组， p q r 是下标，满足 p<=q<r.
'''
def merge(A,p,q,r):
    """docstring for merge"""
    n1 = q-p+1
    n2 = r-q
    L = [None]*(n1+1)
    R = [None]*(n2+1)
    for i in range(n1):
        L[i] = A[p+i]
    print L
    for j in range(n2):
        R[j] = A[q+j+1]
    print R
    i = 0
    j = 0
    for k in range(len(A)+2):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

A = [7,4,5,3,1,8,9,21,43,11,45,65,23,24,67,61,42]
print A
merge(A,0,5,len(A)-1)
print A
