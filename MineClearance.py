# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time
'''
1：Hello World
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Hello,World")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
'''
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("move square")

color = 255,255,0
global left
left = 0
global top
top = 0
sideLength = 20
width = 2
global x
x = 1
global y
y = 1
global tipe
tipe = 1
def movesquare():
    pygame.draw.rect(screen,color,[left,top,sideLength,sideLength],width,0)
def modify(tipe):
    
    if tipe == 1 and (left+sideLength) < 500:
        left += x
        top += y
    else:
        x = -x
        tipe += 1
        left += x
        top += y
    if tipe == 2 and (top+sideLength) < 600:
        left += x
        top += y
    else:
        y = -y
        tipe += 1
        left += x
        top += y
    if tipe == 3 and left > 0:
        left += x
        top += y
    else:
        x = -x
        tipe += 1
        left += x
        top += y
    if tipe == 4 and top > 0 :
        left += x
        top += y
    else:
        y = -y
        tipe = 1
        left += x
        top += y
while True:
    for event in pygame.event.get():
        movesquare()
        modify()
        time.sleep(1)
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()      