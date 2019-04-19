import pygame
import sys
import pygame.camera

from collections import defaultdict

BACKGROUND_IMAGE_SIZE = 128

class Game:
    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate):
        self.height = height
        self.width = width
        self.background_image = pygame.image.load(back_image_filename)
        self.background_image = pygame.transform.scale(self.background_image, (BACKGROUND_IMAGE_SIZE, BACKGROUND_IMAGE_SIZE))
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        # pygame.camera.init()
        self.surface = pygame.display.set_mode((800, 600))
        # self.clist = pygame.camera.list_cameras()
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
            o.draw(self.surface)

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
        while not self.game_over:
            for y in range(0, self.height, BACKGROUND_IMAGE_SIZE):
                for x in range(0, self.width, BACKGROUND_IMAGE_SIZE):
                    self.surface.blit(self.background_image, (x, y))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
