import unittest

from chase.sheep import Sheep
from chase.point import Point


class SheepTestCase(unittest.TestCase):
    def test_sheep_init(self):
        for test in range(0, 100):
            s = Sheep(10, 0.5)
            self.assertTrue(-10 <= s.position.x <= 10)
            self.assertTrue(-10 <= s.position.y <= 10)
        self.assertEqual(Sheep(10, 0.5).distance, 0.5)

    def test_sheep_moving(self):
        s = Sheep(10, 1)
        s.position.set(Point())
        s.move()

        self.assertTrue([s.position.x, s.position.y] == [0, 1] or
                        [s.position.x, s.position.y] == [0, -1] or
                        [s.position.x, s.position.y] == [1, 0] or
                        [s.position.x, s.position.y] == [-1, 0])


if __name__ == '__main__':
    unittest.main()
