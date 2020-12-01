from chase.animal import Animal
from random import uniform
from math import floor
from chase.point import Point
import logging

class Sheep(Animal):
    def __init__(self, init_pos_limit: float, sheep_move_dist: float):
        logging.debug('object initialization')
        super().__init__(Point(uniform(-init_pos_limit, init_pos_limit),
                               uniform(-init_pos_limit, init_pos_limit)),
                         sheep_move_dist)

    def move(self):
        logging.debug('move() method called')

        world_side = floor(uniform(0, 4))

        if world_side == 0:
            self.position.y += self.distance
            return "North"
        if world_side == 1:
            self.position.y -= self.distance
            return "South"
        if world_side == 2:
            self.position.x += self.distance
            return "East"
        self.position.x -= self.distance
        return "West"
