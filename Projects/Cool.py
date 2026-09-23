#   a113_flower_alt_color.py
#   This code draws a flower using modulo
#   to alternate every other color
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
"""painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.goto(20,180)

for petal in range(18):
  painter.right(20)
  painter.forward(30)
  painter.color("darkorchid")
  rem = petal % 2
  if (rem == 0):
    painter.color("blue")
  painter.stamp()

painter.goto(16,150)


for petal in range(18):
  painter.right(20)
  painter.forward(20)
  painter.color("SpringGreen")
  rem = petal % 2
  if (rem == 0):
    painter.color("yellow")
  painter.stamp()

painter.goto(12,120)

for petal in range(18):
  painter.right(20)
  painter.forward(10)
  painter.color("violet")
  rem = petal % 2
  if (rem == 0):
    painter.color("OrangeRed")
  painter.stamp()"""





painter.pensize(5)
y = 0
x = 200
for floor in range(630000000):
  painter.penup()
  rem = floor % 9
  rem2 = floor % 21
  if(rem < 3):
    painter.color("gray")
  if(rem > 2 and rem < 6):
    painter.color("blue")
  if(rem > 5):
    painter.color("red")
  if(rem2 == 0 and floor != 0):
    painter.penup()
    x = x - 100
    y = 0
  painter.goto(x,y)
  y = y + 5
  painter.pendown()
  painter.forward(50)




wn = trtl.Screen()
wn.mainloop()