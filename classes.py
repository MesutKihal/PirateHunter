import pygame


class Navy(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 113
        self.height = 66
        self.image = pygame.image.load('navy.png')


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, (172,228,244), (self.x, self.y, self.width, self.height), 1)
        
class Cannon(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 34
        self.height = 13
        self.image = pygame.image.load('bullet.png')

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, (172,228,244), (self.x, self.y, self.width, self.height), 1)

class Ship(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 113
        self.height = 66
        self.image = pygame.image.load('pirate_ship.png')

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, (172,228,244), (self.x, self.y, self.width, self.height), 1)

    
