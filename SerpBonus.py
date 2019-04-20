import pygame
from game_object import GameObject

class SerpBonus(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 20, game)
        self.image = pygame.image.load('images/serp.png')
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.im_width = self.image.get_width() / 2
        self.im_height = self.image.get_height() / 2


    def update(self):
        pass

    def draw(self):
        self.game.surface.blit(self.image, (self.x - self.im_width, self.y - self.im_height))

    def handle_collisions(self, coll_objects):
        from player import Player
        for object in coll_objects:
            if isinstance(object, Player):
                self.is_alive = False