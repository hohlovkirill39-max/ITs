#!/usr/bin/python3
from turtle import *

shape("triangle")
speed(0)

def draw_arc(radius):
    circle(-radius, 180)
penup()
goto(-250, 0)
setheading(90)
pendown()

R_big = 50    
R_small = 15  
loops = 4 

for _ in range(loops):
    draw_arc(R_big)
    draw_arc(R_small)
draw_arc(R_big)

done()
