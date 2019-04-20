import math
from collections import defaultdict

class NewPos:
    def __init__(self, x, y, r):
        self.radius = r
        self.y = y
        self.x = x

new_pos = NewPos(0,0,0)

class CollisionsResolver:
    @staticmethod
    def resolve_collisions(game_objects):
        collisions = CollisionsResolver._get_collisions_dict(game_objects)
        for object in collisions.keys():
            object.handle_collisions(collisions[object])

    @staticmethod
    def are_collided(first, second_x, second_y, second_radius):
        new_pos.x = second_x
        new_pos.y = second_y
        new_pos.radius = second_radius
        return CollisionsResolver._are_collided(first, new_pos)

    @staticmethod
    def _are_collided(first, second):
        distance = math.sqrt((first.x - second.x) ** 2 + (first.y - second.y) ** 2)
        return distance <= first.radius + second.radius

    @staticmethod
    def _get_collisions_dict(game_objects):
        collisions = defaultdict(list)

        for i in range(len(game_objects)):
            for j in range(i + 1, len(game_objects)):

                first, second = game_objects[i], game_objects[j]
                if CollisionsResolver._are_collided(first, second):
                    collisions[first].append(second)
                    collisions[second].append(first)
        return collisions