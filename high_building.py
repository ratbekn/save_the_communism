from Building import Building


class HighBuilding(Building):
    # size = 230
    def __init__(self, x, y, game):
        super().__init__(x, y, game, Building.size, 'images/high_building.png')
        self.radius = 50