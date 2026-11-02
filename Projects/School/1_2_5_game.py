import random
import math
import turtle as t
import playsound3 as p
import sys
import leaderboard as lb

class Game():
    def __init__(self, screen=None, new_gameid=0, player_name=None):
        if screen is None:
            self.screen = t.Screen()
        else:
            self.screen = screen

        self.counter = t.Turtle()
        self.player = t.Turtle()
        self.coin = t.Turtle()

        self.x = self.player.xcor()
        self.y = self.player.ycor()
        self.speed = 5
        self.ymax = 300
        self.xmax = 300
        self.package = []
        self.time = 11
        self.score = 0
        self.gameid = 0
        self.game_running = False
        self.timeover = False
        self.leaderboard_file_name =  "GitHub/Mohameds-Code-Library/Projects/School/1_2_5_gameleaderboard.txt"
        self.sounds = ["GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav", "GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav"]

        self.keys = {
            "w": False,
            "a": False,
            "s": False,
            "d": False
        }
        self.gameid = new_gameid
        print(self.gameid)

        #if self.gameid == 0:
            #self.start()
        #else:
            #self.player_name = player_name
            #self.game_running = True
        self.game_running = True

        self.backgroundimg = "GitHub/Mohameds-Code-Library/Images/random/battlebox.png"
        self.screen.bgpic(self.backgroundimg)

        self.counter.hideturtle()
        self.counter.penup()
        self.counter.teleport(0, 300)

        self.player.penup()
        self.heartimg = "GitHub/Mohameds-Code-Library/Images/random/heart.png"
        self.screen.addshape(self.heartimg)
        self.player.shape(self.heartimg)
        self.player_height = 50
        self.player_width = 50

        self.coin.shape("circle")
        self.coin.fillcolor("gold")
        self.coin.shapesize(2)
        self.coin.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
        self.coin_width = 20
        self.coin_height = 20
        while True:
            if -65 < self.coin.xcor() < 65 and -65 < self.coin.ycor() < 65:
                self.coin.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
                continue
            break

        self.meanbox1 = (
            (15, 15),
            (-15, 15),
            (-15, -15),
            (15, -15)
        )

        self.meanboxes = []
        self.sounds = ["GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav", "GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav"]
        self.screen.register_shape("meanbox1", self.meanbox1)
        for _ in range(10):
            self.meanbox = t.Turtle()
            self.meanbox_width = 30
            self.meanbox_height = 30
            self.meanboxes.append(self.meanbox)
            self.meanbox.shape("meanbox1")
            self.meanbox.fillcolor("gold1")
            self.meanbox.showturtle()
            self.meanbox.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
            while True:
                if -65 < self.meanbox.xcor() < 65 and -65 < self.meanbox.ycor() < 65:
                    self.meanbox.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
                    continue
                break
            self.meanbox.seth(random.randint(0, 359))
            self.meanbox.penup()
        self.setup_controls()

    def setup_controls(self):
        self.screen.listen()

        self.screen.onkeypress(lambda: self.click(self.keys, "w"), "w")
        self.screen.onkeypress(lambda: self.click(self.keys, "a"), "a")
        self.screen.onkeypress(lambda: self.click(self.keys, "s"), "s")
        self.screen.onkeypress(lambda: self.click(self.keys, "d"), "d")

        self.screen.onkeyrelease(lambda: self.release(self.keys, "w"), "w")
        self.screen.onkeyrelease(lambda: self.release(self.keys, "a"), "a")
        self.screen.onkeyrelease(lambda: self.release(self.keys, "s"), "s")
        self.screen.onkeyrelease(lambda: self.release(self.keys, "d"), "d")

    def player_movement(self, my_gameid):
        if my_gameid != self.gameid:
            return

        if not self.game_running:
            return

        if self.keys["w"]:
            self.y += self.speed
        if self.keys["s"]:
            self.y -= self.speed
        if self.keys["a"]:
            self.x -= self.speed
        if self.keys["d"]:
            self.x += self.speed

        self.player.goto(self.x, self.y)


    def click(self, keys, key):
        keys[key] = True

    def release(self, keys, key):
        keys[key] = False

    def run(self):
        if not self.game_running:
            return

        self.player_movement(self.gameid)

        self.screen.tracer(32, 10)
        self.screen.update()
        self.screen.ontimer(self.run, 16)

game = Game()

game.run()

t.mainloop()

