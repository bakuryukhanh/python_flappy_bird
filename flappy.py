# 1.import library
import random
import math
import pygame
from pygame.locals import *

# MAINMENU

# 2.intialize variable
pygame.init()
pygame.mixer.init()
pygame.display.init()
screen = pygame.display.set_mode((800,600))
birdpos = [340,300]
tunel1_H1=100
tunel2_H1 = 300
tunelpos1=[800,0]
tunelpos2=[1200,0]
fly=False


# 3.load image
bird = pygame.image.load("image/bird.png")
bird =pygame.transform.scale(bird,(60,40))
lid = pygame.image.load("image/lid.png")
tunel = pygame.image.load("image/tunel.png")
array = []
space = 150

# 4.load music
hit = pygame.mixer.Sound("audio/explode.wav")
hit2 = pygame.mixer.Sound("audio/shoot.wav")

# 5. Looping
pygame.event.set_blocked(MOUSEMOTION)
running = 1
while running:
    pygame.time.wait(3)

    screen.fill(0)


    screen.blit(bird,birdpos)

    # 6.1 Draw tunel
    tunel = pygame.transform.scale(tunel,(77,tunel1_H1))
    screen.blit(tunel,tunelpos1)
    screen.blit(lid,(tunelpos1[0]-3,tunelpos1[1]+tunel1_H1))
    tunel1_H2 = 600-76-tunel1_H1-space
    tunel = pygame.transform.scale(tunel,(77,tunel1_H2))
    screen.blit(tunel,(tunelpos1[0],600-tunel1_H2))
    screen.blit(lid,(tunelpos1[0]-3,600-tunel1_H2-38))



    tunel = pygame.transform.scale(tunel,(77,tunel2_H1))
    screen.blit(tunel,tunelpos2)
    screen.blit(lid,(tunelpos2[0]-3,tunelpos2[1]+tunel2_H1))
    tunel2_H2 = 600-76-tunel2_H1-space
    tunel = pygame.transform.scale(tunel,(77,tunel2_H2))
    screen.blit(tunel,(tunelpos2[0],600-tunel2_H2))
    screen.blit(lid,(tunelpos2[0]-3,600-tunel2_H2-38))



    # 6.3 Tunel Rectangle
    tunel1_top_rect = pygame.Rect(tunelpos1[0],0,83,tunel1_H1+38)

    tunel1_bot_rect = pygame.Rect(tunelpos1[0],562-tunel1_H2,83,tunel1_H2+38)

    tunel2_top_rect = pygame.Rect(tunelpos2[0],0,83,tunel2_H1+38)

    tunel2_bot_rect = pygame.Rect(tunelpos2[0],562 - tunel2_H2,83,tunel2_H2+38)



    #7.1 Bird fly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                fly = True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                fly = False




    if fly:
        birdpos[1]-=0.7
    else:
        birdpos[1]+=0.7




    #7.3 Bird rectagle
    bird_rect = pygame.Rect(bird.get_rect())
    bird_rect.left = birdpos[0]
    bird_rect.right = birdpos[0]+60
    bird_rect.top = birdpos[1]
    bird_rect.bottom = birdpos[1]+40


    # 8 check collision
    if bird_rect.colliderect(tunel1_top_rect) :
        hit.play()
    if bird_rect.colliderect(tunel1_bot_rect):
        hit.play()


    if bird_rect.colliderect(tunel2_top_rect):
        hit2.play()
    if bird_rect.colliderect(tunel2_bot_rect):
        hit2.play()

    #6.2 recreate Tunel
    if tunelpos1[0] < 30:
        tunelpos1[0] = 800
        tunel1_H1 = random.randint(50,300)

    if tunelpos2[0] < 30:
        tunelpos2[0] = 800
        tunel2_H1 = random.randint(50,300)

    tunelpos1[0]-=0.7
    tunelpos2[0]-=0.7

    pygame.display.flip()