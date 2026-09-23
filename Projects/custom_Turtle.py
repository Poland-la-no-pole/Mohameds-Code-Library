import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Define coordinates for a custom shape (e.g., a diamond/star-like polygon)
# (0, 0) is the center point of your turtle

#Input your own coordinates here
custom_polygon = ( (16, 25),
        (25, 5),
        (0, -25),
        (-25, 5),
        (-16, 25),
        (0, 10),)

# Register the new custom shape and name it "mystar"
wn.register_shape("mystar", custom_polygon)

# Create your turtle and apply the shape
heart = turtle.Turtle()
heart.shape("mystar")
heart.color("darkorchid")
heart.fillcolor("cyan")

# Move it around to test
heart.forward(100)
heart.left(90)
heart.forward(100)

print(heart.xcor(), heart.ycor())

# Keep the window open
wn.mainloop()