import sys

import pygame

from UI.button import Button
from UI.window import Window


class MainMenu(Window):
    def __init__(self, event_handler):
        super().__init__("Main Menu", 60, self.get_all_objects, 400, 430, event_handler, pygame.Color('black'))
        self.start_button = Button(460, 280, 445, 130, pygame.Color('blue'), "", event_handler)
        self.quit_button = Button(1150, 720, 300, 50, pygame.Color('yellow'), "Quit", event_handler, font_color=pygame.Color('yellow'))
        # self._setup_window()

    def get_all_objects(self):
        yield self.quit_button
        yield self.start_button

    def setup(self):
        self._setup_window()