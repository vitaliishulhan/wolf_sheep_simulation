from chase.animal import Animal
from random import uniform
from math import floor
from chase.point import Point
import logging
from enum import Enum, auto


class WorldSide(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Sheep(Animal):
    sides = {
        WorldSide.NORTH: [0, 1],
        WorldSide.SOUTH: [0, -1],
        WorldSide.EAST: [1, 0],
        WorldSide.WEST: [-1, 0]
    }

    def __init__(self, init_pos_limit: float = 10, sheep_move_dist: float = 0.5):
        logging.debug(f'object initialization, init_pos_limit: {init_pos_limit} sheep_move_dist: {sheep_move_dist}')

        super().__init__(Point(uniform(-init_pos_limit, init_pos_limit),
                               uniform(-init_pos_limit, init_pos_limit)),
                         sheep_move_dist)

    def update_distance(self):
        side = [WorldSide.NORTH,
                WorldSide.SOUTH,
                WorldSide.WEST,
                WorldSide.EAST][floor(uniform(0, 4))]

        logging.info(f'Side:{side.name}')

        # if NORTH or SOUTH then 0, elif WEST then distance, elif EAST then -distance
        return Point(self.distance * Sheep.sides[side][0],
                     # if WEST or EAST then 0, elif NORTH then distance, elif SOUTH then -distance
                     self.distance * Sheep.sides[side][1])
