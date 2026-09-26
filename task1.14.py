#!/usr/bin/python3
from turtle import *

def star(n, rayLen, m):
    penup()
    rayLen2 = 0.5 * rayLen
    forward(rayLen2)
    pendown()
    a = 180 - (180 * (n - 2 * m) / n)
    for _ in range(n):
        left(a)
        forward (rayLen)

speed(0)
shape('triangle')
left(180)
penup()
back(100)
star(5, 100, 2)
penup()
forward(100)
star(11, 100, 5)

done()
