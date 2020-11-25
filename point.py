import logging

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        logging.debug('object initialization')

        self.x = round(x, 3)
        self.y = round(y, 3)

    def set(self, point):
        logging.debug('set() method called')

        self.x = point.x
        self.y = point.y

    def __str__(self):
        logging.debug('__str__() method called')

        return "(" + "%.3f" % self.x + ", " + "%.3f" % self.y + ")"
