import pygame
import sys
import random
import math
from player import Player
from enemy import Enemy
from collections import defaultdict

MAX_ENEMIES_COUNT = 7
MIN_DISTANCE_BETWEEN_PLAYER_AND_ENEMY = 100


class Game:
    def __init__(self,
                 caption,
                 back_image_filename,
                 frame_rate):
        self.surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.background_image = pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.player = Player(100, 100, self)
        self.enemies = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        self.player.setup_handlers(self.keydown_handlers, self.keyup_handlers)
        self.objects.append(self.player)
        for i in range(MAX_ENEMIES_COUNT):
            self.enemies.append(self.create_enemy())
        self.objects.extend(self.enemies)
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def create_enemy(self):
        x = random.randrange(self.surface.get_height())
        while math.fabs(x - self.player.x) < MIN_DISTANCE_BETWEEN_PLAYER_AND_ENEMY:
            x = random.randrange(self.surface.get_height())

        y = random.randrange(self.surface.get_width())
        while math.fabs(y - self.player.y) < MIN_DISTANCE_BETWEEN_PLAYER_AND_ENEMY:
            y = random.randrange(self.surface.get_width())

        return Enemy(x, y, self)
