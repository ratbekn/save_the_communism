from pygame.rect import Rect


class UIObject():
    def __init__(self, x, y, width, height):
        self.bounds = Rect(x, y, width, height)

    @property
    def left(self):
        return self.bounds.left

    @property
    def top(self):
        return self.bounds.top

    @property
    def width(self):
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    @property
    def center(self):
        return self.bounds.center

    @property
    def centerX(self):
        return self.bounds.centerx

    @property
    def centerY(self):
        return self.bounds.centery
