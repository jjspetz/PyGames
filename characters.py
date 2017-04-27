import pygame

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

class Monster(Sprite):
    def move(self, switch, screen, width, height):
        x = self.pos[0]
        y = self.pos[1]

        # script for monster's random movement
        if switch == 0:
            x += 4
        elif switch == 1:
            x += 3
            y += 3
        elif switch == 2:
            x += -3
            y += 3
        elif switch == 3:
            x += -4
        elif switch == 4:
            y += 4
        elif switch == 5:
            x += 3
            y += -3
        elif switch == 6:
            x += -3
            y += -3
        elif switch == 7:
            y += -4

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

class Hero(Sprite):
    def move(self, x, y, screen):
        self.pos = [x, y]
        self.render(screen)
