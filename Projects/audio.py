import turtle
import playsound3
screen = turtle.Screen()
sound = False
def play():
    global sound
    sound = True
def pause():
    global sound
    sound = False
def soun():
    if sound == True:
        playsound3.playsound("GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav", False)
    screen.ontimer(soun, 1)
screen.listen()
screen.onkeypress(play, "o")
screen.onkeyrelease(pause, "o")
soun()
screen.mainloop()