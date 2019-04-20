import pygame

from game_object import GameObject
from force_field import ForceField
from enemy import Enemy
import geometry


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
        self.image = pygame.image.load('images/lenin.png')
        self.image = pygame.transform.scale(self.image, (self.radius * 3, self.radius * 3))
        self.on_pos_changed = None

    def setup_handlers(self, keydown_handlers_dict, keyup_handlers_dict):
        for key in self.dirs:
            keydown_handlers_dict[key].append(self.on_pressed)
            keyup_handlers_dict[key].append(self.on_released)
        keydown_handlers_dict[pygame.K_SPACE].append(self.hit)

    def hit(self, key):
        self.game.objects.append(ForceField(self.x, self.y, self.game))

    def draw(self):
        #pygame.draw.circle(self.game.surface, pygame.Color('red'), (self.x, self.y), 25)
        self.game.surface.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def update(self):
        x, y = 0, 0
        self.move_direction = (0, 0)
        for key in self.pressed:
            x += self.dirs[key][0]
            y += self.dirs[key][1]

        self.move_direction = geometry.normalize_direction((x, y))
        self.move(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed))
        self.on_pos_changed(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed), self.x, self.y)

    def on_released(self, key):
        self.pressed.remove(key)

    def on_pressed(self, key):
        self.pressed.add(key)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Enemy):
                self.is_alive = False
