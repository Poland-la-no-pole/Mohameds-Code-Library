#poland aka MOHAMED aka MOHAMED AINT POLISH aka POLANDLANOPOLE
import turtle as t
import random
myPen = t.Turtle()
screen = t.Screen()
screen.bgcolor("#3fa652")
myPen.shape("arrow")
myPen.pensize(2)
myPen.speed(10)
myPen.color("white")
myPen.write("Turtle Race!", align='center', font=("Arial", 20, "normal"))
my_turtles = []

def start():
    linemaker = t.Turtle()
    linemaker.teleport(180, 150)
    linemaker.seth(270)
    linemaker.pensize(3)
    linemaker.forward(150)
    linemaker.teleport(-180, 150)
    linemaker.forward(150)
    linemaker.hideturtle()
def turtles():
    # create an empty list of turtles
    global my_turtles
    # use interesting shapes and colors
    turtle_shapes = ["arrow", "turtle", "circle", "square"]
    turtle_colors = ["red", "blue", "green", "orange"]
    new_color = turtle_colors[3]
    for s in turtle_shapes:
        turtle = t.Turtle(shape=s)
        my_turtles.append(turtle)
        new_color = turtle_colors.pop()
        turtle.color(new_color)
        turtle.pencolor(new_color)
def race():
    global my_turtles
    y = 140
    for turtle in my_turtles:
        turtle.teleport(-180, y)
        y -= 30
        turtle.penup()
    racing = True
    while racing:
        turtl = my_turtles[random.randint(0, 3)]
        turtl.goto(turtl.xcor() + random.randint(1, 8), turtl.ycor())
        if turtl.xcor() >= 180:
            racing = False
            turtl.teleport(0, 200)
            turtl.write("this is your winner", align='center', font=("Arial", 20, "normal"))
            break

start()
turtles()
race()

screen.mainloop()