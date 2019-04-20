from Building import Building


class UrfuBuilding(Building):
    # size = 230
    def __init__(self, x, y, game):
        super().__init__(x, y, game, Building.size, 'images/urfu.png')
        self.radius = 180