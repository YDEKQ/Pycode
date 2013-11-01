#!/usr/bin/python
#! -*- coding: utf-8 -*-

# fd bk 向前 向后 lt rt 左转 右转 pu pd 画笔 抬起 放下
import math
from swampy.TurtleWorld import *    # 导入模块

world = TurtleWorld()
bob = Turtle()      # 实例turtle
#print bob
bob.delay = 0.8  # bob 速度

# 第一步 画正方形
#for i in range(4):
#    fd(bob, 100)
#    lt(bob)

# 第二步 封装画正方形的代码
def square(t, length, n):      # 增加length的行参:边长
    """画正方形"""
    for i in range(n):
        fd(t, length)
        lt(t, 360.0/n)       # 增加转弯角度

def polygon(t, length, n, angle):      # 增加length的行参:边长
    """画正方形"""
    langle = 2 *  math.pi
    for i in range(n):
        fd(t, length)
        lt(t, 360.0/n)       # 增加转弯角度

def circle(t, r):
    """半径r 通过合适的边和边长画近似的圆"""
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    square(t, length, n)

#circle(bob,50)

def yangshuzhou(t, length):
    """yangshuzhou"""
    fd(t,length)
    bk(t, length/2)
    lt(t)
    fd(t, length)
    bk(t,length * 3)
    fd(t,length * 2)
    lt(t, 155)
    fd(t, length * 1.5)
    bk(t, length * 1.5)
    lt(t,50)
    fd(t, length * 1.5)



#square(bob, 80, 6)

yangshuzhou(bob,100)

wait_for_user()     # 等待用户的指示
