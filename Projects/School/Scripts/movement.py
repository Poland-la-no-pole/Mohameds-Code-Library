import turtle as t

class movement:
    def setup_controls(self, screen, keys):
        screen.listen()

        screen.onkeypress(lambda: self.click(keys, "w"), "w")
        screen.onkeypress(lambda: self.click(keys, "a"), "a")
        screen.onkeypress(lambda: self.click(keys, "s"), "s")
        screen.onkeypress(lambda: self.click(keys, "d"), "d")

        screen.onkeyrelease(lambda: self.release(keys, "w"), "w")
        screen.onkeyrelease(lambda: self.release(keys, "a"), "a")
        screen.onkeyrelease(lambda: self.release(keys, "s"), "s")
        screen.onkeyrelease(lambda: self.release(keys, "d"), "d")

    def player_movement(self, player, speed, keys):
        x = player.xcor()
        y = player.ycor()

        if keys["w"]:
            y += speed
        if keys["s"]:
            y -= speed
        if keys["a"]:
            x -= speed
        if keys["d"]:
            x += speed

        player.goto(x, y)


    def click(self, keys, key):
        keys[key] = True

    def release(self, keys, key):
        keys[key] = False

    