import random
from SerpBonus import SerpBonus
from citizen import Citizen
from enemy import Enemy
from shooting_enemy import ShootingEnemy


class Generator:
    def __init__(self, delay):
        self.delay = delay
        self.generate_after = delay


class SerpGenerator(Generator):
    def __init__(self, delay):
        super().__init__(delay)

    def try_generate(self, game):
        if self.generate_after == 0:
            x = random.randrange(game.width)
            y = random.randrange(game.height)
            self.generate_after = self.delay
            return SerpBonus(x, y, game)

        self.generate_after -= 1


class CitizenGenerator(Generator):
    def __init__(self, delay):
        super().__init__(delay)

    def try_generate(self, game):
        if self.generate_after == 0:
            x = random.randrange(game.width)
            y = random.randrange(game.height)
            self.generate_after = self.delay
            return Citizen(x, y, game)

        self.generate_after -= 1


class EnemiesGenerator(Generator):
    def __init__(self, delay):
        super().__init__(delay)

    def try_generate(self, game):
        if self.generate_after == 0:
            x = random.randrange(game.width)
            y = random.randrange(game.height)
            self.generate_after = self.delay
            r = random.randrange(0, 2)
            if r == 0:
                return Enemy(x, y, game)
            else:
                return ShootingEnemy(x, y, game)

        self.generate_after -= 1