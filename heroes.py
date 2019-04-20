import pygame
from game_object import GameObject

class Hero(GameObject):
    def __init__(self, x, y, radius, game, image_path):
        super().__init__(x, y, radius, game)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.rotation_vector = (0, 0)

    def draw(self):
        pygame.transform.rotate()
        self.game.surface.blit(self.image, (self.x - self.radius, self.y - self.radius))