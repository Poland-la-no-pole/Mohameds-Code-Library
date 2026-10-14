import sys
import math
import pygame
import random
import time


class Game:
    def __init__(self):
        pygame.init()

        self.heartx = 400
        self.hearty = 400
        self.border_x = 800
        self.border_y = 800

        pygame.display.set_caption("Hello")
        self.screen = pygame.display.set_mode(
            (self.border_x, self.border_y)
        )
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/gerson.gif")
        self.battlebox = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/battlebox.png")

        # Load the heart with transparency
        self.heart = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/heart.png").convert_alpha()

        # Crop away transparent padding around the heart
        visible_rect = self.heart.get_bounding_rect()
        self.heart = self.heart.subsurface(visible_rect).copy()

        # Create the heart's rectangle and pixel mask
        self.heart_rect = self.heart.get_rect(center=(self.heartx, self.hearty))
        self.heart_mask = pygame.mask.from_surface(self.heart)

        # Load the original bullet image
        self.original_bullet = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/mbullet.png").convert_alpha()

        self.battlebox_rect = self.battlebox.get_rect( center=(self.border_x // 2, self.border_y // 2))

        # Creates independent bullets
        self.bullets = []

        for _ in range(0):
            bullet = {
                "x": 700, #random.randint(self.battlebox_rect.left + 20,self.battlebox_rect.right - 20),
                "y": 700,     #random.randint(self.battlebox_rect.top + 20,self.battlebox_rect.bottom - 20),
                "dx": random.choice([-2.0, 2.0]),
                "dy": random.choice([-2.0, 2.0]),
                "image": self.original_bullet,
                "mask": pygame.mask.from_surface(self.original_bullet),
                "bounced": False,
            }

            self.bullets.append(bullet)

        # Heart movement controls
        self.heartmovementup = False
        self.heartmovementdown = False
        self.heartmovementleft = False
        self.heartmovementright = False
        self.gravity = .5
        self.velocityy = 0
        self.velocityx = 0
        self.jumping = False
        self.grounded = False
        self.hello = 1
        self.bye = 0

        self.music = pygame.Sound("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3")
        self.sound1 = pygame.Sound("GitHub/Mohameds-Code-Library/Audios/bounce.wav")
        self.sound1.set_volume(.2)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_w:
                    #    self.heartmovementup = True
                    #if event.key == pygame.K_s:
                    #    self.heartmovementdown = True
                    if event.key == pygame.K_w:
                            self.jumping = True
                            self.grounded = False
                    if event.key == pygame.K_a:
                        self.heartmovementleft = True
                    if event.key == pygame.K_d:
                        self.heartmovementright = True
                if event.type == pygame.KEYUP:
                    #if event.key == pygame.K_w:
                    #    self.heartmovementup = False
                    #if event.key == pygame.K_s:
                    #    self.heartmovementdown = False
                    if event.key == pygame.K_a:
                        self.heartmovementleft = False
                    if event.key == pygame.K_d:
                        self.heartmovementright = False

                    if event.key == pygame.K_SPACE:
                        if pygame.mixer.get_busy():
                            pygame.mixer.pause()
                        else:
                            pygame.mixer.unpause()

                    if event.key == pygame.K_p:
                        self.music.stop()

                    if event.key == pygame.K_o:
                        self.music.play()

            # Move the heart
            #if self.heartmovementup:
            #    self.velocityy = -5
            #    self.hearty += self.velocityy
            #if self.heartmovementdown:
            #    self.velocityy = 5 + self.gravity
            #    self.gravity += .3
            #    self.hearty += self.velocityy
            if self.jumping and self.grounded:
                self.velocityy = -10 * self.hello
            if not self.grounded:
                self.velocityy += self.gravity
                self.hearty += self.velocityy
            if self.heartmovementleft:
                self.velocityx = -5
                self.heartx += self.velocityx
            if self.heartmovementright:
                self.velocityx = 5
                self.heartx += self.velocityx

            self.heart_rect.center = (
                self.heartx, self.hearty
            )

            # Keep the heart inside the battlebox
            if self.heart_rect.left < self.battlebox_rect.left + 10:
                self.heart_rect.left = self.battlebox_rect.left + 10

            if self.heart_rect.right > self.battlebox_rect.right - 10:
                self.heart_rect.right = self.battlebox_rect.right - 10

            if self.heart_rect.top < self.battlebox_rect.top + 10:
                self.heart_rect.top = self.battlebox_rect.top + 10
                self.grounded = True
                self.hello = -1
                self.bye = 0

            if self.heart_rect.bottom > self.battlebox_rect.bottom - 10:
                self.heart_rect.bottom = self.battlebox_rect.bottom - 10
                self.velocityy = 0
                self.grounded = True
                self.hello = 1
                self.bye = 0

            self.heartx, self.hearty = self.heart_rect.center
            # Move and bounce each bullet
            for bullet in self.bullets:
                bullet["x"] += bullet["dx"]
                bullet["y"] += bullet["dy"]

                bullet_rect = bullet["image"].get_rect(
                    center=(
                        round(bullet["x"]),
                        round(bullet["y"])
                    )
                )

                bullet["bounced"] = False

                # Bounce off the left wall
                if bullet_rect.left <= self.battlebox_rect.left:
                    bullet_rect.left = self.battlebox_rect.left + 10
                    bullet["x"] = bullet_rect.centerx
                    bullet["dx"] = abs(bullet["dx"]) + 1
                    bullet["bounced"] = True

                # Bounce off the right wall
                if bullet_rect.right >= self.battlebox_rect.right:
                    bullet_rect.right = self.battlebox_rect.right - 10
                    bullet["x"] = bullet_rect.centerx
                    bullet["dx"] = -abs(bullet["dx"] + 1)
                    bullet["bounced"] = True

                # Bounce off the top wall
                if bullet_rect.top <= self.battlebox_rect.top:
                    bullet_rect.top = self.battlebox_rect.top + 10
                    bullet["y"] = bullet_rect.centery
                    bullet["dy"] = abs(bullet["dy"]) + 1
                    bullet["bounced"] = True

                # Bounce off the bottom wall
                if bullet_rect.bottom >= self.battlebox_rect.bottom:
                    bullet_rect.bottom = self.battlebox_rect.bottom - 10
                    bullet["y"] = bullet_rect.centery
                    bullet["dy"] = -abs(bullet["dy"] + 1)
                    bullet["bounced"] = True

                # Rotate the bullet after bouncing
                if bullet["bounced"]:
                    speed = math.hypot(
                        bullet["dx"], bullet["dy"]
                    )
                if bullet["bounced"]:
                    self.sound1.play()

                    angle = -math.degrees(
                        math.atan2(bullet["dy"], bullet["dx"])
                    )
                    angle += random.uniform(-10, 10)

                    bullet["image"] = pygame.transform.rotate(
                        self.original_bullet, angle
                    )

                    #update the mask to match the rotated image
                    bullet["mask"] = pygame.mask.from_surface(
                        bullet["image"]
                    )

                    bullet["dx"] = speed * math.cos(
                        math.radians(-angle)
                    )
                    bullet["dy"] = speed * math.sin(
                        math.radians(-angle)
                    )

                # Limit the bullet speed
                bullet["dx"] = max(-4, min(4, bullet["dx"]))
                bullet["dy"] = max(-4, min(4, bullet["dy"]))

            # Pixel-perfect collision detection
            for bullet in self.bullets:
                bullet_rect = bullet["image"].get_rect(
                    center=(
                        round(bullet["x"]),
                        round(bullet["y"])
                    )
                )

                offset = (
                    bullet_rect.left - self.heart_rect.left,
                    bullet_rect.top - self.heart_rect.top
                )

                # Only collide when visible pixels overlap
                if self.heart_mask.overlap(bullet["mask"], offset):
                    pygame.quit()
                    sys.exit()

            # Draw everything
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.battlebox, self.battlebox_rect)
            self.screen.blit(self.heart, self.heart_rect)

            # Draw all five bullets
            for bullet in self.bullets:
                bullet_rect = bullet["image"].get_rect(
                    center=(
                        round(bullet["x"]),
                        round(bullet["y"])
                    )
                )

                self.screen.blit(bullet["image"], bullet_rect)

            pygame.display.update()
            self.clock.tick(60)


Game().run()

def movementg(self):
    self.jumping = False
    self.grounded = False
    self.heartmovementup = False
    self.heartmovementleft = False
    self.heartmovementright = False
    self.sprinting = 1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.jumping = True
                self.grounded = False
            if event.key == pygame.K_a:
                self.heartmovementleft = True
            if event.key == pygame.K_d:
                self.heartmovementright = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.heartmovementleft = False
                self.standing = True
            if event.key == pygame.K_d:
                self.heartmovementright = False
                self.standing = True
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                self.sprinting = 1

    if self.jumping and self.grounded:
        self.velocityy = -10 * self.hello
    if not self.grounded:
        self.velocityy += self.gravity
        self.hearty += self.velocityy
    if self.heartmovementleft:
        self.velocityx = -5
        self.heartx += self.velocityx
    if self.heartmovementright:
        self.velocityx = 5
        self.heartx += self.velocityx


import sys
import math
import pygame
import random
import time


class Game:
    def __init__(self):
        pygame.init()

        self.heartx = 400
        self.hearty = 700
        self.border_x = 800
        self.border_y = 800

        pygame.display.set_caption("Hello")
        self.screen = pygame.display.set_mode(
            (self.border_x, self.border_y)
        )
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/gerson.gif")
        self.battlebox = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/battlebox.png")

        # Load the heart with transparency
        self.playerimage = 0
        self.playerimagechange = 0
        self.images = [pygame.image.load("GitHub/Mohameds-Code-Library/Photos/Kris1.png").convert_alpha(),
                    pygame.image.load("GitHub/Mohameds-Code-Library/Photos/Kris2.png").convert_alpha(),
                    pygame.image.load("GitHub/Mohameds-Code-Library/Photos/Kris1.png").convert_alpha(),
                    pygame.image.load("GitHub/Mohameds-Code-Library/Photos/Kris3.png").convert_alpha()]
        # Crop away transparent padding around the heart
        visible_rect = self.images[self.playerimage].get_bounding_rect()
        self.heart = self.images[self.playerimage].subsurface(visible_rect).copy()
        # Create the heart's rectangle and pixel mask
        self.heart_rect = self.images[self.playerimage].get_rect(center=(self.heartx, self.hearty))
        self.heart_mask = pygame.mask.from_surface(self.images[self.playerimage])
        # Load the original block image

        self.battlebox_rect = self.battlebox.get_rect( center=(self.border_x // 2, self.border_y // 2))
        # Heart movement controls
        self.heartmovementup = False
        self.heartmovementdown = False
        self.heartmovementleft = False
        self.heartmovementright = False
        self.jumping = False
        self.grounded = False
        self.standing = True
        self.fallingtime = .5
        self.gravity = .1
        self.velocityy = 0
        self.velocityx = 0
        self.floor = 1
        self.floortime = 0
        self.sprinting = 1

        pygame.mixer.music.load("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3")
        self.sound1 = pygame.Sound("GitHub/Mohameds-Code-Library/Audios/bounce.wav")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_w:
                    #    self.heartmovementup = True
                    #if event.key == pygame.K_s:
                    #    self.heartmovementdown = True
                    if event.key == pygame.K_a:
                        self.heartmovementleft = True
                    if event.key == pygame.K_d:
                        self.heartmovementright = True
                    if event.key == pygame.K_w:
                            self.jumping = True
                            self.grounded = False
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.sprinting = 2
                    if event.key == pygame.K_SPACE:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                    # Press S to stop
                    if event.key == pygame.K_o:
                        pygame.mixer.music.stop()
                    if event.key == pygame.K_p:
                        pygame.mixer.music.play()
                if event.type == pygame.KEYUP:
                    #if event.key == pygame.K_w:
                    #    self.heartmovementup = False
                    #if event.key == pygame.K_s:
                    #    self.heartmovementdown = False
                    if event.key == pygame.K_a:
                        self.heartmovementleft = False
                        self.standing = True
                    if event.key == pygame.K_d:
                        self.heartmovementright = False
                        self.standing = True
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.sprinting = 1
            # Move the heart
            #if self.heartmovementup:
            #    self.velocityy = -5
            #    self.hearty += self.velocityy
            #if self.heartmovementdown:
            #    self.velocityy = 5
            #    self.hearty += self.velocityy
            if self.jumping and self.grounded:
                self.velocityy = -15
            if not self.grounded:
                self.gravity = self.gravity * self.fallingtime
                if self.gravity > 1:
                    self.gravity = 1
                self.velocityy += self.gravity
                self.hearty += self.velocityy
                self.fallingtime += .5
            if self.heartmovementleft:
                self.velocityx = -5 * self.sprinting
                self.heartx += self.velocityx
                self.playerimagechange -= 1 * self.sprinting
                self.standing = False
            if self.heartmovementright:
                self.velocityx = 5 * self.sprinting
                self.heartx += self.velocityx
                self.playerimagechange += 1 * self.sprinting
                self.standing = False
            self.heart_rect.center = (self.heartx, self.hearty)

            # Keep the heart inside the battlebox
            if self.heart_rect.left < self.battlebox_rect.left + 10:
                self.heart_rect.left = self.battlebox_rect.left + 11

            if self.heart_rect.right > self.battlebox_rect.right - 10:
                self.heart_rect.right = self.battlebox_rect.right - 11

            if self.heart_rect.top < self.battlebox_rect.top + 10:
                self.heart_rect.top = self.battlebox_rect.top + 11

            if self.heart_rect.bottom > self.battlebox_rect.bottom - 10:
                self.heart_rect.bottom = self.battlebox_rect.bottom - 11
                self.velocityy = 0
                self.grounded = True
                self.fallingtime = 1
            self.heartx, self.hearty = self.heart_rect.center


            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.battlebox, self.battlebox_rect)
            if not self.standing:
                if  15 >= self.playerimagechange >= 1:
                    self.playerimage = 0
                elif  30 >= self.playerimagechange >= 16:
                    self.playerimage = 1
                elif  45 >= self.playerimagechange >= 3:
                    self.playerimage = 2
                elif  60 >= self.playerimagechange >=46:
                    self.playerimage = 3
                if  0 >= self.playerimagechange:
                    self.playerimagechange = 60
                if  61 <= self.playerimagechange:
                    self.playerimagechange = 0
            if self.standing:
                self.playerimage = 0
            self.screen.blit(self.images[round(self.playerimage)], self.heart_rect)


            pygame.display.update()
            self.clock.tick(60)


Game().run()





