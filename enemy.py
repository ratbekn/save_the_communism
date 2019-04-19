import random

import pygame


class Enemy:
    def __init__(self,  radius):
        self.radius = 10
        self.x = random.randrange(0, 1200)
        self.y = random.randrange(0, 600)

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('BLUE'), (self.x, self.y), self.radius)
