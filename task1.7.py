#!/usr/bin/python3
from turtle import *

a = 30
speed(0)
shape('triangle')
for _ in range(1000):
    x, y = pos()
    forward(1)
    setheading(a * (x**2 + y**2)**0.5)
done()
