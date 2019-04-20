from force_field import ForceField
from fellow import Fellow
from heroes import Hero
import random
from geometry import *


class Enemy(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 25, game, 'images/enemy.png')
        self.x = x
        self.y = y

    def update(self):
        self.rotation_vector = get_vector(
            (self.x, self.y), (self.game.player.x, self.game.player.y))
        if self.is_player_near():
            self.choose_direction()
            dx = self.move_direction[0] * self.speed
            dy = self.move_direction[1] * self.speed
            dx, dy = self.check_collision_with_other_enemies(dx, dy)
            self.move(dx, dy)
        else:
            self.move(0, 0)

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
            if isinstance(object, ForceField) or isinstance(object, Fellow):
                self.is_alive = False

    def check_collision_with_other_enemies(self, dx, dy):
        for enemy in self.game.enemies:
            if enemy != self:
                if calculate_distance((self.x + dx, self.y + dy), (enemy.x, enemy.y)) < enemy.radius * 2:
                    return 0, 0
        return dx, dy

    def is_player_near(self):
        return calculate_distance((self.x, self.y), (self.game.player.x, self.game.player.y)) <= 500
