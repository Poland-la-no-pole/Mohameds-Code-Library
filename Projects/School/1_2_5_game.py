import random
import math
import turtle as t
import playsound3 as p
import sys

screen = t.Screen()

playery = 0
playerx = 0
meanboxy = 0
meanboxx = 0
speed = 2
ymax = 300
xmax = 300
timer = 10
point = 0
meanboxes = []

box = t.Turtle()
box.shape("square")
box.fillcolor("white")
box.shapesize(2)
box.teleport(random.randint(-xmax + 20, xmax - 20),random.randint(-ymax + 20, ymax - 20))

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.teleport(0, 300)
player = t.Turtle()
player.penup()
backgroundimg = "GitHub/Mohameds-Code-Library/Images/random/battlebox.png"
screen.bgpic(backgroundimg)

heartimg = "GitHub/Mohameds-Code-Library/Images/random/heart.png"
screen.addshape(heartimg)
player.shape(heartimg)


meanbox1 = (
    (15, 15),
    (-15, 15),
    (-15, -15),
    (15, -15)
)
screen.register_shape("meanbox1", meanbox1)
for _ in range(20):
    meanbox = t.Turtle()
    meanboxes.append(meanbox)
    meanbox.shape("meanbox1")
    meanbox.fillcolor("gold1")
    meanbox.showturtle()
    meanbox.teleport(random.randint(-xmax + 20, xmax - 20),random.randint(-ymax + 20, ymax - 20))
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
    screen.update()
def border():
    global playerx
    global playery
    global bulletx
    global bullety

    player_right = player.xcor() + 25
    player_left = player.xcor() - 25
    player_top = player.ycor() + 25
    player_bottom = player.ycor() - 25

    for meanbox in meanboxes:
        meanbox_right = meanbox.xcor() + 15
        meanbox_left = meanbox.xcor() - 15
        meanbox_top = meanbox.ycor() + 15
        meanbox_bottom = meanbox.ycor() - 15
        if meanbox_right >= xmax:
            meanbox.setx(xmax - 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
        if meanbox_left <= -xmax:
            meanbox.setx(-xmax + 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
        if meanbox_top >= ymax:
            meanbox.sety(ymax - 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
        if meanbox_bottom <= -ymax:
            meanbox.sety(-ymax + 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
    if player_right >= xmax:
        player.setx(xmax - 25)
        keys["d"] = False
    if player_left <= -xmax:
        player.setx(-xmax + 25)
        keys["a"] = False
    if player_top >= ymax:
        player.sety(ymax - 25)
        keys["w"] = False
    if player_bottom <= -ymax:
        player.sety(-ymax + 25)
        keys["s"] = False
def meanbox_movement():
    for meanbox in meanboxes:
        meanbox.forward(4)
    screen.update()
def points():
    global timer
    global point
    player_right = player.xcor() + 25
    player_left = player.xcor() - 25
    player_top = player.ycor() + 25
    player_bottom = player.ycor() - 25
    box_left = box.xcor() - 20
    box_right = box.xcor() + 20
    box_bottom = box.ycor() - 20
    box_top = box.ycor() + 20
    if (player_right >= box_left and player_left <= box_right and player_top >= box_bottom and player_bottom <= box_top):
        box.teleport(random.randint(-xmax + 20, xmax - 20), random.randint(-ymax + 20, ymax - 20))
        timer += 3
        point += 1
    screen.update()
def collision():
    global timer
    player_right = player.xcor() + 25
    player_left = player.xcor() - 25
    player_top = player.ycor() + 25
    player_bottom = player.ycor() - 25
    for meanbox in meanboxes:
        meanbox_right = meanbox.xcor() + 15
        meanbox_left = meanbox.xcor() - 15
        meanbox_top = meanbox.ycor() + 15
        meanbox_bottom = meanbox.ycor() - 15
        if (player_right >= meanbox_left and player_left <= meanbox_right and player_top >= meanbox_bottom and player_bottom <= meanbox_top):
            sys.exit()

def countdown():
    global counter
    global timer
    global point

    counter.clear()

    if timer <= 0:
        counter.write("Time's Up",font=("Arial", 20, "normal"))
        sys.exit()

    else:
        counter.write("Timer: " + str(timer) + "  Points: " + str(point), font=("Arial", 20, "normal"))
        timer -= 1
    screen.ontimer(countdown, 1000)

def gameloop():
    player_movement()
    meanbox_movement()
    border()
    points()
    collision()
    screen.ontimer(gameloop, 16)

screen.listen()

screen.onkeypress(upclick, "w")
screen.onkeypress(rightclick, "d")
screen.onkeypress(downclick, "s")
screen.onkeypress(leftclick, "a")

screen.onkeyrelease(uprelease, "w")
screen.onkeyrelease(downrelease, "s")
screen.onkeyrelease(rightrelease, "d")
screen.onkeyrelease(leftrelease, "a")

screen.tracer(0)
countdown()
gameloop()



wn = t.Screen()
wn.mainloop()