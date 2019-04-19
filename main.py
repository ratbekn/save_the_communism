from game import Game
from player import Player

from enemy import Enemy
import random

FIELD_WIDTH = 2048
FIELD_HEIGHT = 2048

def main():
    game = Game('Save The Communism', FIELD_WIDTH, FIELD_HEIGHT, "images/main_background.png", 60)
    player = Player(100, 100, 800, 600)
    player.setup_handlers(game.keydown_handlers, game.keyup_handlers)
    enemies = []

    for i in range(1):
        enemies.append(Enemy(random.randrange(0, 500), random.randrange(0, 500)))

    game.objects.append(player)
    game.objects.extend(enemies)
    game.run()


if __name__ == '__main__':
    main()
