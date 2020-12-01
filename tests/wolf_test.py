import unittest

from chase.wolf import Wolf
from chase.sheep import Sheep
from chase.point import Point

from math import sqrt


class WolfTestCase(unittest.TestCase):
    def test_init(self):
        w = Wolf(1)
        self.assertEqual(w.distance, 1)
        self.assertTrue(w.position.x == 0 and w.position.y == 0)

    def test_looking_back(self):
        sheep = [Sheep(10, 1) for x in range(5)]

        for index, _ in enumerate(sheep):
            _.position.set(Point(index + 1, index + 1))

        wolf = Wolf(3)

        self.assertEqual(wolf.look_back(sheep), [sheep[0], True, sqrt(2)])

        wolf.position.set(Point(0, 1))

        self.assertEqual(wolf.look_back(sheep), [sheep[0], True, 1])

        wolf.position.set(Point(2, 1))

        self.assertEqual(wolf.look_back(sheep), [sheep[0], True, 1])

        wolf.position.set(Point(1, -3))

        self.assertEqual(wolf.look_back(sheep), [sheep[0], False, 4.0])

        wolf.position.set(Point(10, 5))

        self.assertEqual(wolf.look_back(sheep), [sheep[-1], False, 5.0])
        pass

    def test_moving(self):
        sheep = [Sheep(10, 1) for x in range(2)]

        for index, _ in enumerate(sheep):
            _.position.set(Point(index + 1, index + 1))

        wolf = Wolf(3)

        self.assertEqual(wolf.move(sheep), [True, sheep[0]])

        wolf = Wolf(1)

        self.assertEqual(wolf.move(sheep), [False, sheep[0]])

        wolf.position.set(Point(5, 2))

        self.assertEqual(wolf.move(sheep), [False, sheep[1]])
        self.assertEqual([wolf.position.x, wolf.position.y], [4, 2])

        pass


if __name__ == '__main__':
    unittest.main()
