from game_object import GameObject
from enemy import Enemy
import pygame
from geometry import *
import geometry


class Fellow(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 20, game)

    def update(self):
        if len(self.game.enemies) == 0:
            return

        nearest = self._get_nearest_enemy()
        self.move_direction = geometry.get_vector(
            (self.x, self.y), (nearest.x, nearest.y))
        self.move(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed))

    def _get_nearest_enemy(self):
        min_dist = self._get_distance_to(self.game.enemies[0])
        nearest = self.game.enemies[0]
        for enemy in self.game.enemies:
            d = self._get_distance_to(enemy)
            if d < min_dist:
                min_dist = d
                nearest = enemy

        return nearest

    def _get_distance_to(self, object):
        return math.sqrt((self.x - object.x) ** 2 + (self.y - object.y))

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color("white"), (self.x, self.y), self.radius)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Enemy):
                self.is_alive = False