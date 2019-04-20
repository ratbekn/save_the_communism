import pygame

from UI.event_handler import EventHandler
from UI.game_over_menu import GameOverMenu
from UI.main_menu import MainMenu
from game import Game


FIELD_WIDTH = 7000
FIELD_HEIGHT = 1700

def main():
    pygame.init()
    pygame.font.init()
    handler = EventHandler()
    menu = MainMenu(handler)

    game = Game('Save The Communism', "images/main_background.png", 30, FIELD_WIDTH, FIELD_HEIGHT, menu)
    game.run()
    # gom = GameOverMenu(handler, game)




if __name__ == '__main__':
    main()
