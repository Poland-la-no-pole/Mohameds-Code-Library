import turtle as t
import random

screen = t.Screen()
pizzat = t.Turtle()
pizzat_smallcrust = t.Turtle()
saucet = t.Turtle()




size = t.textinput("welcome","welcome to bills, what size would you like your pizza. we have small, medium, large")
if "small" in size:
    x = 0
    e = 0
elif "medium" in size:
    x = 15
    e = 1.5
elif "large" in size:
    x = 30
    e = 3
#pizza
pizza = (
    (30 + (.5 * x), 75 + x),
    (-30 - (.5 * x), 75 + x),
    (-75 - x,30 + (.5 * x)),
    (-75 - x,-30 - (.5 * x)),
    (-30 - (.5 * x),-75 - x),
    (30 + (.5 * x),-75 - x),
    (75 + x,-30 - (.5 * x)),
    (75 + x, 30 + (.5 * x))
    )


screen.register_shape("pizza", pizza)
pizzat.shape("circle")
pizzat.color("bisque")
pizzat.penup()
for i in range(18):
    pizzat.right(45)
    pizzat.shapesize(2 + i/2)
    if(pizzat.xcor() == 0):
        pizzat.goto(5, 0)
    if(pizzat.ycor() == 0):
        pizzat.goto(5, 5)
    if(pizzat.xcor() == 5):
        pizzat.goto(0, 5)
    if(pizzat.ycor() == 5):
        pizzat.goto(0, 0)
pizzat.shapesize(1)
pizzat.shape("pizza")
#sauce
sauce = t.textinput("SAUCE","what kind of sauce would you like, we have alfredo or marinara sauce")
if "marinara" in sauce:
    saucet.color("OrangeRed1")
elif "alfredo" in sauce:
    saucet.color("cornsilk")
saucet.shape("circle")
saucet.shapesize(7 + e)
# pizza crust after baking
pizza_layer1 = (
    (30 + (.5 * x), 75 + x),
    (-30 - (.5 * x), 75 + x),
    (-75 - x, 30 + (.5 * x)),
    (-75 - x, -30 - (.5 * x)),
    (-30 - (.5 * x), -75 - x),
    (30 + (.5 * x), -75 - x),
    (75 + x, -30 - (.5 * x)),
    (75 + x, 30 + (.5 * x)),
    (30 + (.5 * x), 75 + x),
    (35 + (.75 * x), 80 + (1.5 * x)),
    (-35 - (.75 * x), 80 + (1.5 * x)),
    (-80 - (1.5 * x), 35 + (.75 * x)),
    (-80 - (1.5 * x), -35 - (.75 * x)),
    (-35 - (.75 * x), -80 - (1.5 * x)),
    (35 + (.75 * x), -80 - (1.5 * x)),
    (80 + (1.5 * x), -35 - (.75 * x)),
    (80 + (1.5 * x), 35 + (.75 * x)),
    (35 + (.75 * x), 80 + (1.5 * x))
    )
screen.register_shape("layer1", pizza_layer1)
pizzat_smallcrust.shape("layer1")
pizzat_smallcrust.color("peru")
pizzat_smallcrust.penup()
#pizzat_smallcrust.seth(pizzat.heading())

screen.mainloop()

