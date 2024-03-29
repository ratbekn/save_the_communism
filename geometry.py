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


def calculate_distance(first_obj, second_obj):
    return math.sqrt((first_obj[0] - second_obj[0]) ** 2 + (first_obj[1] - second_obj[1]) ** 2)


def get_rotation_from_vector(x, y):
    return math.degrees(math.atan2(-y, x) - math.pi / 2)


def are_close(first, second):
    eps = 0.1

    if first == (0, 0) or second == (0, 0):
        return False

    return (first[0] * second[0] + first[1] * second[1]) / (vector_len(*first) * vector_len(*second)) >= 1 - eps

def vector_len(x, y):
    return math.sqrt(x ** 2 + y ** 2)
