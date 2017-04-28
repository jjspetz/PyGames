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

        # script for astroid's random vector
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
            x = 20
        elif self.pos[0] < 0:
            x = width- 20
        elif self.pos[1] > height:
            y = 20
        elif self.pos[1] < 0:
            y = height - 20

        self.pos = [x, y]
        self.render(screen)

class Astroid(Sprite):
    def __init__(self, WIDTH, HEIGHT):
        self.img = pygame.image.load(random.choice(['images/astroid1.png',
         'images/astroid2.png', 'images/astroid3.png', 'images/astroid4.png']))
        self.pos = random.choice(
            [[0, random.randint(0,HEIGHT)],
            [WIDTH - 100 , random.randint(0,HEIGHT)],
            [random.randint(0, WIDTH), 0],
            [random.randint(0, WIDTH), HEIGHT - 100]]
            )
        self.colorkey = [0, 0, 0]
        self.alpha = 255
        self.speed = random.randint(1, 10) / 10
        self.switch = random.randint(0,7)
        self.rotation = random.randint(0, 360)
        self.scale = random.randint(50, 125)/100
        self.img = pygame.transform.rotozoom(self.img, self.rotation, self.scale)

    def rotate(self):
        self.img = pygame.transform.rotozoom(self.img, 0, random.random())

class Ship(Sprite):
    def __init__(self, filename):
        self.img = pygame.image.load(filename)
        self.pos = [200, 200]
        self.colorkey = [0, 0, 0]
        self.alpha = 255

    def move(self, x, y, screen):
        self.pos = [x, y]
        self.render(screen)
