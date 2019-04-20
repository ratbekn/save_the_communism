import pygame

from game_object import GameObject


class Building(GameObject):
    def __init__(self, x, y, size, game):
        super().__init__(x, y, size, game)

    def draw(self):
        pygame.draw.rect(self.game.surface, pygame.Color('green'), (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2))
        pygame.draw.circle(self.game.surface, pygame.Color('red'),
                         (self.x, self.y),self.radius)

    def update(self):
        pass


