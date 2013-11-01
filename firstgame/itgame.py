#!/usr/bin/python
#! -*- coding:utf-8 -*-
# 导入模块
import pygame
from pygame.locals import *
import math

# 2.初始化游戏
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100, 100]

acc = [0, 0]
arrows = []

# 加载图片
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

arrow = pygame.image.load("resources/images/bullet.png")

# 保持循环通过
while 1:
    # 再绘图之前再次清除屏幕
    screen.fill(0)
    for x in range(width/grass.get_width() + 1):
        for y in range(height/grass.get_height() + 1):
            screen.blit(grass, (x*100, y*100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # 6.绘制屏幕基础
    # 跟随鼠标旋转
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360- angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)
    #screen.blit(player, playerpos)
    # 更新屏幕
    pygame.display.flip()
    # 事件循环通过
    for event in pygame.event.get():
        # 如果按下关闭按钮
        if event.type == pygame.QUIT:
            # 如果是就退出游戏
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0] = True
            elif event.key ==K_a:
                keys[1] = True
            elif event.key ==K_s:
                keys[2] =True
            elif event.key ==K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0] = False
            elif event.key ==pygame.K_a:
                keys[1] = False
            elif event.key ==pygame.K_s:
                keys[2] = False
            elif event.key ==pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32, playerpos1[1] + 32])
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    elif keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
