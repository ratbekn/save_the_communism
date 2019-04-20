import pygame
from game_object import GameObject
from force_field import ForceField
from fellow import Fellow


class Citizen(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 20, game)
        self.image = pygame.image.load('images/citizen.png')
        self.image = pygame.transform.scale(self.image, (self.radius * 3, self.radius * 3))

    def update(self):
        pass

    def draw(self):
        #pygame.draw.circle(self.game.surface, pygame.Color("black"), (self.x, self.y), self.radius)
        self.game.surface.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, ForceField):
                self.is_alive = False
                self.game.objects.append(Fellow(self.x, self.y, self.game))
