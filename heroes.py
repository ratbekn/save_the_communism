import pygame

from MovableObject import MovableObject
from game_object import GameObject
import geometry


class Hero(MovableObject):
    def __init__(self, x, y, radius, game, image_path):
        super().__init__(x, y, radius, game)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.rotation_vector = (0, 0)
        self.im_width = self.image.get_width() / 2
        self.im_height = self.image.get_height() / 2

    def draw(self):
        img = pygame.transform.rotate(
            self.image, geometry.get_rotation_from_vector(self.rotation_vector[0], self.rotation_vector[1]))
        self.game.surface.blit(img, (self.x - self.im_width, self.y - self.im_height))

    def orientate_to(self, to_x, to_y):
        self.rotation_vector = geometry.get_vector((self.x, self.y), (to_x, to_y))
