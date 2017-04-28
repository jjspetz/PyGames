#!/usr/bin/env python3

'''
This is my first attempt at using py-game.
The object of the game it to catch the monster while avoiding his minions
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
    dist_apart = math.sqrt((mon_pos[0] - hero_pos[0])**2) + math.sqrt((mon_pos[1] - hero_pos[1])**2)
    if dist_apart < 32:
        return True
    else:
        return False

def main():
    # create sprites and background
    hero = Hero('images/hero.png')
    monster = Monster('images/monster.png', 120, 50)
    background = pygame.image.load('images/background.png')

    # initilize variables
    herox = hero.pos[0]
    heroy = hero.pos[1]
    changex = 0
    changey = 0
    count = -1

    # main game loop starts
    while not crash_check(monster.pos, hero.pos):
        # counts the iterations in the loop and switches movement for monster's
        # random love directions
        count += 1
        if count == 0 or count % 90 == 0:
            switch = random.randint(0,7)

        # script for handling hero movement via user keyboard commands
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

        screen.blit(background, (0, 0))
        hero.move(herox, heroy, screen)
        monster.move(switch, screen, WIDTH, HEIGHT)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
