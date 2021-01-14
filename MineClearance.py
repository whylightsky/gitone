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
#3:掉球游戏
import pygame,random,sys,time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Drop ball")
color = 255,255,0
rect_baffle_x,rect_baffle_y,rect_baffle_w,rect_baffle_h = 250,460,100,40
circle_ball_x,circle_ball_y,circle_ball_r,circle_ball_w = random.randint(30,570),50,30,2
rect_baffle = [rect_baffle_x,rect_baffle_y,rect_baffle_w,rect_baffle_h]
circle_ball = [circle_ball_x,circle_ball_y,circle_ball_r,circle_ball_w]
move_x,move_y,move_flag = 0,1,0
move = [move_x,move_y,move_flag]
live,score = 3,0
information = [live,score]

def print_all(information):
    myfont = pygame.font.Font(None,20)
    pygame.draw.line(screen,(255,255,255),(0,20),(600,20),2)
    imagetext = myfont.render("Live:" + str(information[0]),True, (255,255,255))
    screen.blit(imagetext,(0,0))
    imagetext = myfont.render("Score:" + str(information[1]),True,(255,255,255))
    screen.blit(imagetext,(550,0))
def ball_move(circle_ball,move,information):
    circle_ball[1] += move[1]
    circle_ball[0] += move[0]
    if (circle_ball[1]+30) == 460 and circle_ball[0] >= rect_baffle[0] and circle_ball[0] <= (rect_baffle[0]+100):
        move[1] = -move[1]
        information[1] += 1
        if move[2] == -1:
            move[0] += -1
        else:
            move[0] += 1
    if (circle_ball[0]+30) >= 600 or (circle_ball[0]-50) <= 0:
        move[0] = -move[0]
    if (circle_ball[1]-50) <= 0:
        move[1] = -move[1]
    if (circle_ball[1]+30) >= 500:
        if information[0] == 0:
            pygame.quit()
            sys.exit()
        else:
            information[0] -= 1
            circle_ball[1] -= 420

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if rect_baffle[0] > 0:
                    rect_baffle[0] -= 20
                move[2] = -1
            if event.key == K_RIGHT:
                if rect_baffle[0] < 500:
                    rect_baffle[0] += 20
                move[2] = 1
    screen.fill((0,0,0)) 
    print_all(information)
    pygame.time.delay(5)
    ball_move(circle_ball,move,information)
    pygame.draw.rect(screen, color, (rect_baffle[0],rect_baffle[1],rect_baffle[2],rect_baffle[3]),2)
    pygame.draw.circle(screen, color,(circle_ball[0],circle_ball[1]),circle_ball[2],circle_ball[3]) 
    pygame.display.update()
#4:飞机大战


































