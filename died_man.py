from heroes import Hero
import pygame


class DiedMan(Hero):
    def __init__(self, x, y, radius, game, img):
        super().__init__(x, y, radius, game, img)
        self.x = x
        self.y = y
        self.timer = pygame.time

    def update(self):
        pass