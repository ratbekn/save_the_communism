import pygame
from MovableObject import MovableObject
from game_object import GameObject


class Bullet(MovableObject):
    def __init__(self, x, y, dir_x, dir_y, game, not_touching, sprite=None):
        super().__init__(x, y, 10, game)
        self.speed = 20
        self.move_direction = (dir_x, dir_y)
        self.not_touching = not_touching
        self.sprite = sprite
        if self.sprite:
            self.image = pygame.image.load(sprite)
            self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
            self.im_width = self.image.get_width() / 2
            self.im_height = self.image.get_height() / 2

    def update(self):
        self.move(int(self.move_direction[0] * self.speed),
                  int(self.move_direction[1] * self.speed))
        if self.collision:
            self.is_alive = False

    def draw(self):
        if self.sprite:
            self.game.surface.blit(self.image, (self.x - self.im_width, self.y - self.im_height))
        else:
            pygame.draw.circle(self.game.surface, pygame.Color('yellow'), (int(self.x), int(self.y)), self.radius)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if type(object) not in self.not_touching:
                self.is_alive = False
