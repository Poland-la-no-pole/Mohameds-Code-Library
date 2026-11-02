import random
import math
import turtle as t
import playsound3 as p
import sys
import leaderboard as lb

class Collisions():
    def border_wall_collision(self, borderx, bordery, object, object_width, object_height):
        object_right = object.xcor() + object_width/2
        object_left = object.xcor() - object_width/2
        object_top = object.ycor() + object_height/2
        object_bottom = object.ycor() - object_height/2

        if object_right > borderx:
            object.setx(borderx - object_width/2)

        if object_left < -borderx:
            object.setx(-borderx + object_width/2)

        if object_top > bordery:
            object.sety(bordery - object_height/2)

        if object_bottom < -bordery:
            object.sety(-bordery + object_height/2)

    def border_bounce_collision(self, borderx, bordery, object, object_width, object_height):
        object_right = object.xcor() + object_width / 2
        object_left = object.xcor() - object_width / 2
        object_top = object.ycor() + object_height / 2
        object_bottom = object.ycor() - object_height / 2

        angle = object.heading()


        if object_right >= borderx:
            object.setx(borderx - object_width / 2)
            object.setheading(180 - angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

        if object_left <= -borderx:
            object.setx(-borderx + object_width / 2)
            object.setheading(180 - angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

        if object_top >= bordery:
            object.sety(bordery - object_height / 2)
            object.setheading(-angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

        if object_bottom <= -bordery:
            object.sety(-bordery + object_height / 2)
            object.setheading(-angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

    def border_bounce_tracking_collision(self, borderx, bordery, object, object_width, object_height, player):
        object_right = object.xcor() + object_width / 2
        object_left = object.xcor() - object_width / 2
        object_top = object.ycor() + object_height / 2
        object_bottom = object.ycor() - object_height / 2

        angle = object.heading()


        if object_right >= borderx:
            object.setx(borderx - object_width / 2)
            angle = math.degrees(math.atan2(player.ycor() - object.ycor(),player.xcor() - object.xcor()))
            object.seth(angle)

        if object_left <= -borderx:
            object.setx(-borderx + object_width / 2)
            angle = math.degrees(math.atan2(player.ycor() - object.ycor(),player.xcor() - object.xcor()))
            object.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

        if object_top >= bordery:
            object.sety(bordery - object_height / 2)
            angle = math.degrees(math.atan2(player.ycor() - object.ycor(),player.xcor() - object.xcor()))
            object.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

        if object_bottom <= -bordery:
            object.sety(-bordery + object_height / 2)
            angle = math.degrees(math.atan2(player.ycor() - object.ycor(),player.xcor() - object.xcor()))
            object.seth(angle)
            p.playsound("GitHub/Mohameds-Code-Library/Audios/bounce.wav", False)

    def projectle_player_collision(self, player, player_width, player_height, projectle, projectle_width, projectle_height):
        player_right = player.xcor() + player_width / 2
        player_left = player.xcor() - player_width / 2
        player_top = player.ycor() + player_height / 2
        player_bottom = player.ycor() - player_height / 2
    
        projectle_right = projectle.xcor() + projectle_width / 2
        projectle_left = projectle.xcor() - projectle_width / 2
        projectle_top = projectle.ycor() + projectle_height / 2
        projectle_bottom = projectle.ycor() - projectle_height / 2


        if(player_right >= projectle_left and player_left <= projectle_right and player_top >= projectle_bottom and player_bottom <= projectle_top):
            return True
        return False

    def point_player_collision(self, borderx, bordery, player, player_width, player_height, point, point_width, point_height, time, score):
        player_right = player.xcor() + player_width / 2
        player_left = player.xcor() - player_width / 2
        player_top = player.ycor() + player_height / 2
        player_bottom = player.ycor() - player_height / 2

        point_right = point.xcor() + point_width / 2
        point_left = point.xcor() - point_width / 2
        point_top = point.ycor() + point_height / 2
        point_bottom = point.ycor() - point_height / 2
        if (player_right >= point_left and player_left <= point_right and player_top >= point_bottom and player_bottom <= point_top):
            point.teleport(random.randint(-borderx + 20, borderx - 20), random.randint(-bordery + 20, bordery - 20))
            time += 4
            score += 1
            p.playsound("GitHub/Mohameds-Code-Library/Audios/jarona.wav", False)
        new_time = time
        new_score = score
        return (new_time, new_score)

