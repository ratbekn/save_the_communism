import pygame
import sys
import random
import lives
from enemy import Enemy
from Building import Building
from Urfu_building import UrfuBuilding
from green_building import GreenBuilding
from high_building import HighBuilding
from main_building import MainBuilding
from player import Player
from shooting_enemy import ShootingEnemy
from collision import CollisionsResolver
from citizen import Citizen
import pygame.camera
from collections import defaultdict
from geometry import *
from generators import SerpGenerator, CitizenGenerator, EnemiesGenerator
from boss import Boss

MAX_ENEMIES_COUNT = 7
MAX_CITIZENS_COUNT = 3
MIN_DISTANCE_BETWEEN_PLAYER_AND_ENEMY = 100
BACKGROUND_IMAGE_SIZE = 128


class Game:
    def __init__(self,
                 caption,
                 back_image_filename,
                 frame_rate, width, height, main_menu):
        self.game_over_menu = main_menu
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.surface = pygame.Surface((self.width, self.height))
        self.background_image = pygame.image.load(back_image_filename).convert()
        self.background_image = pygame.transform.scale(self.background_image,
                                                       (BACKGROUND_IMAGE_SIZE, BACKGROUND_IMAGE_SIZE))
        self.frame_rate = frame_rate
        self.game_over = False
        self.buildings = []
        self.objects = []
        self.enemies = []
        self.fellows = []
        self.boss = None  # generated near urfu
        self.is_boss_scene = False
        self.started = False
        self.is_quit = False
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.display.set_caption(caption)
        self.import_sounds()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.obj_generators = [SerpGenerator(300), CitizenGenerator(600)]
        self.enemy_generator = EnemiesGenerator(150)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 100)

    def init(self):
        self.camera_pos = 0, 0
        self.game_over = False
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.surface = pygame.Surface((self.width, self.height))
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.clock = pygame.time.Clock()
        self.buildings.clear()
        self.objects.clear()
        self.enemies.clear()
        self.fellows.clear()
        if self.boss is not None:
            self.boss.game = None
        self.boss = None
        with open('Map/map.txt', 'r') as f:
            x = 0
            y = 0
            for line in f.readlines():
                for s in line:
                    if s == '#':
                        self.buildings.append(MainBuilding(x, y, self))
                    if s == '1':
                        self.buildings.append(HighBuilding(x, y, self))
                    if s == '@':
                        self.buildings.append(GreenBuilding(x, y, self))
                    if s == 'U':
                        self.buildings.append(UrfuBuilding(x, y, self))
                        self.boss = Boss(x - 200, y - 200, self)
                    x += Building.size * 2
                x = 0
                y += Building.size
        self.player = Player(150, 150, self)
        self.objects.append(self.player)
        self.objects.extend(self.buildings)
        self.keydown_handlers.clear()
        self.keyup_handlers.clear()
        self.mouse_handlers.clear()
        self.player.setup_handlers(self.keydown_handlers, self.keyup_handlers, self.mouse_handlers)

        for i in range(MAX_ENEMIES_COUNT // 2):
            self.enemies.append(self.create_hero(Enemy))
        for i in range(MAX_ENEMIES_COUNT // 2):
            self.enemies.append(self.create_hero(ShootingEnemy))
        self.objects.append(Citizen(150, 250, self))
        for i in range(MAX_CITIZENS_COUNT):
            self.objects.append(self.create_hero(Citizen))
        self.objects.extend(self.enemies)
        self.player.on_pos_changed = self.change_camera_pos
        self.ui = lives.Lives(10, 10, self)

    def collide_with_building(self, x, y, r):
        for building in self.buildings:
            if CollisionsResolver.are_collided(building, x, y, r):
                return True
        return False

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                self.objects.append(self.boss)
                self.enemies.append(self.boss)

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def change_camera_pos(self, dx, dy, x, y):
        ch_x = self.camera_pos[0] - dx
        ch_y = self.camera_pos[1] - dy
        if x <= self.screen_width // 2 + self.player.speed or x >= self.width - self.screen_width // 2 - self.player.speed:
            ch_x = self.camera_pos[0]
        if y <= self.screen_height // 2 + self.player.speed or y >= self.height - self.screen_height // 2 - self.player.speed:
            ch_y = self.camera_pos[1]
        self.camera_pos = ch_x, ch_y

    def start(self):
        self.started = True
        self.rip_sound.stop()
        pygame.mixer_music.play()

    def quit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.game_over_menu.start_button.add_click_handler(self.start)
        self.game_over_menu.quit_button.add_click_handler(self.quit)
        self.game_over_menu.setup()
        while True:
            self.started = False
            while not self.started:
                self.game_over_menu.run(self.display)

            self.init()
            while not self.game_over:
                for y in range(0, self.height, BACKGROUND_IMAGE_SIZE):
                    for x in range(0, self.width, BACKGROUND_IMAGE_SIZE):
                        self.surface.blit(self.background_image, (x, y))
                self.handle_events()
                self.update()
                self.draw()

                self.display.blit(self.surface, self.camera_pos)
                self.ui.draw()

                CollisionsResolver.resolve_collisions(self.objects)

                self.objects = self.get_alive_objects(self.objects)
                self.enemies = self.get_alive_objects(self.enemies)
                self.fellows = self.get_alive_objects(self.fellows)
                for generator in self.obj_generators:
                    obj = generator.try_generate(self)
                    if obj:
                        self.objects.append(obj)
                enemy = self.enemy_generator.try_generate(self)
                if enemy:
                    self.objects.append(enemy)
                    self.enemies.append(enemy)
                if not self.player.is_alive:
                    self.game_over = True
                pygame.display.update()
                self.clock.tick(self.frame_rate)

            self.objects = self.get_alive_objects(self.objects)
            self.enemies = self.get_alive_objects(self.enemies)
            self.fellows = self.get_alive_objects(self.fellows)
            if not self.is_boss_scene:
                self.apply_generators()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def apply_generators(self):
        for generator in self.obj_generators:
            obj = generator.try_generate(self)
            if obj:
                self.objects.append(obj)
        enemy = self.enemy_generator.try_generate(self)
        if enemy:
            self.objects.append(enemy)
            self.enemies.append(enemy)

    def get_alive_objects(self, objs):
        alive_objs = []
        for obj in objs:
            if obj.is_alive:
                alive_objs.append(obj)
        return alive_objs

    def is_inside_screen(self, object):
        return (0 <= object.x + self.camera_pos[0] and object.x + self.camera_pos[0] <= self.screen_width and
                0 <= object.y + self.camera_pos[1] and object.y + self.camera_pos[1] <= self.screen_height)

    def create_hero(self, cls):
        x, y = 0, 0
        while x < self.screen_width and y < self.screen_height:
            x = random.randrange(self.width)
            y = random.randrange(self.height)

        for o in self.objects:
            if calculate_distance((x, y), (o.x, o.y)) < o.radius * 2:
                return self.create_hero(cls)
        return cls(x, y, self)

    def import_sounds(self):
        pygame.mixer_music.load(r"sounds\Моя оборона 2.mp3")
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(10)
        self.rip_sound = pygame.mixer.Sound(r'sounds\rip.wav')
        self.rip_sound.set_volume(1)
        self.attack_sound = pygame.mixer.Sound(r'sounds\attack.ogg')
        self.attack_sound.set_volume(1)
        self.boss_sound = pygame.mixer.Sound(r'sounds\boss.ogg')