import pygame

from MovableObject import MovableObject
from game_object import GameObject

class Bullet(MovableObject):
    def __init__(self, x, y, dir_x, dir_y, game, owner):
        super().__init__(x, y, 10, game)
        self.speed = 10
        self.move_direction = (dir_x, dir_y)
        self.owner = owner

    def update(self):
        self.move(int(self.move_direction[0] * self.speed),
                  int(self.move_direction[1] * self.speed))

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color('black'), (self.x, self.y), 2)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if object != self.owner:
                self.is_alive = False
