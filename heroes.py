import pygame
from game_object import GameObject
import geometry

class Hero(GameObject):
    def __init__(self, x, y, radius, game, image_path):
        super().__init__(x, y, radius, game)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.rotation_vector = (0, 0)

    def draw(self):
        img = pygame.transform.rotate(
            self.image, geometry.get_rotation_from_vector(self.rotation_vector[0], self.rotation_vector[1]))
        self.game.surface.blit(img, (self.x - img.get_width() / 2, self.y - img.get_height() / 2))

    def orientate_to(self, to_x, to_y):
        self.rotation_vector = geometry.get_vector((self.x, self.y), (to_x, to_y))
