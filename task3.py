#!/usr/bin/python3
from turtle import *

shape('triangle')
for a in range (1, 100, 10):
 pendown()
 goto(a, a)
 for i in range(4):
    forward(a)
    right(90)
 penup()
