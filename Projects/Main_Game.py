import turtle as t
import random
import tkinter as tk
from tkinter import messagebox

#set up our objects
heart = t.Turtle()
sA1 = t.Turtle()
root = tk.Tk()
root.withdraw()
w = 0
#sets up our screen and background
screen = t.Screen()
#sets up our turtles
heart1 = "GitHub/Mohameds-Code-Library/Photos/heart.gif"
screen.addshape(heart1)
heart.shape(heart1)


smallArrow1 = "GitHub/Mohameds-Code-Library/Photos/smallArrow1.png"
screen.addshape(smallArrow1)
sA1.shape(smallArrow1)
#sets up our cord maxes
yMAX = 300
xMAX = 300
#setting up our functions

#sets keys to values of true and false for each letter
keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}


        (heart.xcor() + 25,heart.ycor() + 5),

cords = [
    (heart.xcor() + 16,heart.ycor() + 25),
    (heart.xcor() + 25,heart.ycor() + 5),
    (heart.xcor(), heart.ycor() - 25),
    (heart.xcor() - 25, heart.ycor() + 5),
    (heart.xcor() - 16, heart.ycor() + 25),
    (heart.xcor(), heart.ycor() + 10),
    ]
    


# each changes the value of keys
def upclick():
    keys["w"] = True
def downclick():
    keys["s"] = True
def rightclick():
    keys["d"] = True
def leftclick():
    keys["a"] = True
def uprelease():
    keys["w"] = False
def downrelease():
    keys["s"] = False
def rightrelease():
    keys["d"] = False
def leftrelease():
    keys["a"] = False

#is our movement function
def move():
    #sets x and y to the cordanates of our heart
    y = heart.ycor()
    x = heart.xcor()
    # these if stayments check if the value of the letter in keys is true or false
    if(keys["w"]):
        y +=4
    if(keys["s"] == True):
        y -=4
    if(keys["d"]):
        x +=4
    if(keys["a"] == True):
        x -=4
    heart.goto(x, y)


    #is a timer that runs move ever 10 milliseconds
    screen.ontimer(move, 10)
def border():


    screen.ontimer(border, 10)



#sets up our keyboard to listen
screen.listen()
#sets keybinds to functions
screen.onkeypress(upclick, "w")
screen.onkeypress(rightclick, "d")
screen.onkeypress(downclick, "s")
screen.onkeypress(leftclick, "a")


screen.onkeyrelease(uprelease, "w")
screen.onkeyrelease(rightrelease, "d")
screen.onkeyrelease(downrelease, "s")
screen.onkeyrelease(leftrelease, "a")





heart.penup()
move()
border()

wn = screen
wn.mainloop()
