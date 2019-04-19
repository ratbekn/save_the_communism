from game_object import GameObject
import pygame

class Fellow(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 20, game)

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color("white"), (self.x, self.y), self.radius)