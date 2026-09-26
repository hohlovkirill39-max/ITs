#!/usr/bin/python3
from turtle import *
a = 12
b = 360 / a
speed(0)
shape('turtle')
for _ in range(a):
    forward(100)
    stamp()
    left(180)
    forward(100)
    right(180)
    right(b)
done()
