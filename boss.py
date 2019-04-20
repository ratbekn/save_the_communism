from force_field import ForceField
from game_object import GameObject
from fellow import Fellow
from heroes import Hero
import pygame

class Boss(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/boss.png')
        self.x = x
        self.y = y
        self.xp = 100
        self.game.boss_sound.play()

    def update(self):
        pass

    def handle_collisions(self, coll_objects):
        pass

    def check_collision_with_other_enemies(self, dx, dy):
        pass
