from point import Point
import logging


class Animal:
    def __init__(self, position: Point, distance: float):
        logging.debug("object initialization")

        self._position = position
        self._distance = distance

    @property
    def position(self) -> Point:
        logging.debug('position getter called')
        return self._position
    
    @position.setter
    def position(self, position: Point):
        logging.debug('position setter method called')
        if isinstance(position, Point):
            self._position = position
        else:
            logging.error('position must be Point')
            raise TypeError('position must be Point')

    @property
    def distance(self) -> float:
        logging.debug('distance getter method called')
        return self._distance

    @distance.setter
    def distance(self, distance: float):
        logging.debug('distance setter method called')
        if isinstance(distance, float):
            self._distance = distance
        else:
            logging.error("distance must be float")
            raise TypeError("distance must be float")

    def move(self, args):
        pass
