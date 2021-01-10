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
sideLength = 150
width = 2
x = 1
y = 1
tipe = 1

point_x = 10+left
point_y = 10+top
circle_left = 0
circle_top = 0
circle_radius = 10
circle_width = 2

def move_square():
    pygame.time.delay(5)
    pygame.draw.rect(screen,color,[left,top,sideLength,sideLength],width,0)
def modify_square():
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
def move_circle(point_x,point_y,circle_radius,circle_width,circle_left,circle_top):
    pygame.draw.circle(screen,color,[point_x+circle_left,point_y+circle_top],circle_radius,circle_width)
def modify_circle(point_x,point_y,circle_left,circle_top,circle_radius,circle_width):
    circle_left += 1
    circle_top += 1
    move_circle(point_x,point_y,circle_radius,circle_width,circle_left,circle_top)
    
    
while True:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    dark=0,0,0
    screen.fill(dark)
    move_square()
    modify_square()
    modify_circle(point_x,point_y,circle_left,circle_top,circle_radius,circle_width)
    pygame.display.update()      