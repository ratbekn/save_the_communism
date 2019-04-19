from game import Game


FIELD_WIDTH = 2048
FIELD_HEIGHT = 2048

def main():

    game = Game('Save The Communism', "images/background.png", 60, FIELD_WIDTH, FIELD_HEIGHT)
    game.run()


if __name__ == '__main__':
    main()
