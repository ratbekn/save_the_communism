import pygame
from game_object import GameObject

class Hero(GameObject):
    def __init__(self, x, y, radius, game, image_path):
        super().__init__(x, y, radius, game)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))

    def draw(self):
        self.game.surface.blit(self.image, (self.x - self.radius, self.y - self.radius))