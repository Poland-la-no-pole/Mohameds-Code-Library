import random
import math
import turtle as t
import playsound3 as p
import sys
import leaderboard as lb

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
gameid = 0
current_gameid = 0
game_running = False
leaderboard_file_name =  "GitHub/Mohameds-Code-Library/Projects/School/1_2_5_gameleaderboard.txt"

keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}
def gamestart():
    player_name = t.textinput("name", "Enter your name")
    while True:
        while "," in player_name or len(player_name) == 0 or len(player_name) > 12:
            player_name = t.textinput("Name", "Enter your name without using a comma")
        startchoice = t.textinput("Intro","This is my game, would you like to play it")
        if (startchoice in ["yes", "Yes", "y", "Y"]):
            break
        elif (startchoice in ["no", "No", "n", "N"]):
            sys.exit()
def manage_leaderboard():
    global score
    global spot
    global player_name

# get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

# show the leaderboard with or without the current player
    if (len(leader_scores_list) < 5 or score >= int(leader_scores_list[4])):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)
    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
def startup():
    global game_running
    global gameid

    game_running = True
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

    meanboxes = []
    sounds = ["GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav", "GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav"]
    screen.register_shape("meanbox1", meanbox1)
    for _ in range(10):
        meanbox = t.Turtle()
        meanboxes.append(meanbox)
        meanbox.shape("meanbox1")
        meanbox.fillcolor("gold1")
        meanbox.showturtle()
        meanbox.teleport(random.randint(-xmax + 20, xmax - 20),random.randint(-ymax + 20, ymax - 20))
        if -65 < meanbox.xcor() < 65 and -65 < meanbox.ycor() < 65:
            meanbox.teleport(random.randint(-xmax + 20, xmax - 20),random.randint(-ymax + 20, ymax - 20))
        meanbox.seth(random.randint(0, 359))
        meanbox.penup()


    # GAME ID
    gameid += 1

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
    global player
def border():
    global playerx
    global playery
    global bulletx
    global bullety
    global player

    player_right = player.xcor() + 25
    player_left = player.xcor() - 25
    player_top = player.ycor() + 25
    player_bottom = player.ycor() - 25
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

def meanbox_pattern1():
    global meanboxes
    for meanbox in meanboxes:
        meanbox.forward(4)
    for meanbox in meanboxes:
        meanbox_right = meanbox.xcor() + 15
        meanbox_left = meanbox.xcor() - 15
        meanbox_top = meanbox.ycor() + 15
        meanbox_bottom = meanbox.ycor() - 15
        if meanbox_right >= xmax:
            meanbox.setx(xmax - 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)
        if meanbox_left <= -xmax:
            meanbox.setx(-xmax + 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)
        if meanbox_top >= ymax:
            meanbox.sety(ymax - 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)
        if meanbox_bottom <= -ymax:
            meanbox.sety(-ymax + 15)
            angle = math.degrees(math.atan2(player.ycor() - meanbox.ycor(),player.xcor() - meanbox.xcor()))
            meanbox.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

    screen.update()

def meanbox_pattern2():
    for meanbox in meanboxes:
        meanbox.forward(10)
    screen.update()

def points():
    global timer
    global point
    global box
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
    global sounds
    global meanboxes
    global meanbox
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
            index = (meanboxes.index(meanbox))
            p.playsound(sounds[index], True)
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
    screen.ontimer(lambda: countdown(gameid), 1000)

def restart():
    global game_running
    player.hideturtle()
    box.hideturtle()
    meanbox.hideturtle()
    screen.bgpic("nopic")
    keys["w"] = False
    keys["s"] = False
    keys["d"] = False
    keys["a"] = False
    game_running = False
    endchoice = t.textinput("Outro","YOU DIE, would you like to play again")

    if (endchoice in ["yes", "Yes", "y", "Y"]):
        game_running = False

    elif(endchoice in ["no", "No", "n", "N"]):
        sys.exit()


def gameloop():
    global point
    player_movement()
    meanbox_pattern1()
    border()
    points()
    collision()
    screen.ontimer(gameloop, 16)

gamestart()

screen.listen()

screen.onkeypress(upclick, "w")
screen.onkeypress(rightclick, "d")
screen.onkeypress(downclick, "s")
screen.onkeypress(leftclick, "a")

screen.onkeyrelease(uprelease, "w")
screen.onkeyrelease(downrelease, "s")
screen.onkeyrelease(rightrelease, "d")
screen.onkeyrelease(leftrelease, "a")


startup()

countdown()

gameloop()

screen.tracer(32, 16)

wn = t.Screen()
wn.mainloop()