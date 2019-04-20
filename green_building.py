import pygame

from Building import Building


class GreenBuilding(Building):
    # size = 230s
    def __init__(self, x, y, game):
        super().__init__(x, y, game, Building.size, 'images/green_building.png')
        self.radius = 170

    def draw(self):
        super().draw()
        # pygame.draw.circle(self.game.surface, pygame.Color('green'), (self.x, self.y), self.radius)