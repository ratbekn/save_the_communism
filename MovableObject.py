from game_object import GameObject


class MovableObject(GameObject):
    def __init__(self, x, y, r, game):
        super().__init__(x, y, r, game)
        self.speed = 5
        self.move_direction = (0, 0)

    def set_position(self, x, y):
        self.x = max(self.radius, min(x, self.field_width - self.radius))
        self.y = max(self.radius, min(y, self.field_height - self.radius))

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.game.collide_with_building(new_x, new_y, self.radius):
            return

        self.set_position(new_x, new_y)