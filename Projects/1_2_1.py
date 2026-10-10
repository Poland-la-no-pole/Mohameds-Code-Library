import turtle as t
import random
import math
import sys
import playsound3
#objects
heart = t.Turtle()
mbullet = t.Turtle()
sbullet = t.Turtle()
box = t.Turtle()
counter = t.Turtle()
screen = t.Screen()

timer = 5
points = 0
yMAX = 198
xMAX = 200
gameid = 0
game_running = False
sound = False


def gamestart():
    while True:
        startchoice = t.textinput("Intro","This is my game, would you like to play it")
        if (startchoice in ["yes", "Yes", "y", "Y"]):
            break
        elif (startchoice in ["no", "No", "n", "N"]):
            sys.exit()

keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

def startup():
    global yMAX
    global xMAX
    global timer
    global points
    global game_running
    global gameid

    game_running = True
    timer = 5
    points = 0

    # GAME ID
    gameid += 1

    #heart
    heart1 = "GitHub/Mohameds-Code-Library/Photos/heart.png"
    screen.addshape(heart1)
    heart.shape(heart1)
    heart.showturtle()
    heart.home()
    #medium bullet
    bulletm = "GitHub/Mohameds-Code-Library/Photos/mbullet.png"
    screen.addshape(bulletm)
    mbullet.shape(bulletm)
    #mbullet.showturtle()
    box.shape("square")
    box.shapesize(2)
    box.color("white")
    box.showturtle()

    #background
    screen.bgpic("GitHub/Mohameds-Code-Library/Photos/battlebox.png")
    counter.hideturtle()
    counter.penup()
    counter.teleport(0, 300)

    box.teleport(
        random.randint(-xMAX + 20, xMAX - 20),
        random.randint(-yMAX + 20, yMAX - 20)
    )

    box.penup()
    heart.penup()

def upclick():
    if not game_running:
        return
    keys["w"] = True

def downclick():
    if not game_running:
        return
    keys["s"] = True

def rightclick():
    if not game_running:
        return
    keys["d"] = True

def leftclick():
    if not game_running:
        return
    keys["a"] = True

def uprelease():
    keys["w"] = False

def downrelease():
    keys["s"] = False

def rightrelease():
    keys["d"] = False

def leftrelease():
    keys["a"] = False

def move(my_gameid):
    global heart
    global screen
    global game_running

    if my_gameid != gameid:
        return

    if not game_running:
        return

    heart.penup()
    y = heart.ycor()
    x = heart.xcor()

    if keys["w"]:
        y += 4
    if keys["s"]:
        y -= 4
    if keys["d"]:
        x += 4
    if keys["a"]:
        x -= 4

    heart.goto(x, y)

    screen.ontimer(lambda: move(my_gameid), 10)

def border(my_gameid):
    global box
    global heart
    global screen
    global yMAX
    global xMAX
    global game_running

    if my_gameid != gameid:
        return

    if not game_running:
        return

    heart_left = heart.xcor() - 25
    heart_right = heart.xcor() + 25
    heart_bottom = heart.ycor() - 25
    heart_top = heart.ycor() + 25

    box_left = box.xcor() - 20
    box_right = box.xcor() + 20
    box_bottom = box.ycor() - 20
    box_top = box.ycor() + 20

    if heart_right > xMAX:
        heart.setx(xMAX - 25)
    if heart_left < -xMAX:
        heart.setx(-xMAX + 25)
    if heart_bottom < -yMAX:
        heart.sety(-yMAX + 25)
    if heart_top > yMAX:
        heart.sety(yMAX - 25)
    if box_right > xMAX:
        box.setx(xMAX - 20)
    if box_left < -xMAX:
        box.setx(-xMAX + 20)
    if box_bottom < -yMAX:
        box.sety(-yMAX + 20)
    if box_top > yMAX:
        box.sety(yMAX - 20)

    screen.ontimer(lambda: border(my_gameid), 10)

def countdown(my_gameid):
    global counter
    global mbullet
    global sbullet
    global timer
    global points
    global game_running

    if my_gameid != gameid:
        return

    if not game_running:
        return

    counter.clear()

    if timer <= 0:
        counter.write(
            "Time's Up",font=("Arial", 20, "normal"))
        restart()

    else:
        counter.write("Timer: " + str(timer) + "  Points: " + str(points), font=("Arial", 20, "normal"))
        timer -= 1
        screen.ontimer(lambda: countdown(my_gameid), 1000)

def point(my_gameid):
    global yMAX
    global xMAX
    global timer
    global points
    global game_running

    if my_gameid != gameid:
        return

    if not game_running:
        return

    heart_left = heart.xcor() - 20
    heart_right = heart.xcor() + 20
    heart_bottom = heart.ycor() - 20
    heart_top = heart.ycor() + 20

    box_left = box.xcor() - 20
    box_right = box.xcor() + 20
    box_bottom = box.ycor() - 20
    box_top = box.ycor() + 20

    # Check if the two objects overlap
    if (heart_right >= box_left and heart_left <= box_right and heart_top >= box_bottom and heart_bottom <= box_top):
        box.teleport(random.randint(-xMAX + 20, xMAX - 20), random.randint(-yMAX + 20, yMAX - 20))

        timer += 3
        points += 1

    screen.ontimer(lambda: point(my_gameid), 10)


def restart():
    global game_running
    heart.hideturtle()
    box.hideturtle()
    mbullet.hideturtle()
    sbullet.hideturtle()
    screen.bgpic("nopic")
    keys["w"] = False
    keys["s"] = False
    keys["d"] = False
    keys["a"] = False
    game_running = False
    endchoice = t.textinput("Outro","YOU DIE, would you like to play again")

    if (endchoice in ["yes", "Yes", "y", "Y"]):
        game_running = False
        game()

    elif(endchoice in ["no", "No", "n", "N"]):
        sys.exit()

def game():
    startup()
    # GAME ID
    current_gameid = gameid

    screen.listen()
    move(current_gameid)
    border(current_gameid)
    point(current_gameid)
    countdown(current_gameid)
    soun(current_gameid)
    backgroundmusic(current_gameid)

def play():
    global sound
    sound = True
def pause():
    global sound
    sound = False

def soun(my_gameid):
    if my_gameid != gameid:
        return
    if not game_running:
        return
    if sound == True:
        playsound3.playsound("GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav", False)
    screen.ontimer(lambda: soun(my_gameid), 3000)

def backgroundmusic(my_gameid):
    if my_gameid != gameid:
        return
    if not game_running:
        return
    playsound3.playsound("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3", False)
    screen.ontimer(lambda: backgroundmusic(my_gameid), 193000)
screen.onkeypress(upclick, "w")
screen.onkeypress(rightclick, "d")
screen.onkeypress(downclick, "s")
screen.onkeypress(leftclick, "a")
screen.onkeypress(play, "p")

screen.onkeyrelease(uprelease, "w")
screen.onkeyrelease(downrelease, "s")
screen.onkeyrelease(rightrelease, "d")
screen.onkeyrelease(leftrelease, "a")
screen.onkeyrelease(pause, "p")
gamestart()
sbullet.hideturtle()
mbullet.hideturtle()
game()


screen.mainloop()