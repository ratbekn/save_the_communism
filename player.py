import pygame

from game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, field_width, field_height):
        super().__init__(x, y, 25, field_width, field_height)
        self.x, self.y = x, y
        self.speed = 2
        self.dirs = {
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0),
            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1),
        }
        self.direction = (0, 0)

    def setup_handlers(self, keydown_handlers_dict, keyup_handlers_dict):
        for key in self.dirs:
            keydown_handlers_dict[key].append(self.on_move)
            keyup_handlers_dict[key].append(self.on_stop)

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('red'), (self.x, self.y), 25)

    def update(self):
        dx = self.direction[0] * self.speed
        dy = self.direction[1] * self.speed
        self.move(dx, dy)

    def on_move(self, key):
        self.direction = self.dirs[key]

    def on_stop(self, key):
        self.direction = (0, 0)
