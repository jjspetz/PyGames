#!/usr/bin/env python3

'''
This is my second attempt at using py-game.
The object of the game it to avoid the meteors
'''

import pygame, sys, random, math
from pygame.locals import *
from sprites import *

#SCREEN GLOBAL VARIABLES
WIDTH = 1200
HEIGHT = 840

# set up the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Astroid Mayhem')
clock = pygame.time.Clock()

#
def collision_check(astroids, ship_pos):
    for astroid in astroids:
        dist_apart = math.sqrt((astroid.pos[0] - ship_pos[0])**2) \
        + math.sqrt((astroid.pos[1] - ship_pos[1])**2)
        if dist_apart < 32:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/lose.wav')
            pygame.mixer.music.play()
            return True
    else:
        return False

def menu_screen(count, first=True):
    while True:
        screen.fill((97, 159, 182))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_RETURN:
                    main()

        text = "Hit RETURN to begin"
        text2 = "You survied for " + str(int(count/60)) + " seconds"

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(text, False, (0, 0, 0))
        screen.blit(textsurface,(195,195))

        if not first:
            textsurface2 = myfont.render(text2, False, (0, 0, 0))
            screen.blit(textsurface2,(220,230))

        pygame.display.update()
        clock.tick(60)

def main():
    # create sprites and background
    ship = Ship('images/spaceship.png')
    screen.fill((0,0,0))
    # builds astroid list
    astroids = []
    for i in range(10):
        astroids.append(Astroid(WIDTH, HEIGHT))

    # initilize variables
    shipx = ship.pos[0]
    shipy = ship.pos[1]
    changex = 0
    changey = 0
    count = 0

    # load and start music
    pygame.mixer.music.load('sounds/scifi_music.mp3')
    pygame.mixer.music.play(-1)

    # main game loop starts
    while True:
        if count % 60 == 0:
            astroids.append(Astroid(WIDTH, HEIGHT))

        # counts the iterations in the loop and switches movement for monster's
        # random love directions
        count += 1

        # script for handling ship movement via user keyboard commands
        # This is left in the main loop for major UX improvement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    sys.exit()
                elif event.key == K_w:
                    changey = -4
                elif event.key == K_s:
                    changey = 4
                elif event.key == K_a:
                    changex = -4
                elif event.key == K_d:
                    changex = 4
            elif event.type == pygame.KEYUP:
                if event.key == K_d or event.key == K_a:
                    changex = 0
                elif event.key == K_w or event.key == K_s:
                    changey = 0


        shipx += changex
        shipy += changey

        if shipx < 30:
            shipx = 30
        if shipx > WIDTH - 60:
            shipx = WIDTH - 60
        if shipy < 30:
            shipy = 30
        if shipy > HEIGHT -60:
            shipy = HEIGHT - 60

        # updates icons etc. to the screen
        screen.fill((0,0,0))
        ship.move(shipx, shipy, screen)

        # updates astroids on screen
        for astroid in astroids:
            astroid.move(count, screen, WIDTH, HEIGHT)
        #    astroid.rotate()

        if collision_check(astroids, ship.pos):
            menu_screen(count, False)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
