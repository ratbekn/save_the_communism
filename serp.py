import  pygame
from bullet import Bullet

class Serp(Bullet):
    def __init__(self, x, y, dir_x, dir_y, game, not_touching):
        super().__init__(x, y, dir_x, dir_y, game, not_touching)
        self.image = pygame.image.load('images/serp.png')
        self.radius = 20
        self.speed = 20
        self.image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
        self.im_width = self.image.get_width() / 2
        self.im_height = self.image.get_height() / 2


    def draw(self):
        self.game.surface.blit(self.image, (self.x - self.im_width, self.y - self.im_height))
