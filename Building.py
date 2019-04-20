import pygame

from game_object import GameObject


class Building(GameObject):
    def __init__(self, x, y, game, radius, image_path):
        super().__init__(x, y, radius, game)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.im_width = self.image.get_width() // 2
        self.im_height = self.image.get_height() // 2

    def draw(self):
        self.game.surface.blit(self.image, (self.x - self.im_width, self.y - self.im_height))
        # pygame.draw.circle(self.game.surface, pygame.Color('green'), (self.x, self.y), self.radius)

    def update(self):
        pass


