from game_object import GameObject
import pygame
from geometry import *
import geometry


class Fellow(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 20, game)

    def update(self):
        if self.is_enemy_near():
            nearest = self._get_nearest_enemy()
            self.move_direction = geometry.get_vector(
                (self.x, self.y), (nearest.x, nearest.y))
            self.move(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed))
        else:
            self.choose_direction()
            dx = self.move_direction[0] * self.speed
            dy = self.move_direction[1] * self.speed
            dx, dy = self.check_collision_with_other_fellows(dx, dy)
            self.move(dx, dy)

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

    def draw(self):
        pygame.draw.circle(self.game.surface, pygame.Color("white"), (self.x, self.y), self.radius)

    def handle_collisions(self, coll_objects):
        from enemy import Enemy
        for object in coll_objects:
            if isinstance(object, Enemy):
                self.is_alive = False

    def check_collision_with_other_fellows(self, dx, dy):
        for fellow in self.game.fellows:
            if fellow != self:
                if calculate_distance((self.x + dx, self.y + dy), (fellow.x, fellow.y)) < fellow.radius * 2:
                    return 0, 0
        return dx, dy

    def is_enemy_near(self):
        for e in self.game.enemies:
            if calculate_distance((self.x, self.y), (e.x, e.y)) <= 150:
                return True
        return False
