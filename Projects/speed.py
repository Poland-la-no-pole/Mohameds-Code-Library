import turtle as trtl

import random
import math
import time

painter = trtl.Turtle()
screen = trtl.Screen()


# BODY
painter.begin_fill()
painter.fillcolor("black")
painter.circle(100)
painter.end_fill()


# HEAD
painter.begin_fill()
painter.goto(0, 20)
painter.circle(-40)
painter.end_fill()


# PURPLE EYES
painter.teleport(-12, -15)
painter.begin_fill()
painter.fillcolor("purple")
painter.circle(-12)
painter.end_fill()

painter.teleport(7, -15)
painter.begin_fill()
painter.fillcolor("purple")
painter.circle(-12)
painter.end_fill()


# BLACK PUPILS
painter.teleport(-14, -25)
painter.begin_fill()
painter.fillcolor("black")
painter.circle(-4)
painter.end_fill()

painter.teleport(5, -25)
painter.begin_fill()
painter.fillcolor("black")
painter.circle(-4)
painter.end_fill()


# LEGS
painter.pensize(8)
painter.pencolor("black")

legs = [
    [(-60, 180), (-120, 210), (-160, 190)],
    [(-90, 143.6), (-145, 150), (-180, 125)],
    [(-90, 56.4), (-145, 45), (-180, 15)],
    [(-60, 20), (-110, -15), (-140, -60)],

    [(60, 180), (120, 210), (160, 190)],
    [(90, 143.6), (145, 150), (180, 125)],
    [(90, 56.4), (145, 45), (180, 15)],
    [(60, 20), (110, -15), (140, -60)]
]

for leg in legs:
    painter.teleport(leg[0][0], leg[0][1])
    painter.pendown()

    painter.goto(leg[1][0], leg[1][1])
    painter.goto(leg[2][0], leg[2][1])

    painter.penup()


wn = trtl.Screen()
wn.mainloop()


#what do you think is the biggest benefit of using well-named variables?
#to make sure our variables dont get mixed up with eachother
#What can a programmer do to reduce bugs in code?
#add debugging and multiple check in there code to stop bugs