from force_field import ForceField
from game_object import GameObject
from fellow import Fellow
from geometry import *
from serp import Serp
from bullet import Bullet
from heroes import Hero
import pygame

class Boss(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 70, game, 'images/boss.png')
        self.x = x
        self.y = y
        self.xp = 170
        self.game.boss_sound.play()
        self.speed = 13

    def update(self):
        if not self.game.player.is_alive:
            return

        self.orientate_to(self.game.player.x, self.game.player.y)
        self.choose_direction()
        dx = self.move_direction[0] * self.speed
        dy = self.move_direction[1] * self.speed
        dx, dy = self.check_collision_with_other_enemies(dx, dy)
        self.move(int(dx), int(dy))

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Serp):
                self.xp -= 20
            if isinstance(object, Bullet):
                self.xp -= 2
                if self.xp <= 0:
                    self.is_alive = False
                    self.game.player.score += 100

    def check_collision_with_other_enemies(self, dx, dy):
        for enemy in self.game.enemies:
            if enemy != self:
                if calculate_distance((self.x + dx, self.y + dy), (enemy.x, enemy.y)) < enemy.radius * 2:
                    return 0, 0
        return dx, dy

    def choose_direction(self):
        self.move_direction = normalize_direction(
            get_vector((self.x, self.y), (self.game.player.x, self.game.player.y)))

    def play(self):
        pass
