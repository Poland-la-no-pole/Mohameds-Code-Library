import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("hello")
clock = pygame.time.Clock()

sound = pygame.mixer.music
sound.load("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3")
# Start playing


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            # Press S to stop
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()

            if event.key == pygame.K_w:
                pygame.mixer.music.play()

    pygame.display.update()
    clock.tick(60)


