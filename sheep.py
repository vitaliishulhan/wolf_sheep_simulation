from random import uniform
from math import floor
from point import Point
import logging


class Sheep:
    def __init__(self, init_pos_limit: float, sheep_move_dist: float):
        logging.debug('object initialization')

        self.sheep_move_dist = sheep_move_dist
        self.position = Point(uniform(-init_pos_limit, init_pos_limit),
                              uniform(-init_pos_limit, init_pos_limit))

    def move(self):
        logging.debug('move() method called')

        world_side = floor(uniform(0, 4))

        if world_side == 0:
            self.position.y += self.sheep_move_dist
            return "North"
        if world_side == 1:
            self.position.y -= self.sheep_move_dist
            return "South"
        if world_side == 2:
            self.position.x += self.sheep_move_dist
            return "East"
        self.position.x -= self.sheep_move_dist
        return "West"
