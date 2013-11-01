#!/usr/bin/python
#coding:utf-8

'''
输入：一列数 A = [a1,a2,a3...an], 和一个值 v
输出：下标 i ，v ＝ A[i],或者当v不存在A中出现时为 NIL。
'''
def serchA(A,v):
    """docstring for serchA"""
    flag = 0
    for i in range(len(A)):
        if A[i] == v :
            print i
            flag =1
    if flag == 0:
        print 'NIL'
        # code...
A = [1,3,4,5,8,6,7]
serchA(A,2)
