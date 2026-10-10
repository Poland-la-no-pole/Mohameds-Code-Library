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
        # Load the original block image

        self.battlebox_rect = self.battlebox.get_rect( center=(self.border_x // 2, self.border_y // 2))
        # Heart movement controls
        self.heartmovementup = False
        self.heartmovementdown = False
        self.heartmovementleft = False
        self.heartmovementright = False
        self.gravity = .2
        self.velocityy = 0
        self.velocityx = 0
        self.jumping = False
        self.grounded = False
        self.floor = 1
        self.floortime = 0

        pygame.mixer.music.load("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3")
        self.sound1 = pygame.Sound("GitHub/Mohameds-Code-Library/Audios/bounce.wav")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.heartmovementup = True
                    if event.key == pygame.K_s:
                        self.heartmovementdown = True
                    if event.key == pygame.K_a:
                        self.heartmovementleft = True
                    if event.key == pygame.K_d:
                        self.heartmovementright = True
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
                    if event.key == pygame.K_w:
                        self.heartmovementup = False
                    if event.key == pygame.K_s:
                        self.heartmovementdown = False
                    if event.key == pygame.K_a:
                        self.heartmovementleft = False
                    if event.key == pygame.K_d:
                        self.heartmovementright = False
            # Move the heart
            if self.heartmovementup:
                self.velocityy = -5
                self.hearty += self.velocityy
            if self.heartmovementdown:
                self.velocityy = 5
                self.hearty += self.velocityy
            if self.heartmovementleft:
                self.velocityx = -5
                self.heartx += self.velocityx
            if self.heartmovementright:
                self.velocityx = 5
                self.heartx += self.velocityx
            self.heart_rect.center = (self.heartx, self.hearty)

            # Keep the heart inside the battlebox
            if self.heart_rect.left < self.battlebox_rect.left + 10:
                self.heart_rect.left = self.battlebox_rect.left + 10

            if self.heart_rect.right > self.battlebox_rect.right - 10:
                self.heart_rect.right = self.battlebox_rect.right - 10

            if self.heart_rect.top < self.battlebox_rect.top + 10:
                self.heart_rect.top = self.battlebox_rect.top + 10
                self.grounded = True

            if self.heart_rect.bottom > self.battlebox_rect.bottom - 10:
                self.heart_rect.bottom = self.battlebox_rect.bottom - 10
                self.velocityy = 0
                self.grounded = True
            self.heartx, self.hearty = self.heart_rect.center


            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.battlebox, self.battlebox_rect)


            self.screen.blit(self.heart, self.heart_rect)


            pygame.display.update()
            self.clock.tick(60)


Game().run()