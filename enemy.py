import random
from game_object import GameObject
import pygame


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('BLUE'), (self.x, self.y), self.radius)
