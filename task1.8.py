#!/usr/bin/python3
from turtle import *

a = 2
speed(0)
shape('triangle')
for _ in range(1000):
    forward(a)
    a += 10
    left(90)
done()
