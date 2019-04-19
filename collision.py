import math
from collections import defaultdict


class CollisionsResolver:
    @staticmethod
    def resolve_collisions(game_objects):
        collisions = CollisionsResolver._get_collisions_dict(game_objects)
        for object in collisions.keys():
            object.handle_collisions(collisions[object])

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