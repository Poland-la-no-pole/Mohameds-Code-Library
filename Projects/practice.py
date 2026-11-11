import pygame
import sys

class Game:
    def __init__(self):
        pygame.init() #initialize all imported pygame modules. is needed to actually use any of pygames stuff

        pygame.display.set_caption("ninja game for cool guys and girls and others who arent included") # name of the window

        self.screen = pygame.display.set_mode((800, 800))#sets up the window / scren to display our game

        self.clock = pygame.time.Clock() # creates the object to track time

        self.test_surface = pygame.Surface((100, 100))

        self.colors = {1: "red", 2: "blue", 3: "green"}
        self.index = 1
        self.color = self.colors[1]
        self.x = 200
        self.y = 200
        self.xvelocity = 1
        self.test_font = pygame.font.Font("Github/Mohameds-Code-Library/Fonts/deltarune.tff", 10)



    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.x = self.x + self.xvelocity
            self.index += 1
            if self.index <= 10:
                self.color = 1
            if 20 >= self.index > 10:
                self.color = 2
            if 30 >= self.index > 20:
                self.color = 3
            if 31 <= self.index:
                self.index = 0
            if self.x > 500:
                self.xvelocity = -1
            if self.x < 100:
                self.xvelocity = 1
            
            self.screen.blit(self.test_surface, (self.x, self.y))

            self.test_surface.fill(self.colors[self.color])

            for event in pygame.event.get():#how pygame registers events and such
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

Game().run()