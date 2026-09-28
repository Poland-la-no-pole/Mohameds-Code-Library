import turtle as t
import random


screen = t.Screen()

custom_polygon = (
    (30, 30),
    (-30, 30),
    (-30, 15),
    (-40, 15),
    (-40, 0),
    (-30, 0),
    (-30, -30),
    )

# Register the new custom shape and name it "mystar"
screen.register_shape("mystar", custom_polygon)

# Create your turtle and apply the shape
heart = t.Turtle()
heart.shape("mystar")
heart.color("darkorchid")
heart.fillcolor("cyan")

# Move it around to test

heart.right(90)



screen.mainloop()

