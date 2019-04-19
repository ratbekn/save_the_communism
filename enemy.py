from force_field import ForceField
from game_object import GameObject
import pygame
import math


class Enemy(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 25, game)
        self.x = x
        self.y = y

    def update(self):
        self.choose_direction()
        dx = self.move_direction[0] * self.speed
        dy = self.move_direction[1] * self.speed
        self.move(dx, dy)

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color('BLUE'), (self.x, self.y), self.radius)

    def choose_direction(self):
        if math.fabs(self.x - self.game.player.x) > math.fabs(self.y - self.game.player.y):
            if self.x < self.game.player.x:
                self.move_direction = (1, 0)
            else:
                self.move_direction = (-1, 0)
        else:
            if self.y < self.game.player.y:
                self.move_direction = (0, 1)
            else:
                self.move_direction = (0, -1)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, ForceField):
                self.is_alive = False
