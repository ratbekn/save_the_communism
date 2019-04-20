import pygame
import sys


class Window:
    def __init__(self, caption, frame_rate, objects, width, height, event_handler, back_color = (0,0,0)):
        self.caption = caption
        self.frame_rate = frame_rate
        self.objects = objects
        self.width = width
        self.height = height
        self._event_handler = event_handler
        self.back_color = back_color
        self.surface = None
        self.background = None
        self.screen = None
        self.clock = None
        self.is_ended = False

    def update(self):
        for obj in self.objects():
            obj.update()

    def draw(self):
        for obj in self.objects():
            obj.draw(self.surface)

    def run(self):
        self._setup_window()
        while not self.is_ended:
            self.surface.blit(self.background, (0, 0))

            self._event_handler.handle_events()
            if self._event_handler.last_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def __set_background(self, surface):
        background = pygame.image.load('images/mainmenu.png')
        background = background.convert()
        background = pygame.transform.scale(background,
                                                       (1366, 768))
        return background

    def _setup_window(self):
        self.surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.background = self.__set_background(self.surface)
        self.screen = pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()
