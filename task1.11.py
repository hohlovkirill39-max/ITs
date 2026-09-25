#!/usr/bin/python3
from turtle import *

def circle(direction='left'):
    N = 5 * a
    for _ in range(N):
        forward(1)
        if direction == 'left':
            left(360/N)
        elif direction == 'right':
            right(360/N)
        else: return
    update()

def eight():
    circle('left')
    circle('right')

shape('classic')
speed(0)
left(90)
for a in range(10, 200, 5):
    eight()
