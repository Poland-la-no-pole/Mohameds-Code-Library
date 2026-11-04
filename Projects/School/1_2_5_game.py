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
        self.screen.title("larptale")

        self.counter = t.Turtle()
        self.player = t.Turtle()
        self.coin = t.Turtle()


        self.playerspeed = 8
        self.ymax = 300
        self.xmax = 300

        self.time = 11
        self.score = 0
        self.gameid = 0
        self.game_running = False
        self.timeover = False
        self.leaderboard_file_name =  "GitHub/Mohameds-Code-Library/Projects/School/1_2_5_gameleaderboard.txt"
        self.leader_names_list = []
        self.leader_scores_list = []
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
            self.game_running = True
        else:
            self.player_name = player_name
            self.game_running = True
        
        self.setup_controls()

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
        self.player_top_hitbox_height = 10
        self.player_top_hitbox_width = 30
        self.player_bottom_hitbox_height = 10
        self.player_bottom_hitbox_width = 10

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


        self.meanboxes = []
        self.meanboxes_x_speeds = []
        self.meanboxes_y_speeds = []
        self.meanboxes_hypotenuse_speeds = []
        self.sounds = ["GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav", "GitHub/Mohameds-Code-Library/Audios/anything.wav", "GitHub/Mohameds-Code-Library/Audios/chaos.wav", "GitHub/Mohameds-Code-Library/Audios/jarona.wav", "GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav", "GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav"]
        for i in range(10):
            self.meanbox = t.Turtle()
            self.meanbox_radius = 25
            self.meanboxes.append(self.meanbox)
            self.meanbox.shape("circle")
            self.meanbox.shapesize(2)
            self.meanbox.fillcolor("blue1")
            self.meanbox.showturtle()
            self.meanbox.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
            self.meanbox_x_speed = random.choice((-4, 4))
            self.meanbox_y_speed = random.choice((-4, 4))
            self.meanboxes_x_speeds.append(self.meanbox_x_speed)
            self.meanboxes_y_speeds.append(self.meanbox_y_speed)
            self.meanbox_hypotenuse = math.sqrt((self.meanboxes_x_speeds[i] ** 2) + (self.meanboxes_y_speeds[i] ** 2))
            self.meanboxes_hypotenuse_speeds.append(self.meanbox_hypotenuse)
            while True:
                if -100 < self.meanbox.xcor() < 100 and -100 < self.meanbox.ycor() < 100:
                    self.meanbox.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
                    continue
                for i, meanbox in enumerate(self.meanboxes):
                    meanbox_right = meanbox.xcor() + self.meanbox_radius/ 2
                    meanbox_left = meanbox.xcor() - self.meanbox_radius / 2
                    meanbox_top = meanbox.ycor() + self.meanbox_radius / 2
                    meanbox_bottom = meanbox.ycor() - self.meanbox_radius / 2
                    for e, meanboxx in enumerate(self.meanboxes[i + 1:], i + 1):
                        meanboxx_right = meanboxx.xcor() + self.meanbox_radius / 2
                        meanboxx_left = meanboxx.xcor() - self.meanbox_radius / 2
                        meanboxx_top = meanboxx.ycor() + self.meanbox_radius / 2
                        meanboxx_bottom = meanboxx.ycor() - self.meanbox_radius / 2
                        if(meanboxx_right >= meanbox_left and meanboxx_left <= meanbox_right and meanboxx_top >= meanbox_bottom and meanboxx_bottom <= meanbox_top):
                            meanbox.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
                            meanboxx.teleport(random.randint(-self.xmax + 20, self.xmax - 20),random.randint(-self.ymax + 20, self.ymax - 20))
                break
            self.meanbox.penup()

        self.score_tracker(self.gameid)

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
            self.player.sety(self.player.ycor() + self.playerspeed)
        if self.keys["s"]:
            self.player.sety(self.player.ycor() - self.playerspeed)
        if self.keys["a"]:
            self.player.setx(self.player.xcor() - self.playerspeed)
        if self.keys["d"]:
            self.player.setx(self.player.xcor() + self.playerspeed)

    def click(self, keys, key):
        keys[key] = True

    def release(self, keys, key):
        keys[key] = False

    def border(self, my_gameid):
        if my_gameid != self.gameid:
            return

        if not self.game_running:
            return

        player_right = self.player.xcor() + self.player_width/2
        player_left = self.player.xcor() - self.player_width/2
        player_top = self.player.ycor() + self.player_height/2
        player_bottom = self.player.ycor() - self.player_height/2

        if player_right > self.xmax:
            self.player.setx(self.xmax - self.player_width/2)
            

        if player_left < -self.xmax:
            self.player.setx(-self.xmax + self.player_width/2)

        if player_top > self.ymax:
            self.player.sety(self.ymax - self.player_height/2)

        if player_bottom < -self.ymax:
            self.player.sety(-self.ymax + self.player_height/2)

    def projectle_player_collision(self):
        player_top_right = self.player.xcor() + self.player_top_hitbox_width / 2
        player_top_left = self.player.xcor() - self.player_top_hitbox_width / 2
        player_top_top = self.player.ycor() + self.player_top_hitbox_height
        player_top_bottom = self.player.ycor()
        player_bottom_right = self.player.xcor() + self.player_bottom_hitbox_width / 2
        player_bottom_left = self.player.xcor() - self.player_bottom_hitbox_width / 2
        player_bottom_top = self.player.ycor()
        player_bottom_bottom = self.player.ycor() - self.player_bottom_hitbox_height
        for meanbox in self.meanboxes:
            meanbox_right = meanbox.xcor() + self.meanbox_radius
            meanbox_left = meanbox.xcor() - self.meanbox_radius
            meanbox_top = meanbox.ycor() + self.meanbox_radius
            meanbox_bottom = meanbox.ycor() - self.meanbox_radius


            if(player_top_right >= meanbox_left and player_top_left <= meanbox_right and player_top_top >= meanbox_bottom and player_top_bottom <= meanbox_top):
                return True
            if(player_bottom_right >= meanbox_left and player_bottom_left <= meanbox_right and player_bottom_top >= meanbox_bottom and player_bottom_bottom <= meanbox_top):
                return True
        return False

    def projectle_projectle_collision(self):
        for i, meanbox in enumerate(self.meanboxes):
            meanbox_right = meanbox.xcor() + self.meanbox_radius
            meanbox_left = meanbox.xcor() - self.meanbox_radius
            meanbox_top = meanbox.ycor() + self.meanbox_radius
            meanbox_bottom = meanbox.ycor() - self.meanbox_radius
            for e, meanboxx in enumerate(self.meanboxes[i+1:], i+1):
                meanboxx_right = meanboxx.xcor() + self.meanbox_radius
                meanboxx_left = meanboxx.xcor() - self.meanbox_radius
                meanboxx_top = meanboxx.ycor() + self.meanbox_radius
                meanboxx_bottom = meanboxx.ycor() - self.meanbox_radius
                if(meanboxx_right >= meanbox_left and meanboxx_left <= meanbox_right and meanboxx_top >= meanbox_bottom and meanboxx_bottom <= meanbox_top):
                    overlap_x = min(meanbox_right, meanboxx_right) - max(meanbox_left, meanboxx_left)
                    overlap_y = min(meanbox_top, meanboxx_top) - max(meanbox_bottom, meanboxx_bottom)
                    if overlap_x < overlap_y:
                        if meanbox.xcor() < meanboxx.xcor(): #left for meanbox, right for meanboxx
                            meanbox.setx((meanbox.xcor() - overlap_x / 2) - 1)
                            meanboxx.setx((meanboxx.xcor() + overlap_x / 2) + 1)

                            self.meanboxes_x_speeds[i] = -abs(self.meanboxes_x_speeds[i])
                            self.meanboxes_x_speeds[e] = abs(self.meanboxes_x_speeds[e])

                            if self.meanboxes_y_speeds[i] < 0:
                                self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                            
                            if self.meanboxes_y_speeds[i] > 0:
                                self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))

                            if self.meanboxes_y_speeds[e] < 0:
                                self.meanboxes_y_speeds[e] = -math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_x_speeds[e] ** 2))
                            
                            if self.meanboxes_y_speeds[e] > 0:
                                self.meanboxes_y_speeds[e] = math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_x_speeds[e] ** 2))
                        else: #left for meanboxx, right for meanbox
                            meanbox.setx((meanbox.xcor() + overlap_x / 2) + 1)
                            meanboxx.setx((meanboxx.xcor() - overlap_x / 2) - 1)

                            self.meanboxes_x_speeds[i] = abs(self.meanboxes_x_speeds[i])
                            self.meanboxes_x_speeds[e] = -abs(self.meanboxes_x_speeds[e])

                            if self.meanboxes_y_speeds[i] < 0:
                                self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                            
                            if self.meanboxes_y_speeds[i] > 0:
                                self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))

                            if self.meanboxes_y_speeds[e] < 0:
                                self.meanboxes_y_speeds[e] = -math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_x_speeds[e] ** 2))
                            
                            if self.meanboxes_y_speeds[e] > 0:
                                self.meanboxes_y_speeds[e] = math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_x_speeds[e] ** 2))
                    else:
                        if meanbox.ycor() < meanboxx.ycor(): #down for meanbox, up for meanboxx
                            meanbox.sety((meanbox.ycor() - overlap_y / 2) - 1)
                            meanboxx.sety((meanboxx.ycor() + overlap_y / 2) + 1)

                            self.meanboxes_y_speeds[i] = -abs(self.meanboxes_y_speeds[i])
                            self.meanboxes_y_speeds[e] = abs(self.meanboxes_y_speeds[e])

                            if self.meanboxes_x_speeds[i] < 0:
                                self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                            
                            if self.meanboxes_x_speeds[i] > 0:
                                self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))

                            if self.meanboxes_x_speeds[e] < 0:
                                self.meanboxes_x_speeds[e] = -math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_y_speeds[e] ** 2))
                            
                            if self.meanboxes_x_speeds[e] > 0:
                                self.meanboxes_x_speeds[e] = math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_y_speeds[e] ** 2))
                        else: #up for meanbox, down for meanboxx
                            meanbox.sety((meanbox.ycor() + overlap_y / 2) + 1)
                            meanboxx.sety((meanboxx.ycor() - overlap_y / 2) - 1)

                            self.meanboxes_y_speeds[i] = abs(self.meanboxes_y_speeds[i])
                            self.meanboxes_y_speeds[e] = -abs(self.meanboxes_y_speeds[e])

                            if self.meanboxes_x_speeds[i] < 0:
                                self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                            
                            if self.meanboxes_x_speeds[i] > 0:
                                self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))

                            if self.meanboxes_x_speeds[e] < 0:
                                self.meanboxes_x_speeds[e] = -math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_y_speeds[e] ** 2))
                            
                            if self.meanboxes_x_speeds[e] > 0:
                                self.meanboxes_x_speeds[e] = math.sqrt((self.meanboxes_hypotenuse_speeds[e] ** 2) - (self.meanboxes_y_speeds[e] ** 2))

    def bullet_pattern1(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        for i, meanbox in enumerate(self.meanboxes):
            meanbox_right = meanbox.xcor() + self.meanbox_radius
            meanbox_left = meanbox.xcor() - self.meanbox_radius
            meanbox_top = meanbox.ycor() + self.meanbox_radius
            meanbox_bottom = meanbox.ycor() - self.meanbox_radius

            if meanbox_right >= self.xmax:
                meanbox.setx(self.xmax - self.meanbox_radius)
                self.meanboxes_x_speeds[i] = -abs(self.meanboxes_x_speeds[i])
                
                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                
                if self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_left <= -self.xmax:
                meanbox.setx(-self.xmax + self.meanbox_radius)
                self.meanboxes_x_speeds[i] = abs(self.meanboxes_x_speeds[i])
                
                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                
                if self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_top >= self.ymax:
                meanbox.sety(self.ymax - self.meanbox_radius)
                self.meanboxes_y_speeds[i] = -abs(self.meanboxes_y_speeds[i])
                
                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                
                if self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_bottom <= -self.ymax:
                meanbox.sety(-self.ymax + self.meanbox_radius)
                self.meanboxes_y_speeds[i] = abs(self.meanboxes_y_speeds[i])
                
                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                
                if self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)
            meanbox.goto(meanbox.xcor() + self.meanboxes_x_speeds[i], meanbox.ycor() + self.meanboxes_y_speeds[i])
        if self.projectle_player_collision():
            #self.index = (self.meanboxes.index(meanbox))
            #p.playsound(self.sounds[self.index], False)
            return True
        return False

    def bullet_pattern2(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        for i, meanbox in enumerate(self.meanboxes):
            meanbox_right = meanbox.xcor() + self.meanbox_radius
            meanbox_left = meanbox.xcor() - self.meanbox_radius
            meanbox_top = meanbox.ycor() + self.meanbox_radius
            meanbox_bottom = meanbox.ycor() - self.meanbox_radius

            if meanbox_right >= self.xmax:
                meanbox.setx(self.xmax - self.meanbox_radius)
                self.meanboxes_x_speeds[i] = -abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] + 1.5)))
                
                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                
                if self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_left <= -self.xmax:
                meanbox.setx(-self.xmax + self.meanbox_radius)
                self.meanboxes_x_speeds[i] = abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] - 1.5), min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] + 1.5)))
                
                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                
                if self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_top >= self.ymax:
                meanbox.sety(self.ymax - self.meanbox_radius)
                self.meanboxes_y_speeds[i] = -abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] + 1.5)))
                
                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                
                if self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_bottom <= -self.ymax:
                meanbox.sety(-self.ymax + self.meanbox_radius)
                self.meanboxes_y_speeds[i] = abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] + 1.5)))
                
                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                
                if self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)
            self.projectle_projectle_collision()
            meanbox.goto(meanbox.xcor() + self.meanboxes_x_speeds[i], meanbox.ycor() + self.meanboxes_y_speeds[i])
        if self.projectle_player_collision():
            #self.index = (self.meanboxes.index(meanbox))
            #p.playsound(self.sounds[self.index], False)
            return True
        return False

    def bullet_pattern3(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        for i, meanbox in enumerate(self.meanboxes):
            meanbox_right = meanbox.xcor() + self.meanbox_radius
            meanbox_left = meanbox.xcor() - self.meanbox_radius
            meanbox_top = meanbox.ycor() + self.meanbox_radius
            meanbox_bottom = meanbox.ycor() - self.meanbox_radius

            wanted_x = self.player.xcor() - meanbox.xcor()
            wanted_y = self.player.ycor() - meanbox.ycor()
            if i % 2 == 1:
                if wanted_y > 0:
                    self.meanboxes_y_speeds[i] += 1

                if wanted_y < 0:
                    self.meanboxes_y_speeds[i] -= 1

                if wanted_x > 0:
                    self.meanboxes_x_speeds[i] += 1

                if wanted_x < 0:
                    self.meanboxes_x_speeds[i] -= 1

                current_speed = math.hypot(
                    self.meanboxes_x_speeds[i],
                    self.meanboxes_y_speeds[i]
                )

                if current_speed != 0:
                    self.meanboxes_x_speeds[i] *= (
                        self.meanboxes_hypotenuse_speeds[i] / current_speed
                    )

                    self.meanboxes_y_speeds[i] *= (
                        self.meanboxes_hypotenuse_speeds[i] / current_speed
                    )

            if meanbox_right >= self.xmax:
                meanbox.setx(self.xmax - self.meanbox_radius)
                self.meanboxes_x_speeds[i] = -abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] + 1.5)))
                
                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                
                if self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_left <= -self.xmax:
                meanbox.setx(-self.xmax + self.meanbox_radius)
                self.meanboxes_x_speeds[i] = abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_x_speeds[i] + 1.5)))
                
                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                
                if self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_x_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_top >= self.ymax:
                meanbox.sety(self.ymax - self.meanbox_radius)
                self.meanboxes_y_speeds[i] = -abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] + 1.5)))
                
                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                
                if self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

            if meanbox_bottom <= -self.ymax:
                meanbox.sety(-self.ymax + self.meanbox_radius)
                self.meanboxes_y_speeds[i] = abs(random.uniform(max(-self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] - 1.5),min(self.meanboxes_hypotenuse_speeds[i], self.meanboxes_y_speeds[i] + 1.5)))
                
                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] = -math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                
                if self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] = math.sqrt((self.meanboxes_hypotenuse_speeds[i] ** 2) - (self.meanboxes_y_speeds[i] ** 2))
                p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)
            self.projectle_projectle_collision()
            meanbox.goto(meanbox.xcor() + self.meanboxes_x_speeds[i], meanbox.ycor() + self.meanboxes_y_speeds[i])
        if self.projectle_player_collision():
            #self.index = (self.meanboxes.index(meanbox))
            #p.playsound(self.sounds[self.index], False)
            return True
        return False

    def start(self):
        self.player_name = t.textinput("name", "Enter your name")
        while "," in self.player_name or len(self.player_name) == 0 or len(self.player_name) > 12:
            self.player_name = t.textinput("Name", "Enter your name without using a comma")
        while True:
            self.startchoice = t.textinput("Intro","This is my game, would you like to play it(yes or no please. btw you can use wasd to move, get the coin)")
            if (self.startchoice in ["yes", "Yes", "y", "Y"]):
                self.game_running = True
                break
            if(self.startchoice == None):
                sys.exit()
            elif (self.startchoice in ["no", "No", "n", "N"]):
                sys.exit()

    def stop(self):
        self.game_running = False
        self.gameid += 1
        self.screen.clear()

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

    def score_tracker(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        
        self.counter.clear()
        self.time -= 1
        self.counter.write("Timer: " + str(self.time) + "  Points: " + str(self.score), font=("Arial", 20, "normal"))
        if self.time <= 0:
            self.timeover = True
            return self.timeover
        self.screen.ontimer(lambda: self.score_tracker(self.gameid), 1000)
        return self.time

    def points(self, my_gameid):
        if my_gameid != self.gameid:
            return False

        if not self.game_running:
            return False
        
        player_right = self.player.xcor() + self.player_width / 2
        player_left = self.player.xcor() - self.player_width / 2
        player_top = self.player.ycor() + self.player_height / 2
        player_bottom = self.player.ycor() - self.player_height / 2

        point_right = self.coin.xcor() + self.coin_width / 2
        point_left = self.coin.xcor() - self.coin_width / 2
        point_top = self.coin.ycor() + self.coin_height / 2
        point_bottom = self.coin.ycor() - self.coin_height / 2
        if (player_right >= point_left and player_left <= point_right and player_top >= point_bottom and player_bottom <= point_top):
            self.coin.teleport(random.randint(-self.xmax + 20, self.xmax - 20), random.randint(-self.ymax+ 20, self.ymax - 20))
            self.time += 3
            self.score += 1
            for i, meanbox in enumerate(self.meanboxes):
                increase = self.score / 100

                if self.meanboxes_x_speeds[i] < 0:
                    self.meanboxes_x_speeds[i] -= increase
                elif self.meanboxes_x_speeds[i] > 0:
                    self.meanboxes_x_speeds[i] += increase

                if self.meanboxes_y_speeds[i] < 0:
                    self.meanboxes_y_speeds[i] -= increase
                elif self.meanboxes_y_speeds[i] > 0:
                    self.meanboxes_y_speeds[i] += increase

                self.meanboxes_hypotenuse_speeds[i] = math.sqrt((self.meanboxes_x_speeds[i] ** 2) + (self.meanboxes_y_speeds[i] ** 2))


            p.playsound("GitHub/Mohameds-Code-Library/Audios/jarona.wav", False)
        return (self.time, self.score)

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

        if self.score <= 7:
            lost = self.bullet_pattern1(self.gameid)
            if lost:
                self.stop()
                self.restart_game()
                return

        if 14 >= self.score > 7:
            lost = self.bullet_pattern2(self.gameid)
            if lost:
                self.stop()
                self.restart_game()
                return
        if 21 >= self.score > 14:
            lost = self.bullet_pattern3(self.gameid)
            if lost:
                self.stop()
                self.restart_game()
                return

        self.screen.tracer(0)
        self.screen.update()
        self.screen.ontimer(self.run, 16)

game = Game()

game.run()

t.mainloop()




#well rn it seems like the issue is just your timers are messing with each other, the code itself isnt wrong since it just moves itZ