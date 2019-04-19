import random
from game_object import GameObject
import pygame


class Enemy(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 25, game)
        self.x = x
        self.y = y
        self.direction = ()

    def update(self):
        self.x += random.randrange(-5, 5)
        self.y += random.randrange(-5, 5)

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color('BLUE'), (self.x, self.y), self.radius)

    def choose_direction(self):
        pass
