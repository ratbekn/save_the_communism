class GameObject:
    def __init__(self, x, y, r, game):
        self.game = game
        self.field_height = game.surface.get_height()
        self.field_width = game.surface.get_width()
        self.x = x
        self.y = y
        self.radius = r
        self.is_alive = True

    @property
    def left(self):
        return self.x - self.radius

    @property
    def right(self):
        return self.x + self.radius

    @property
    def top(self):
        return self.y - self.radius

    @property
    def bottom(self):
        return self.y + self.radius

    def draw(self):
        pass

    def handle_collisions(self, coll_objects):
        pass

    def update(self):
        pass