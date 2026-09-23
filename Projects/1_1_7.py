# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "teal", "gray"]
new_color = turtle_colors[7]
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)
    new_color = turtle_colors.pop()
    t.color(new_color)
    t.pencolor(new_color)

#
startx = 0
starty = 0
heading = 0
move = 50

#
for t in my_turtles:
    t.teleport(startx, starty)
    t.seth(heading + 45)
    t.forward(50)
    move += 15

#
    startx = t.xcor()
    starty = t.ycor()
    heading += 45


wn = trtl.Screen()
wn.mainloop()