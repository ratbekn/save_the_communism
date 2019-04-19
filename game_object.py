

class GameObject:
    def __init__(self, x, y, r, game):
        self.game = game
        self.field_height = game.surface.get_height()
        self.field_width = game.surface.get_width()
        self.x = x
        self.y = y
        self.radius = r
        self.speed = 1
        self.move_direction = (0, 0)

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

    def set_position(self, x, y):
        self.x = max(self.radius, min(x, self.field_width - self.radius))
        self.y = max(self.radius, min(y, self.field_height - self.radius))

    def move(self, dx, dy):
        self.set_position(self.x + dx, self.y + dy)

    def update(self):
        pass