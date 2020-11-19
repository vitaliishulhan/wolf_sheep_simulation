class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def set(self, point):
        self.x = point.x
        self.y = point.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
