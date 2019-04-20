import pygame
from game_object import GameObject
from force_field import ForceField
from fellow import Fellow
from heroes import Hero


class Citizen(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/citizen.png')

    def update(self):
        pass

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, ForceField):
                self.is_alive = False
                self.game.objects.append(Fellow(self.x, self.y, self.game))
