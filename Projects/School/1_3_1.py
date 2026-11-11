import turtle as t




def Mainloop():
    screen = t.Screen()
    screen.bgpic("Github/Mohameds-Code-Library/Images/random/coverpage.png")
    screen.listen()
    writer = t.Turtle()
    def cool(x, y):
        print(str(x) + ", " + str(y))
        screen.bgpic("Github/Mohameds-Code-Library/Images/random/page.png")
        writer.teleport(100, 100)
        writer.write("hello")
    screen.onscreenclick(cool)
Mainloop()


t.mainloop()
