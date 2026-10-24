import random
import math
import turtle as t
import playsound3 as p
import sys
def setup():
    screen = t.Screen()

    heart = t.Turtle()
    bullets = []

    backgroundimg = "GitHub/Mohameds-Code-Library/Images/random/battlebox.png"
    screen.bgpic(backgroundimg)

    heartimg = "GitHub/Mohameds-Code-Library/Images/random/heart.png"
    screen.addshape(heartimg)
    heart.shape(heartimg)

    for _ in range(10):
        bullet = t.Turtle()
        bulletimg = "GitHub/Mohameds-Code-Library/Images/random/mbullet.png"
        screen.addshape(bulletimg)
        bullet.shape(bulletimg)
        bullets.append(bullet)


setup()



wn = t.Screen()
wn.mainloop()