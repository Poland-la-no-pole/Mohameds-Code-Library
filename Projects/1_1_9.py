import turtle as t
import random
import time

screen = t.Screen()

pizzat = t.Turtle()
pizzat_smallcrust = t.Turtle()
saucet = t.Turtle()
cheeset = t.Turtle()
oven = t.Turtle()
welcome = "welcome to bills, what size would you like your pizza. we have small, medium, large"
while True:
    size = t.textinput("welcome", welcome)
    if "small" in size:
        x = 0
        e = 0
        break
    elif "medium" in size:
        x = 15
        e = 2
        break
    elif "large" in size:
        x = 30
        e = 4
        break
    else:
        welcome = "dude, im just a 9-5 worker, quit being difficult and pick a size(small, medium or large please)"
        continue


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
pizzat.color("LightGoldenrod1")
pizzat.penup()
for i in range(18):
    pizzat.right(45)
    pizzat.shapesize(2 + i/3)
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
else:
    saucet.color("OrangeRed1")

saucet.shape("circle")
for i in range(5):
    time.sleep(.1)
    saucet.shapesize(2 + i + e)
saucet.shape("pizza")
saucet.shapesize(.95)
#cheese
cheese = t.textinput("CHEESE","what kind of cheese would you like, we have cheddar or parmesan")
cheeset.shape("circle")
cheeset.shapesize(.7)
if "cheddar" in cheese:
    cheeset.color("DarkGoldenrod1")
elif "parmesan" in cheese:
    cheeset.color("LemonChiffon")
else:
    cheeset.color("DarkGoldenrod1")
for _ in range(200):
    cheeset.teleport(random.randint(-60 - x, 60 + x), random.randint(-60 - x, 60 + x))
    cheeset.stamp()
#baking
oven1 = "GitHub/Mohameds-Code-Library/Photos/oven.gif"
screen.addshape(oven1)
oven.shape(oven1)
time.sleep(4)
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
oven.hideturtle()

screen.mainloop()

