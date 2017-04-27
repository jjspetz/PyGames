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

    # main game loop starts
    while True:
        screen.blit(background, (0, 0))
        hero.move(herox, heroy)
        monster.move(monx, mony)

        # script for handling hero movement via user keyboard commands
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

            elif event.type == pygame.KEYDOWN

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
