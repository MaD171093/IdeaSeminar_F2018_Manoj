#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep
import random

# http://www.101computing.net/python-turtle-spirograph/

window = turtle.Screen()
window.bgcolor("#FFFFFF")
window.colormode(255)
m = turtle.Turtle()

R = 90
r = 97
d = 80

angle = 0

theta = 0.2
steps = int(100*3.14/theta)
m.speed(0)
print(steps)
j = 0
ctr=j
for t in range(0,steps):
    m.speed(0)
    angle += theta
    
    
    if j <= 255:
        r1 = 255-j
        g1 = 0 + j
        b1 = 255 -j
    else:
        ctr += 1
        j = 0
        r1 = 255-j
        g1 = 0 + j
        b1 = 255 -j
    j+=1

    print(j)
    m.pencolor((r1,g1,b1))
    #m.begin_fill()
    if ctr<=1:
        x = (R + r) * cos(angle) + d * cos(((R+r)/r)*angle) 
        y = (R + r) * sin(angle) - d * sin(((R+r)/r)*angle)  
    if ctr>1:
        x = (R + r) * cos(angle) + d * cos(((R+r)/r)*angle) 
        y = (R + r) * sin(angle) + d * sin(((R+r)/r)*angle)
    if ctr == 4:
        m.hideturtle()
        break
    m.pensize(1)
    if t == 0:
        m.penup()
        m.goto(x,y)
        m.pendown()
    else:
        m.goto(x,y)
    #m.end_fill()

turtle.done()

#homework implement other formulas
#make it random and crazy