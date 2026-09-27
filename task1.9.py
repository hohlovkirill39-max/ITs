#!/usr/bin/python3
from turtle import *
from math import *

def draw_polygon(n, r):
    a = 2 * r * sin(pi / n)
    turn_angle = 90 + 180 / n
    left(turn_angle)
    for _ in range(n):
        forward(a)
        left(360 / n)
    right(turn_angle)
    
r = 25 
dr = 18      
count = 10
shape("turtle")
speed(0)
penup()
goto(r, 0)
pendown()

for i in range(count):
    pendown()
    n = 3 + i
    draw_polygon(n, r)
    penup()
    if i < count - 1:
        forward(dr)
        r += dr

done()
