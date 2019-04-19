import math

def normalize_direction(direction):
    if direction == (0, 0):
        return (0, 0)
    c = math.sqrt(direction[0] ** 2 + direction[1] ** 2)

    return (direction[0] / c, direction[1] / c)

def get_vector(fr, to):
    dx = to[0] - fr[0]
    dy = to[1] - fr[1]
    return normalize_direction((dx, dy))