'''
To Do:
    add lifes and final death when lifes up

    add leader board
'''


import pygame, random

class Sprite:
    def __init__(self, filename):
        self.img = pygame.image.load(filename)
        self.pos = random.choice([[50,50],[50,420],[420,420],[420,50]])
        self.colorkey = [0, 0, 0]
        self.alpha = 255
        self.speed = 1

    def render(self, screen):
        try:
            self.img.set_colorkey(self.colorkey)
            self.img.set_alpha(self.alpha)
            screen.blit(self.img, self.pos)
        except:
            print('An error has occurred while the game was rendering the image.')
            exit(0)

    def move(self, count, screen, width, height):
        x = self.pos[0]
        y = self.pos[1]

        if count == 0 or count % 90 == 0:
            self.switch = random.randint(0,7)

        # script for monster's random movement
        if self.switch == 0:
            x += 4 * self.speed
        elif self.switch == 1:
            x += 3 * self.speed
            y += 3 * self.speed
        elif self.switch == 2:
            x += -3 * self.speed
            y += 3 * self.speed
        elif self.switch == 3:
            x += -4 * self.speed
        elif self.switch == 4:
            y += 4 * self.speed
        elif self.switch == 5:
            x += 3 * self.speed
            y += -3 * self.speed
        elif self.switch == 6:
            x += -3 * self.speed
            y += -3 * self.speed
        elif self.switch == 7:
            y += -4 * self.speed


        # resets monster when it moves off the edge of the screen
        if self.pos[0] > width:
            x = 10
        elif self.pos[0] < 0:
            x = width- 10
        elif self.pos[1] > height:
            y = 10
        elif self.pos[1] < 0:
            y = height - 10

        self.pos = [x, y]
        self.render(screen)

class Goblin(Sprite):
    def __init__(self, filename, LEVEL):
        self.img = pygame.image.load(filename)
        self.pos = random.choice(
            [[random.randint(20,100), random.randint(20,100)],
            [random.randint(100,150), random.randint(100,150)],
            [random.randint(270,325), random.randint(270,325)],
            [random.randint(325,460), random.randint(325,460)]]
            )
        self.colorkey = [0, 0, 0]
        self.alpha = 255
        if LEVEL < 5:
            self.speed = 0.4
        elif LEVEL <= 8:
            self.speed = 0.5
        else:
            self.speed = random.choice([0.5, 0.7])


class Hero(Sprite):
    def __init__(self, filename):
        self.img = pygame.image.load(filename)
        self.pos = [200, 200]
        self.colorkey = [0, 0, 0]
        self.alpha = 255

    def move(self, x, y, screen):
        self.pos = [x, y]
        self.render(screen)
