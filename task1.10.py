from turtle import *

def circle(direction='left'):
    N = 300
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
a = 3
for _ in range(a):
    eight()
    left(180 / a)

done()
