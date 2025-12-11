import math
import unittest

import circle
import square


class CircleTests(unittest.TestCase):
    def test_area_unit_circle(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_perimeter_fractional_radius(self):
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(circle.perimeter(2.5), expected)


class SquareTests(unittest.TestCase):
    def test_area_integer_side(self):
        self.assertEqual(square.area(4), 16)

    def test_area_fractional_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_perimeter_integer_side(self):
        self.assertEqual(square.perimeter(3), 12)


if __name__ == "__main__":
    unittest.main()
