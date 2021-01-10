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
left = 0
top = 0
sideLength = 20
width = 2
x = 1
y = 1
tipe = 1
def movesquare():
    dark=0,0,0
    screen.fill(dark)
    pygame.time.delay(5)
    pygame.draw.rect(screen,color,[left,top,sideLength,sideLength],width,0)
def modify():
    global tipe
    global y
    global x
    global top
    global left
    left += x
    top += y
    if (left+sideLength) >= 500 or left < 0:
        x = -x
    if (top+sideLength) >= 600 or top < 0:
        y = -y
while True:
    for event in pygame.event.get():
        movesquare()
        modify()
        pygame.display.update()   
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     