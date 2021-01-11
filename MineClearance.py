# -*- coding: utf-8 -*-
'''
import pygame
from pygame.locals import *
import sys
import time

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
2:移动矩形
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("move square")

color = 255,255,0
left = 0
top = 0
length = 150
height = 200
width = 2
x = 1
y = 1
xx = 1
yy = 1 
tipe = 1
point_x = 10+left
point_y = 10+top
circle_left = 100
circle_top = 50
circle_radius = 10
circle_width = 2
circle = [point_x,point_y,circle_left,circle_top,circle_radius,circle_width]

def move_square():
    pygame.time.delay(5)
    pygame.draw.rect(screen,color,[left,top,length,height],width,0)
def modify_square():
    global tipe
    global y
    global x
    global top
    global left
    left += x
    top += y
    if (left+length) >= 500 or left < 0:
        x = -x
    if (top+height) >= 600 or top < 0:
        y = -y
def move_circle(circle):
    pygame.draw.circle(screen,color,[circle[0]+circle[2],circle[1]+circle[3]],circle[4],circle[5])
def modify_circle(circle):
    global xx
    global yy
    circle[0] = 10+left
    circle[1] = 10+top
    circle[2] += xx
    circle[3] += yy
    if circle[2] >= 140 or circle[2] <= 0:
        xx = -xx
    if circle[3] >= 190 or circle[3] <= 0:
        yy = -yy
    move_circle(circle)
    
    
while True:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    dark=0,0,0
    screen.fill(dark)
    move_square()
    modify_square()
    modify_circle(circle)
    pygame.display.update()      
'''
#3:画大饼

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drop ball")

            
#4:飞机大战


































