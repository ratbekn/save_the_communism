import pygame
from MovableObject import MovableObject
from game_object import GameObject


class Bullet(MovableObject):
    def __init__(self, x, y, dir_x, dir_y, game, not_touching):
        super().__init__(x, y, 10, game)
        self.speed = 10
        self.move_direction = (dir_x, dir_y)
        self.not_touching = not_touching

    def update(self):
        self.move(int(self.move_direction[0] * self.speed),
                  int(self.move_direction[1] * self.speed))
        if self.collision:
            self.is_alive = False

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color('yellow'), (int(self.x), int(self.y)), 2)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if type(object) not in self.not_touching:
                self.is_alive = False
