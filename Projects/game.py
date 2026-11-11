import pygame
import sys

from Scripts.entities import PhysicsEntity
from Scripts.util import load_image

class Game:
    def __init__(self):
        pygame.init() #initialize all imported pygame modules. is needed to actually use any of pygames stuff


        pygame.display.set_caption("ninja game for cool guys and girls and others who arent included") # name of the window
        self.screen = pygame.display.set_mode((800, 800))#sets up the window / scren to display our game

        self.clock = pygame.time.Clock() # creates the object to track time

        self.movementy = [False, False]
        self.movementx = [False, False]

        self.player = PhysicsEntity(self, "player", (50, 50,), (8, 15))

        self.assets = {"player": load_image("random/heart.png")} #"data/images/entities/player.png"


    def run(self):
        while True:
            self.screen.fill((0, 0, 0))#sets the background to the color in there. rgb

            self.player.update(((self.movementx[1] - self.movementx[0]) * 5, (self.movementy[1] - self.movementy[0]) * 5))
            self.player.render(self.screen)

            for event in pygame.event.get():#how pygame registers events and such
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:# checks if the event type is pressing a key down
                    if event.key == pygame.K_w:
                        self.movementy[0] = True
                    if event.key == pygame.K_s:
                        self.movementy[1] = True
                    if event.key == pygame.K_d:
                        self.movementx[1] = True
                    if event.key == pygame.K_a:
                        self.movementx[0] = True
                if event.type == pygame.KEYUP:# checks if the event type is releasing a key
                    if event.key == pygame.K_w:
                        self.movementy[0] = False
                    if event.key == pygame.K_s:
                        self.movementy[1] = False
                    if event.key == pygame.K_d:
                        self.movementx[1] = False
                    if event.key == pygame.K_a:
                        self.movementx[0] = False


            pygame.display.update()
            self.clock.tick(60)

Game().run()