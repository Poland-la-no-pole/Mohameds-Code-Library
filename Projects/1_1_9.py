import turtle as t
import random


screen = t.Screen()

custom_polygon = (
    (100, 100),
    (100, 0),
    (0, 100)
    )

# Register the new custom shape and name it "mystar"
screen.register_shape("mystar", custom_polygon)

# Create your turtle and apply the shape
heart = t.Turtle()
heart.shape("mystar")
heart.color("darkorchid")
heart.fillcolor("cyan")

# Move it around to test





screen.mainloop()

