#!/usr/bin/env python3

'''
This is my first attempt at using py-game.
The object of the game it to catch the monster while avoiding his goblin minions
'''

import pygame, sys, random, math
from pygame.locals import *
from characters import *

# global variables
WIDTH = 512
HEIGHT = 480

# set up the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch the Monster')
clock = pygame.time.Clock()

# checks if the hero has caught the monster
def crash_check(mon_pos, hero_pos):
    dist_apart = math.sqrt((mon_pos[0] - hero_pos[0])**2) \
     + math.sqrt((mon_pos[1] - hero_pos[1])**2)
    if dist_apart < 32:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds/win.wav')
        pygame.mixer.music.play()
        return True
    else:
        return False

def goblin_check(goblins, hero_pos):
    for goblin in goblins:
        dist_apart = math.sqrt((goblin.pos[0] - hero_pos[0])**2) \
        + math.sqrt((goblin.pos[1] - hero_pos[1])**2)
        if dist_apart < 32:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds/lose.wav')
            pygame.mixer.music.play()
            return True
    else:
        return False

def menu_screen(LEVEL):
    while True:
        screen.fill((97, 159, 182))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_RETURN:
                    main(LEVEL)

        text = "L" + str(LEVEL) + ": Hit ENTER to play."

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(text, False, (0, 0, 0))
        screen.blit(textsurface,(150,220))

        pygame.display.update()
        clock.tick(60)

def lose_screen(LEVEL):
    while True:
        screen.fill((219, 28, 44))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RETURN or event.key == K_ESCAPE or event.key == K_x:
                    sys.exit()

        text = "You Lost on"
        text2 = "Level " + str(LEVEL - 1)

        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(text, False, (0, 0, 0))
        screen.blit(textsurface,(195,195))

        textsurface2 = myfont.render(text2, False, (0, 0, 0))
        screen.blit(textsurface2,(220,230))

        pygame.display.update()
        clock.tick(60)

def main(LEVEL):
    # create sprites and background
    hero = Hero('images/hero.png')
    monster = Sprite('images/monster.png')
    background = pygame.image.load('images/background.png')
    LEVEL += 1

    # prints current level to screen
    text = "Level: " + str(LEVEL - 1)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 25)


    # builds goblin list
    goblins = []
    for i in range(int(LEVEL/2) + 1):
        goblins.append(Goblin('images/goblin.png', LEVEL))


    # load and start music
    pygame.mixer.music.load('sounds/music.wav')
    pygame.mixer.music.play(-1)

    # initilize variables
    herox = hero.pos[0]
    heroy = hero.pos[1]
    changex = 0
    changey = 0
    count = -1

    # main game loop starts
    while True:
        # counts the iterations in the loop and switches movement for monster's
        # random love directions
        count += 1

        # script for handling hero movement via user keyboard commands
        # This is left in the main loop for major UX improvement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_w:
                    changey = -2
                elif event.key == K_s:
                    changey = 2
                elif event.key == K_a:
                    changex = -2
                elif event.key == K_d:
                    changex = 2
            elif event.type == pygame.KEYUP:
                if event.key == K_d or event.key == K_a:
                    changex = 0
                elif event.key == K_w or event.key == K_s:
                    changey = 0

        herox += changex
        heroy += changey

        if herox < 30:
            herox = 30
        if herox > WIDTH - 60:
            herox = WIDTH - 60
        if heroy < 30:
            heroy = 30
        if heroy > HEIGHT -60:
            heroy = HEIGHT - 60

        # updates icons etc. to the screen
        screen.blit(background, (0, 0))
        hero.move(herox, heroy, screen)
        monster.move(count, screen, WIDTH, HEIGHT)
        # updates level text
        textsurface = myfont.render(text, False, (255, 255, 255))
        screen.blit(textsurface,(30,30))
        # updates goblins on screen
        for goblin in goblins:
            goblin.move(count, screen, WIDTH, HEIGHT)

        if crash_check(monster.pos, hero.pos):
            menu_screen(LEVEL)
        if goblin_check(goblins, hero.pos):
            lose_screen(LEVEL)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    menu_screen(1)
