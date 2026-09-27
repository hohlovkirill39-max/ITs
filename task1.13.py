#!/usr/bin/python3
from turtle import *

def circle1(x, y, radius, color):
    penup()
    goto(x, y - radius)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()
def arc(x, y, radius, angle, color):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    pencolor(color)
    pensize(9)
    circle(radius, angle)

speed(0)
circle1(0, 0, 95, "yellow")
circle1(-38, 45, 15, "blue")
circle1(38, 45, 15, "blue")
penup()
goto(0, 15)
setheading(-90)
pendown()
pencolor("black")
pensize(9)
forward(28)
arc(0, -70, 60, 90, "red")
penup()
goto(0, -70)
pendown()
arc(0, -70, 60, -90, "red")

done()
