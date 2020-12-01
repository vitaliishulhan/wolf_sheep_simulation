import logging


class Point:
    def __init__(self, x: float = 0, y: float = 0):
        logging.debug('object initialization')

        self._x = x
        self._y = y

    @property
    def x(self):
        logging.debug('x getter method called')
        return self._x

    @x.setter
    def x(self, x: float):
        logging.debug('x setter method called')
        if isinstance(x, float):
            self._x = x
        else:
            logging.error('x must be float')
            raise TypeError('x must be float')

    @property
    def y(self) -> float:
        logging.debug('y getter method called')
        return self._y

    @y.setter
    def y(self, y: float):
        logging.debug('y setter method called')
        if isinstance(y, float):
            self._y = y
        else:
            logging.error('y must be float')
            raise TypeError('y must be float')

    def set(self, point):
        logging.debug('set() method called')
        self._x = point.x
        self._y = point.y

    def __str__(self):
        logging.debug('__str__() method called')
        return "(" + "%.3f" % self._x + ", " + "%.3f" % self._y + ")"
