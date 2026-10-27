import random
import math
import turtle as t
import playsound3 as p
import sys

screen = t.Screen()

player = t.Turtle()
bullets = []
player.penup()
backgroundimg = "GitHub/Mohameds-Code-Library/Images/random/battlebox.png"
screen.bgpic(backgroundimg)

heartimg = "GitHub/Mohameds-Code-Library/Images/random/heart.png"
screen.addshape(heartimg)
player.shape(heartimg)

for _ in range(10):
    bullet = t.Turtle()
    bullet.penup()
    bulletimg = "GitHub/Mohameds-Code-Library/Images/random/mbullet.png"
    screen.addshape(bulletimg)
    bullet.shape(bulletimg)
    bullets.append(bullet)
keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}
y = 0
x = 0
speed = 2
ymax = 300
xmax = 300
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
    global x
    global y
    player_right = player.xcor() + 25
    player_left = player.xcor() - 25
    player_up = player.ycor() + 25
    player_down = player.ycor() - 25
    for bullet in bullets:
        bullet_right = bullet.xcor() + 45
        bullet_left = bullet.xcor() - 45
        bullet_up = bullet.ycor() + 25
        bullet_down = bullet.ycor() - 25
        if bullet_right >= xmax:
            bullet.setx(xmax - 45)
        if bullet_left <= -xmax:
            bullet.setx(-xmax + 45)
        if bullet_up >= ymax:
            bullet.sety(ymax - 25)
        if bullet_down <= -ymax:
            bullet.sety(-ymax + 25)
    for bullet in bullets:
        bullet.left(-10)
        bullet.forward(10)
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