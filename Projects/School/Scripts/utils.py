import random
import math
import turtle as t
import playsound3 as p
import sys
import leaderboard as lb

class utils():
    def __init__(self):
        pass

    def score_tracker(self, object, time, score):
        object.clear()
        time -= 1
        object.write("Timer: " + str(time) + "  Points: " + str(score), font=("Arial", 20, "normal"))

        new_time = time
        return new_time