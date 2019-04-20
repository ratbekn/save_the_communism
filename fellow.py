from game_object import GameObject
import pygame
from geometry import *
import geometry
from bullet import Bullet
from heroes import Hero


class Fellow(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/citizen.png')
        self.shot_delay = 10
        self.shoot_after = self.shot_delay

    def update(self):
        if len(self.game.enemies) == 0:
            return

        nearest = self._get_nearest_enemy()
        self.orientate_to(nearest.x, nearest.y)
        #self.rotation_vector = get_vector(
        #    (self.x, self.y), (nearest.x, nearest.y))
        self.move_direction = geometry.get_vector(
            (self.x, self.y), (nearest.x, nearest.y))
        self.move(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed))

        if self.shoot_after <= 0:
            self.shoot()
            self.shoot_after = self.shot_delay
        else:
            self.shoot_after -= 1

    def shoot(self):
        self.game.objects.append(
            Bullet(
                self.x, self.y,
                self.rotation_vector[0], self.rotation_vector[1], self.game, self))

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
        return math.sqrt((self.x - object.x) ** 2 + (self.y - object.y) ** 2)


    def handle_collisions(self, coll_objects):
        from enemy import Enemy
        for object in coll_objects:
            if isinstance(object, Enemy):
                self.is_alive = False