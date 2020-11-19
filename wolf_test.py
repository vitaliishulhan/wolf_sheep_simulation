import unittest

from wolf import Wolf
from sheep import Sheep
from point import Point


class WolfTestCase(unittest.TestCase):
    def test_init(self):
        w = Wolf(1)
        self.assertEqual(w.wolf_move_dist, 1)
        self.assertTrue(w.position.x == 0 and w.position.y == 0)

    def test_look_back_method(self):
        pass

    def test_moving(self):
        pass


if __name__ == '__main__':
    unittest.main()
