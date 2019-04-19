import pygame
from game_object import GameObject

class Citizen(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 25, game)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color("grey"), (self.x, self.y), 20)