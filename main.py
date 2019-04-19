from game import Game
from player import Player


def main():
    game = Game('Save The Communism', 800, 600, "images/background.png", 60)
    player = Player(100, 100)
    game.objects.append(player)
    game.run()



if __name__ == '__main__':
    main()
