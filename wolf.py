from typing import List
from point import Point
from sheep import Sheep
from math import sqrt
from math import pow

import logging


class Wolf:
    def __init__(self, wolf_move_dist: float):
        logging.debug('object initialization')

        self.wolf_move_dist = wolf_move_dist
        self.position = Point()

    def look_back(self, sheep: List[Sheep]) -> [Sheep, bool, float]:
        logging.debug('look_back() method called')

        dist = []

        for _sheep in sheep:
            dist.append(sqrt(pow(self.position.x - _sheep.position.x, 2) + pow(self.position.y - _sheep.position.y, 2)))

        dist_to_victim = min(dist)
        victim = sheep[dist.index(dist_to_victim)]

        return [victim, dist_to_victim <= self.wolf_move_dist, dist_to_victim]

    def move(self, sheep: List[Sheep]) -> [bool, Sheep]:
        logging.debug('move() method called')

        victim, can_be_killed, dist_to_victim = self.look_back(sheep)

        if can_be_killed:
            self.position.set(victim.position)
            return [True, victim]

        relation = self.wolf_move_dist / (dist_to_victim - self.wolf_move_dist)

        go_to = Point((self.position.x + relation * victim.position.x) / (1 + relation),
                      (self.position.y + relation * victim.position.y) / (1 + relation))

        self.position.set(go_to)

        return [False, victim]

    def __str__(self):
        logging.debug('__str__() method called')

        return "wolf position: " + str(self.position)