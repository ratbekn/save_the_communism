import pygame

from game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, field_width, field_height):
        super().__init__(x, y, 25, 25)
        self.x, self.y = x, y
        self.field_height = field_height
        self.field_width = field_width
        self.dirs = {
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0),
            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1),
        }
        self.direction = (0, 0)
        self.abs_speed = 2

    def setup_handlers(self, keydown_handlers_dict, keyup_handlers_dict):
        for key in self.dirs:
            keydown_handlers_dict[key].append(self.handle_keyboard)
            keyup_handlers_dict[key].append(self.stop_move)

    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('red'), (self.x, self.y), 25)

    def update(self):
        dx = self.direction[0] * self.abs_speed
        dy = self.direction[1] * self.abs_speed
        x = max(0, min(self.x + dx, self.field_width))
        y = max(0, min(self.y + dy, self.field_height))
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def handle_keyboard(self, key):
        self.direction = self.dirs[key]

    def stop_move(self, key):
        self.direction = (0, 0)
