from game import Game
from player import Player
from enemy import Enemy
import random


def main():
    game = Game('Save The Communism', 800, 600, "images/background.png", 60)
    player = Player(100, 100)
    enemies = []

    for i in range(1):
        enemies.append(Enemy(random.randrange(0, 500), random.randrange(0, 500)))

    game.objects.append(player)
    game.objects.extend(enemies)
    game.run()


if __name__ == '__main__':
    main()
