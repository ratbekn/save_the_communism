from force_field import ForceField
from game_object import GameObject
from fellow import Fellow
from heroes import Hero
import pygame
from geometry import *
from bullet import Bullet
from serp import Serp


class Enemy(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/enemy.png')
        self.x = x
        self.y = y
        self.xp = 3
        self.speed = 11

    def update(self):
        if not self.game.player.is_alive:
            return
        self.orientate_to(self.game.player.x, self.game.player.y)
        self.choose_direction()
        dx = self.move_direction[0] * self.speed
        dy = self.move_direction[1] * self.speed
        dx, dy = self.check_collision_with_other_enemies(dx, dy)
        self.move(int(dx), int(dy))

    def choose_direction(self):
        self.move_direction = normalize_direction(
            get_vector((self.x, self.y), (self.game.player.x, self.game.player.y)))

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Serp):
                self.is_alive = False
            if isinstance(object, Bullet):
                self.xp -= 2
                if self.xp <= 0:
                    self.is_alive = False

    def check_collision_with_other_enemies(self, dx, dy):
        for enemy in self.game.enemies:
            if enemy != self:
                if calculate_distance((self.x + dx, self.y + dy), (enemy.x, enemy.y)) < enemy.radius * 2:
                    return 0, 0
        return dx, dy
