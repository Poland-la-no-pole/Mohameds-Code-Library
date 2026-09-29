import turtle as t
import random

screen = t.Screen()
pizzat = t.Turtle()
pizzat_smallcrust = t.Turtle()
pizzat_smallcrust.seth(90)
pizzat.seth(90)

size = t.textinput("welcome","welcome to bills, what size would you like your pizza. we have s, m, l, or xl ")
if(size == "s"):
    x = 0
if(size == "m"):
    x = 10
if(size == "l"):
    x = 20
if(size == "xl"):
    x = 30

pizza = (
    (80 + (.5 * x), 75 + x),
    (20 - (.5 * x), 75 + x),
    (-25 - x,30 + (.5 * x)),
    (-25 - x,-30 - (.5 * x)),
    (20 - (.5 * x),-75 - x),
    (80 + (.5 * x),-75 - x),
    (125 + x,-30 - (.5 * x)),
    (125 + x, 30 + (.5 * x))
    )
pizza_layer1 = (
    (80 + (.5 * x), 75 + x),
    (20 - (.5 * x), 75 + x),
    (-25 - x, 30 + (.5 * x)),
    (-25 - x, -30 - (.5 * x)),
    (20 - (.5 * x), -75 - x),
    (80 + (.5 * x), -75 - x),
    (125 + x, -30 - (.5 * x)),
    (125 + x, 30 + (.5 * x)),
    (80 + (.5 * x), 75 + x),
    (85 + (.75 * x), 80 + (1.5 * x)),
    (15 - (.75 * x), 80 + (1.5 * x)),
    (-30 - (1.5 * x), 35 + (.75 * x)),
    (-30 - (1.5 * x), -35 - (.75 * x)),
    (15 - (.75 * x), -80 - (1.5 * x)),
    (85 + (.75 * x), -80 - (1.5 * x)),
    (130 + (1.5 * x), -35 - (.75 * x)),
    (130 + (1.5 * x), 35 + (.75 * x)),
    (85 + (.75 * x), 80 + (1.5 * x))
    )

# Register the new custom shape and name it "mystar"
screen.register_shape("pizza", pizza)
screen.register_shape("layer1", pizza_layer1)
# Create your turtle and apply the shape

pizzat.shape("pizza")
pizzat.color("bisque")
pizzat_smallcrust.shape("layer1")
pizzat_smallcrust.color("peru")

# Move it around to test





screen.mainloop()

