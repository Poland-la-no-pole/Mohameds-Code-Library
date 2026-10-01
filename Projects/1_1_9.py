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
    if "small" in size or "s " in size or "Small" in size:
        size1 = "SMALL"
        x = 0
        e = 0
        break
    elif "medium" in size or  "m " in size or "Medium" in size:
        size1 = "MEDIUM"
        x = 15
        e = 2
        break
    elif "large" in size or "l " in size or "Large" in size:
        size1 = "LARGE"
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
saucechoice = "what kind of sauce would you like, we have alfredo or marinara sauce"
while True:
    sauce = t.textinput("SAUCE", saucechoice)
    if "marinara" in sauce or "m" in sauce or "mar" in sauce or "Marinara" in sauce:
        saucet.color("OrangeRed1")
        break
    elif "alfredo" in sauce or "alf" in sauce or "a" in sauce or "Alfredo" in sauce:
        saucet.color("cornsilk")
        break
    else:
        saucechoice = "please pick a sauce that we have, who even likes " + sauce + " on pizza (alfredo or marinara)"
        continue

saucet.shape("circle")
for i in range(5):
    time.sleep(.1)
    saucet.shapesize(2 + i + e)
saucet.shape("pizza")
saucet.shapesize(.95)
#cheese
while True:
    cheesechoice = "what kind of cheese would you like, we have cheddar or parmesan"
    cheese = t.textinput("CHEESE", cheesechoice)
    cheeset.shape("circle")
    cheeset.shapesize(.7)
    if "cheddar" in cheese or "chedda" in cheese or "c" in cheese:
        cheeset.color("DarkGoldenrod1")
        break
    elif "parmesan" in cheese or "parm" in cheese or "p" in cheese:
        cheeset.color("LemonChiffon")
        break
    else:
        cheesechoice = "please pick a cheese that we have, who even likes " + cheese + " on pizza (cheddar or parmesan)"
        continue
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

writer = t.Turtle()
writer.shapesize(5)
writer.hideturtle()
writer.teleport(-50, 200)
writer.write("HERE IS YOUR "+ size1 + " PIZZA")
screen.mainloop()

