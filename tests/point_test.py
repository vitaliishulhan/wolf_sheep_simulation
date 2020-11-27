import unittest
from point import Point


class PointTestCase(unittest.TestCase):
    def test_point_empty_init(self):
        point = Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def test_point_full_init(self):
        point = Point(1, 2)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)

    def test_set_method(self):
        p1 = Point(1,2)
        p2 = Point(3,4)
        p1.set(p2)
        self.assertEqual(p1.x, 3)
        self.assertEqual(p1.y, 4)

    def test_str_method(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1.000, 2.000)")


if __name__ == '__main__':
    unittest.main()
