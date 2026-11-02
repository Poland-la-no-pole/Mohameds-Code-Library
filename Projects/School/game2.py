import random
import math
import turtle as t
import playsound3 as p
import sys
import leaderboard as lb
from Scripts import collisions as c
from Scripts import movement as m
from Scripts import utils as u

class Game():
    def __init__(self, screen=None, new_gameid=0, player_name=None):
        if screen is None:
            self.screen = t.Screen()
        else:
            self.screen = screen
        self.collisions = c.Collisions()
        self.movement = m.movement()
        self.utils = u.utils()

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

        if self.gameid == 0:
            self.start()
        else:
            self.player_name = player_name
            self.game_running = True



        self.backgroundimg = "GitHub/Mohameds-Code-Library/Images/random/battlebox.png"
        self.screen.bgpic(self.backgroundimg)

        self.counter = t.Turtle()
        self.counter.hideturtle()
        self.counter.penup()
        self.counter.teleport(0, 300)

        self.player = t.Turtle()
        self.player.penup()
        self.heartimg = "GitHub/Mohameds-Code-Library/Images/random/heart.png"
        self.screen.addshape(self.heartimg)
        self.player.shape(self.heartimg)
        self.player_height = 50
        self.player_width = 50

        self.coin = t.Turtle()
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
        self.movement.setup_controls(self.screen, self.keys)
        self.score_tracker(self.gameid)

    def player_movement(self, my_gameid):
        if my_gameid != self.gameid:
            return

        if not self.game_running:
            return
        
        self.movement.player_movement(self.player, 8, self.keys)

    def border(self, my_gameid):
        if my_gameid != self.gameid:
            return

        if not self.game_running:
            return

        self.collisions.border_wall_collision(self.xmax, self.ymax, self.player, self.player_width, self.player_height)

    def bullet_pattern1(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        
        for meanbox in self.meanboxes:
            self.collisions.border_bounce_collision(self.xmax, self.ymax, meanbox, self.meanbox_width, self.meanbox_height)
            if self.collisions.projectle_player_collision(self.player, self.player_width, self.player_height, meanbox, self.meanbox_width, self.meanbox_height):
                #self.index = (self.meanboxes.index(meanbox))
                #p.playsound(self.sounds[self.index], True)
                return True
            meanbox.forward(4)
        return False
    
    def bullet_pattern2(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False

        for meanbox in self.meanboxes:
            self.collisions.border_bounce_tracking_collision(self.xmax, self.ymax, meanbox, self.meanbox_width, self.meanbox_height, self.player)
            if self.collisions.projectle_player_collision(self.player, self.player_width, self.player_height, meanbox, self.meanbox_width, self.meanbox_height):
                self.index = (self.meanboxes.index(meanbox))
                p.playsound(self.sounds[self.index], True)
                return True
            meanbox.forward(4)
    
    def stop(self):
        self.game_running = False
        self.gameid += 1
        self.screen.clear()

    def start(self):
        self.player_name = t.textinput("name", "Enter your name")
        while "," in self.player_name or len(self.player_name) == 0 or len(self.player_name) > 12:
            self.player_name = t.textinput("Name", "Enter your name without using a comma")
        while True:
            self.startchoice = t.textinput("Intro","This is my game, would you like to play it")
            if (self.startchoice in ["yes", "Yes", "y", "Y"]):
                self.game_running = True
                break
            if(self.startchoice == None):
                sys.exit()
            elif (self.startchoice in ["no", "No", "n", "N"]):
                sys.exit()

    def restart_game(self):
        while True:
            self.choice = t.textinput(
                "Game Over",
                "You lost! Would you like to play again? (yes/no)"
            )

            if(self.choice in ["yes", "Yes", "y", "Y"]):
                break
            if(self.choice == None):
                self.screen.bye()
                sys.exit()
            if(self.choice in ["no", "No", "n", "NO"]):
                self.screen.bye()
                sys.exit()

        new_game = Game(screen=self.screen, new_gameid=self.gameid, player_name=self.player_name)

        new_game.run()

    def points(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        self.time, self.score = self.collisions.point_player_collision(self.xmax, self.ymax, self.player, self.player_width, self.player_height, self.coin, self.coin_width, self.coin_height, self.time, self.score)

    def score_tracker(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        self.time = self.utils.score_tracker(self.counter, self.time, self.score)
        if self.time <= 0:
            self.timeover = True
            return self.timeover
        self.screen.ontimer(lambda: self.score_tracker(self.gameid), 1000)
        return False

    def run(self):
        if not self.game_running:
            return

        self.player_movement(self.gameid)
        self.border(self.gameid)
        self.points(self.gameid)

        if self.timeover:
            self.stop()
            self.restart_game()
            return
        if self.score <= 10:
            lost = self.bullet_pattern1(self.gameid)
            if lost:
                self.stop()
                self.restart_game()
                return
        if 20 > self.score > 10:
            lost = self.bullet_pattern2(self.gameid)
            if lost:
                self.stop()
                self.restart_game()
                return
        self.screen.tracer(32, 10)
        self.screen.update()
        self.screen.ontimer(self.run, 16)

game = Game()

game.run()

t.mainloop()

