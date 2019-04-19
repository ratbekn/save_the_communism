import pygame
from game_object import GameObject

class ForceField(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 100, game)
        self.ttl = 1

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color('white'), (self.x, self.y), self.radius, 1)

    def update(self):
        self.ttl -= 1
        if self.ttl <= 0:
            self.is_alive = False