import random
import math
import turtle as t
import playsound3 as p
import sys

screen = t.Screen()

playery = 0
playerx = 0
speed = 2
ba = 0
ymax = 300
xmax = 300
meanboxes = []

player = t.Turtle()
player.penup()
backgroundimg = "GitHub/Mohameds-Code-Library/Images/random/battlebox.png"
screen.bgpic(backgroundimg)

heartimg = "GitHub/Mohameds-Code-Library/Images/random/heart.png"
screen.addshape(heartimg)
player.shape(heartimg)

for _ in range(20):
    meanbox = t.Turtle()
    meanboxes.append(meanbox)
    meanbox1 = (
    (10, 20),
    (-10, 20),
    (-10, -20),
    (10, -20)
    )
    screen.register_shape("meanbox1", meanbox1)
    meanbox.shape("meanbox1")
    meanbox.fillcolor("gold1")
    meanbox.showturtle()
    meanbox.teleport(
        random.randint(-xmax + 20, xmax - 20),
        random.randint(-ymax + 20, ymax - 20)
    )
    meanbox.seth(random.randint(0, 359))
    meanbox.penup()
keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}
#gameid = 0
#current_gameid = 0
#game_running = False

def upclick():
#    if not game_running:
#        return
    keys["w"] = True
def downclick():
#   if not game_running:
#        return
    keys["s"] = True
def rightclick():
#    if not game_running:
#        return
    keys["d"] = True
def leftclick():
#    if not game_running:
#        return
    keys["a"] = True
def uprelease():
    keys["w"] = False
def downrelease():
    keys["s"] = False
def rightrelease():
    keys["d"] = False
def leftrelease():
    keys["a"] = False

def player_movement():
#    if my_gameid != gameid:
#        return

#    if not game_running:
#        return

    player.penup()
    y = player.ycor()
    x = player.xcor()

    if keys["w"]:
        y += 4 * speed
    if keys["s"]:
        y -= 4 * speed
    if keys["d"]:
        x += 4 * speed
    if keys["a"]:
        x -= 4 * speed

    player.goto(x, y)
    screen.ontimer(player_movement, 20)
def border():
    global playerx
    global playery
    global bulletx
    global bullety

    player_right = player.xcor() + 25
    player_left = player.xcor() - 25
    player_up = player.ycor() + 25
    player_down = player.ycor() - 25

    for meanbox in meanboxes:
        meanbox_right = meanbox.xcor() + 45
        meanbox_left = meanbox.xcor() - 45
        meanbox_up = meanbox.ycor() + 25
        meanbox_down = meanbox.ycor() - 25
        if meanbox_right >= xmax:
            meanbox.setx(xmax - 45)
        if meanbox_left <= -xmax:
            meanbox.setx(-xmax + 45)
        if meanbox_up >= ymax:
            meanbox.sety(ymax - 25)
        if meanbox_down <= -ymax:
            meanbox.sety(-ymax + 25)
    if player_right >= xmax:
        player.setx(xmax - 25)
        keys["d"] = False
    if player_left <= -xmax:
        player.setx(-xmax + 25)
        keys["a"] = False
    if player_up >= ymax:
        player.sety(ymax - 25)
        keys["w"] = False
    if player_down <= -ymax:
        player.sety(-ymax + 25)
        keys["s"] = False
    screen.ontimer(border, 10)


screen.listen()

screen.onkeypress(upclick, "w")
screen.onkeypress(rightclick, "d")
screen.onkeypress(downclick, "s")
screen.onkeypress(leftclick, "a")

screen.onkeyrelease(uprelease, "w")
screen.onkeyrelease(downrelease, "s")
screen.onkeyrelease(rightrelease, "d")
screen.onkeyrelease(leftrelease, "a")


player_movement()
border()


screen.tracer(8, 45)
wn = t.Screen()
wn.mainloop()