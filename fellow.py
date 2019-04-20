from game_object import GameObject
import pygame
from geometry import *
from died_man import DiedMan
from bullet import Bullet
from heroes import Hero


class Fellow(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/fellow.png')
        self.shot_delay = 20
        self.shoot_after = self.shot_delay
        self.xp = 10

    def update(self):
        self.follow_player()
        if self.is_enemy_near():
            self.attack_enemies()
        else:
            self.rotation_vector = self.game.player.rotation_vector

    def attack_enemies(self):
        nearest = self._get_nearest_enemy()
        self.orientate_to(nearest.x, nearest.y)
        # self.rotation_vector = get_vector(
        #    (self.x, self.y), (nearest.x, nearest.y))
        if self.shoot_after <= 0:
            self.shoot()
            self.shoot_after = self.shot_delay
        else:
            self.shoot_after -= 1

    def follow_player(self):
        self.choose_direction()
        dx = self.move_direction[0] * self.speed
        dy = self.move_direction[1] * self.speed
        dx, dy = self.check_collision_with_other_fellows(dx, dy)
        self.move(dx, dy)

    def check_collision_with_other_fellows(self, dx, dy):
        if calculate_distance((self.x + dx, self.y + dy), (self.game.player.x, self.game.player.y)) < self.radius * 2:
            return 0, 0
        for fellow in self.game.fellows:
            if fellow != self:
                if calculate_distance((self.x + dx, self.y + dy), (fellow.x, fellow.y)) < fellow.radius * 2:
                    return 0, 0
        return dx, dy

    def choose_direction(self):
        self.move_direction = normalize_direction(
            get_vector((self.x, self.y), (self.game.player.x, self.game.player.y)))

    def shoot(self):
        from player import Player
        self.game.objects.append(
            Bullet(
                self.x, self.y,
                self.rotation_vector[0], self.rotation_vector[1], self.game, [Player, Fellow]))

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
        from shooting_enemy import ShootingEnemy

        for object in coll_objects:
            if isinstance(object, Enemy) or isinstance(object, ShootingEnemy):
                self.die()
            if isinstance(object, Bullet) and Fellow not in object.not_touching:
                self.xp -= 2
                if self.xp <= 0:
                    self.die()

    def is_enemy_near(self):
        for enemy in self.game.enemies:
            if self.game.is_inside_screen(enemy):
                return True
        return False

    def die(self):
        self.is_alive = False
        self.game.enemy_death3.play()
        died = DiedMan(self.x, self.y, self.radius, self.game, r'images\красноармеец сдох.png')
        self.game.objects.append(died)
