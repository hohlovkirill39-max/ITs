#!/usr/bin/python3
from turtle import *

side = 20   
step = 10 
 
for i in range(10):
    for _ in range(4):
        forward(side)
        left(90)
    penup()
    backward(step)
    right(90)
    forward(step)
    left(90)
    pendown()
 
    side += 2 * step   
 
done()
