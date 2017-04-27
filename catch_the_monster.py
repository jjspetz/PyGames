#!/usr/bin/env python3

'''
This is my first attempt at using py-game.
The object of the game it to catch the monster while avoiding his minions
'''

import pygame, sys, random, math
from pygame.locals import *


# global variables
WIDTH = 512
HEIGHT = 480


# set up the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Catch the Monster')
clock = pygame.time.Clock()

class Sprite:
    def __init__(self, filename, x=200, y=200):
        self.img = pygame.image.load(filename)
        self.pos = [x, y]
        self.colorkey = [0, 0, 0]
        self.alpha = 255

    def render(self, screen):
        try:
            self.img.set_colorkey(self.colorkey)
            self.img.set_alpha(self.alpha)
            screen.blit(self.img, self.pos)
        except:
            print('An error has occurred while the game was rendering the image.')
            exit(0)

    def move(self, x, y):
        self.pos = [x, y]
        self.render(screen)

def crash_check(mon_pos, hero_pos):
    dist_apart = math.sqrt((mon_pos[0] - hero_pos[0])**2) + math.sqrt((mon_pos[1] - hero_pos[1])**2)
    if dist_apart < 32:
        return True
    else:
        return False

def main():
    # create sprites and background
    hero = Sprite('images/hero.png')
    monster = Sprite('images/monster.png', 120, 50)
    background = pygame.image.load('images/background.png')

    # initilize variables
    herox = hero.pos[0]
    heroy = hero.pos[1]
    monx = monster.pos[0]
    mony = monster.pos[1]
    changex = 0
    changey = 0
    count = -1

    # main game loop starts
    while not crash_check(monster.pos, hero.pos):
        screen.blit(background, (0, 0))
        hero.move(herox, heroy)
        monster.move(monx, mony)

        # script for monster's random movement
        count += 1
        if count == 0 or count % 90 == 0:
            switch = random.randint(0,7)
        if switch == 0:
            monx += 4
        elif switch == 1:
            monx += 3
            mony += 3
        elif switch == 2:
            monx += -3
            mony += 3
        elif switch == 3:
            monx += -4
        elif switch == 4:
            mony += 4
        elif switch == 5:
            monx += 3
            mony += -3
        elif switch == 6:
            monx += -3
            mony += -3
        elif switch == 7:
            mony += -4

        # resets monster when it moves off the edge of the screen
        if monster.pos[0] > WIDTH:
            monx = 10
        elif monster.pos[0] < 0:
            monx = WIDTH - 10
        elif monster.pos[1] > HEIGHT:
            mony = 10
        elif monster.pos[1] < 0:
            mony = HEIGHT - 10

        herox += changex
        heroy += changey

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

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
