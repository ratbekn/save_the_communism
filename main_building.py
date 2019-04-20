from Building import Building


class MainBuilding(Building):
    size = 230
    def __init__(self, x, y, game):
        super().__init__(x, y, game, MainBuilding.size, 'images/main_building.png')
        # self.radius = 240