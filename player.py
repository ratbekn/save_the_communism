import pygame
from heroes import Hero
from game_object import GameObject
from force_field import ForceField
from enemy import Enemy
import geometry
from serp import Serp
from bullet import Bullet
from shooting_enemy import ShootingEnemy

class Player(Hero):
    def __init__(self, x, y, game):
        super().__init__(x, y, 45, game, 'images/lenin.png')
        self.x, self.y = x, y
        self.speed = 17
        self.dirs = {
            pygame.K_a: (-1, 0),
            pygame.K_d: (1, 0),
            pygame.K_w: (0, -1),
            pygame.K_s: (0, 1)
        }
        self.pressed = set()
        self.on_pos_changed = None
        self.bullets_cnt = 3
        self.xp = 10

    def setup_handlers(self, keydown_handlers_dict, keyup_handlers_dict, mouse_handlers):
        for key in self.dirs:
            keydown_handlers_dict[key].append(self.on_pressed)
            keyup_handlers_dict[key].append(self.on_released)
        keydown_handlers_dict[pygame.K_SPACE].append(self.hit)
        mouse_handlers.append(self.shoot)

    def hit(self, key):
        self.game.objects.append(ForceField(self.x, self.y, self.game))

    def shoot(self, type, key):
        from fellow import Fellow
        if self.bullets_cnt > 0:
            self.bullets_cnt -= 1
            bullet = Serp(self.x, self.y,
                            self.rotation_vector[0], self.rotation_vector[1],
                            self.game, [Player, Fellow])
            self.game.objects.append(bullet)

    def update(self):
        x, y = 0, 0
        pos = pygame.mouse.get_pos()
        self.orientate_to(pos[0] - self.game.camera_pos[0], pos[1] - self.game.camera_pos[1])
        #self.rotation_vector = geometry.get_vector((self.x, self.y), pygame.mouse.get_pos())
        self.move_direction = (0, 0)
        for key in self.pressed:
            x += self.dirs[key][0]
            y += self.dirs[key][1]

        self.move_direction = geometry.normalize_direction((x, y))
        self.move(int(self.move_direction[0] * self.speed), int(self.move_direction[1] * self.speed))
        if not self.collision:
            self.on_pos_changed(
                int(self.move_direction[0] * self.speed),
                int(self.move_direction[1] * self.speed), self.x, self.y)

    def on_released(self, key):
        if key in self.pressed:
            self.pressed.remove(key)

    def on_pressed(self, key):
        self.pressed.add(key)

    def handle_collisions(self, coll_objects):
        for object in coll_objects:
            if isinstance(object, Enemy) or isinstance(object, ShootingEnemy):
                self.is_alive = False
                pygame.mixer_music.stop()
                rip = pygame.mixer.Sound('rip.wav')
                rip.set_volume(1)
                rip.play()
            if isinstance(object, Bullet) and Player not in object.not_touching:
                self.xp -= 2
                if self.xp <= 0:
                    self.is_alive = False
                    pygame.mixer_music.stop()
                    rip = pygame.mixer.Sound('rip.wav')
                    rip.set_volume(1)
                    rip.play()
