from heroes import Hero
from bullet import Bullet
from enemy import Enemy
from serp import Serp
from fellow import Fellow
from geometry import *

class ShootingEnemy(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/hopnik.png')
        self.x = x
        self.y = y
        self.xp = 10
        self.shot_delay = 40
        self.shoot_after = self.shot_delay
        self.speed = 9

    def update(self):
        if not self.game.player.is_alive:
            return
        self.orientate_to(self.game.player.x, self.game.player.y)
        self.choose_direction()
        dx = self.move_direction[0] * self.speed
        dy = self.move_direction[1] * self.speed
        dx, dy = self.check_collision_with_other_enemies(dx, dy)
        self.move(int(dx), int(dy))

        if self.shoot_after <= 0:
            self.shoot()
            self.shoot_after = self.shot_delay
        else:
            self.shoot_after -= 1

    def shoot(self):
        from player import Player


        bullet = Bullet(
                self.x, self.y,
                self.rotation_vector[0], self.rotation_vector[1], self.game, [Enemy, ShootingEnemy], 'images/bottile.png')
        self.game.objects.append(bullet)

    def choose_direction(self):
        self.move_direction = normalize_direction(
            get_vector((self.x, self.y), (self.game.player.x, self.game.player.y)))

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Serp):
                self.is_alive = False
                self.game.player.score += 2
                self.game.enemy_death2.play()
            if isinstance(object, Bullet) and type(self) not in object.not_touching:
                self.xp -= 2
                if self.xp <= 0:
                    self.is_alive = False
                    self.game.player.score += 2
                    self.game.enemy_death2.play()

    def check_collision_with_other_enemies(self, dx, dy):
        for enemy in self.game.enemies:
            if enemy != self:
                if calculate_distance((self.x + dx, self.y + dy), (enemy.x, enemy.y)) < enemy.radius * 2:
                    return 0, 0
        return dx, dy
