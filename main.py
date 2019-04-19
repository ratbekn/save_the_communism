import random
from game import Game
from enemy import Enemy
from player import Player


def main():
    game = Game('Save The Communism', 800, 600, "images/background.png", 60)
    player = Player(game, 100, 100, 800, 600)
    player.setup_handlers(game.keydown_handlers, game.keyup_handlers)
    enemies = []

    for i in range(1):
        enemies.append(Enemy(random.randrange(0, 500), random.randrange(0, 500)))

    game.objects.append(player)
    game.objects.extend(enemies)
    game.run()


if __name__ == '__main__':
    main()
