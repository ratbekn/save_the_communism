import pygame

from game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 25, 25)

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('red'), (self.left, self.top), 25)

    def update(self):
        pass