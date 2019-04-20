from UI.event_handler import EventHandler
from UI.main_menu import MainMenu
from game import Game


FIELD_WIDTH = 6000
FIELD_HEIGHT = 1024

def main():
    handler = EventHandler()
    game = Game('Save The Communism', "images/main_background.png", 30, FIELD_WIDTH, FIELD_HEIGHT)
    MainMenu(handler, game).show()


if __name__ == '__main__':
    main()
