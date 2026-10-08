import random
import math
import time
import pygame
import sys
screen_width_max = 800
screen_height_max = 800
battlebox_width_max = 400
battlebox_height_max = 400
pygame.init()
screen = pygame.display.set_mode((screen_width_max,screen_height_max))
pygame.display.set_caption("hello")
clock = pygame.time.Clock()

test_font = pygame.font.Font("GitHub/Mohameds-Code-Library/Fonts/deltarune.ttf", 50)

#.convert_alpha()

background = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/gerson.gif")
battlebox = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/battlebox.png")
battlebox_rect = battlebox.get_rect(center=(screen_width_max // 2, screen_height_max // 2))
text_surface = test_font.render("my game fo sho", False, "Red")

heart = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/heart.gif")
heart_rect = heart.get_rect(midbottom = (50, 400))

bullet = pygame.image.load("GitHub/Mohameds-Code-Library/Photos/mbullet.gif")
bullet_rect = bullet.get_rect(midbottom = (400, 400))
bullet = pygame.transform.rotate(bullet, 180)


sound1 = pygame.mixer.music
sound1.load("GitHub/Mohameds-Code-Library/Audios/FLOWERMAN.mp3")
sound2 = pygame.mixer.Sound("GitHub/Mohameds-Code-Library/Audios/sanfrancisco.wav")
sound3 = pygame.mixer.Sound("GitHub/Mohameds-Code-Library/Audios/jarona.wav")
sound4 = pygame.mixer.Sound("GitHub/Mohameds-Code-Library/Audios/chaos.wav")
sound5 = pygame.mixer.Sound("GitHub/Mohameds-Code-Library/Audios/metamorphosis.wav")
sound6 = pygame.mixer.Sound("GitHub/Mohameds-Code-Library/Audios/anything.wav")
x = 100
y = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if sound1.get_busy():
                    sound1.pause()
                else:
                    sound1.unpause()
            if event.key == pygame.K_w:
                sound1.play()
            if event.key == pygame.K_s:
                sound1.stop()
            if event.key == pygame.K_p:
                sound2.play()
            if event.key == pygame.K_o:
                sound2.stop()
    screen.blit(background, (0, 0))
    screen.blit(battlebox, battlebox_rect)
    screen.blit(text_surface, (100, 100))


    screen.blit(bullet, bullet_rect)
    screen.blit(heart, heart_rect)

    



    pygame.display.update()
    clock.tick(60)