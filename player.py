import pygame
from math import sqrt
from game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 25, game)
        self.x, self.y = x, y
        self.speed = 8
        self.dirs = {
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0),
            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1)
        }
        self.pressed = set()
        self.is_speaking = False

    def setup_handlers(self, keydown_handlers_dict, keyup_handlers_dict):
        for key in self.dirs:
            keydown_handlers_dict[key].append(self.on_pressed)
            keyup_handlers_dict[key].append(self.on_released)

        keydown_handlers_dict[pygame.K_SPACE].append(self.flip_influence)
        keyup_handlers_dict[pygame.K_SPACE].append(self.flip_influence)

    def flip_influence(self, key):
        self.is_speaking = not self.is_speaking

    def draw(self):
        if self.is_speaking:
            pygame.draw.circle(self.game.surface, pygame.Color('white'), (self.x, self.y), 50, 1)
        pygame.draw.circle(self.game.surface, pygame.Color('red'), (self.x, self.y), 25)

    def update(self):
        if self.is_speaking:
            return

        x, y = 0, 0
        self.move_direction = (0, 0)
        for key in self.pressed:
            x += self.dirs[key][0]
            y += self.dirs[key][1]

        self.move_direction = Player._normalize_direction((x, y))
        self.move(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed))

    @staticmethod
    def _normalize_direction(direction):
        if direction == (0, 0):
            return (0, 0)
        c = sqrt(direction[0] ** 2 + direction[1] ** 2)

        return (direction[0] / c, direction[1] / c)

    def on_released(self, key):
        self.pressed.remove(key)

    def on_pressed(self, key):
        self.pressed.add(key)