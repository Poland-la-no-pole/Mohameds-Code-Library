import pygame

import sys

from Scripts.util import load_image, load_images
from Scripts.tilemap import Tilemap
from Scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("ninja game")

        self.screen = pygame.display.set_mode((640, 640))

        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.assets = {
            "player": load_image("images/entities/player.png"),
            "grass": load_images("images/tiles/grass"),
            "stone": load_images("images/tiles/stone"),
            "background": load_image("images/background.png"),
            }
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.tilemap = Tilemap(self)

        self.scroll = [0, 0]

        self.movementx = [False, False]
        self.movementy = 0

        self.music = pygame.mixer.music.load("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3")

    def run(self):
        while True:
            self.display.blit(self.assets["background"], (0, 0))

            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2- self.scroll[0])
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1])
            render_scroll = int(self.scroll[0]), int(self.scroll[1])

            self.tilemap.render(self.display, offset=render_scroll)

            self.player.update(self.tilemap, (((self.movementx[0] - self.movementx[1]) * 5), self.movementy))
            self.player.render(self.display, offset=render_scroll)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.player.jumpversion <= 1:
                        if event.key == pygame.K_w:
                            self.player.velocity[1] = -3
                            self.player.jumpversion += 1
                    if event.key == pygame.K_d:
                        self.movementx[0] = True
                    if event.key == pygame.K_a:
                        self.movementx[1] = True
                    if event.key == pygame.K_p:
                        pygame.mixer.music.stop()
                    if event.key == pygame.K_o:
                        pygame.mixer.music.play(-1)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.movementx[0] = False
                    if event.key == pygame.K_a:
                        self.movementx[1] = False
                    if event.key == pygame.K_SPACE:
                        if pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            pygame.display.update()
            self.clock.tick(60)
Game().run()