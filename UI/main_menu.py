import sys

import pygame

from UI.button import Button
from UI.window import Window


class MainMenu(Window):
    def __init__(self, event_handler, game):
        super().__init__("Main Menu", 60, self.get_all_objects, 400, 430, event_handler, pygame.Color('black'))
        self.start_button = Button(460, 580, 445, 130, pygame.Color('blue'), "", event_handler)
        self.quit_button = Button(50, 330, 300, 50, pygame.Color('black'), "Quit", event_handler)
        self.quit_button.add_click_handler(self.quit)
        self.start_button.add_click_handler(self.start_game)
        self.game = game

    def start_game(self):
        self.game.init()
        self.game.run()
        self._setup_window()

    def get_all_objects(self):
        # yield self.quit_button
        yield self.start_button

    def quit(self):
        pygame.quit()
        sys.exit()

    def show(self):
        self.run()