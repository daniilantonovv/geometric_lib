import math
import unittest

import circle
import square


class CircleTests(unittest.TestCase):
    def test_area_unit_circle(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_integer_radius_two(self):
        expected = math.pi * 4
        self.assertAlmostEqual(circle.area(2), expected)

    def test_area_small_fraction(self):
        expected = math.pi * 0.25
        self.assertAlmostEqual(circle.area(0.5), expected)

    def test_area_large_radius(self):
        expected = math.pi * 1_000_000
        self.assertAlmostEqual(circle.area(1000), expected)

    def test_area_negative_radius(self):
        expected = math.pi * 9
        self.assertAlmostEqual(circle.area(-3), expected)

    def test_area_tiny_radius(self):
        expected = math.pi * 1e-12
        self.assertAlmostEqual(circle.area(1e-6), expected)

    def test_area_big_integer_radius(self):
        expected = math.pi * 400
        self.assertAlmostEqual(circle.area(20), expected)

    def test_area_pi_radius(self):
        expected = math.pi ** 3
        self.assertAlmostEqual(circle.area(math.pi), expected)

    def test_area_small_decimal_radius(self):
        expected = math.pi * 1e-4
        self.assertAlmostEqual(circle.area(0.01), expected)

    def test_area_seven_radius(self):
        expected = math.pi * 49
        self.assertAlmostEqual(circle.area(7), expected)

    def test_perimeter_fractional_radius(self):
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(circle.perimeter(2.5), expected)

    def test_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_integer_two(self):
        expected = 4 * math.pi
        self.assertAlmostEqual(circle.perimeter(2), expected)

    def test_perimeter_half_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)

    def test_perimeter_large_radius(self):
        expected = 2000 * math.pi
        self.assertAlmostEqual(circle.perimeter(1000), expected)

    def test_perimeter_negative_radius(self):
        expected = -8 * math.pi
        self.assertAlmostEqual(circle.perimeter(-4), expected)

    def test_perimeter_tiny_radius(self):
        expected = 2 * math.pi * 1e-6
        self.assertAlmostEqual(circle.perimeter(1e-6), expected)

    def test_perimeter_big_integer_radius(self):
        expected = 40 * math.pi
        self.assertAlmostEqual(circle.perimeter(20), expected)

    def test_perimeter_pi_radius(self):
        expected = 2 * (math.pi ** 2)
        self.assertAlmostEqual(circle.perimeter(math.pi), expected)

    def test_perimeter_decimal_radius(self):
        expected = 0.02 * math.pi
        self.assertAlmostEqual(circle.perimeter(0.01), expected)

    def test_perimeter_mixed_fraction(self):
        expected = 2 * math.pi * 2.75
        self.assertAlmostEqual(circle.perimeter(2.75), expected)


class SquareTests(unittest.TestCase):
    def test_area_integer_side(self):
        self.assertEqual(square.area(4), 16)

    def test_area_fractional_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_perimeter_integer_side(self):
        self.assertEqual(square.perimeter(3), 12)

    def test_area_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_area_negative_side(self):
        self.assertEqual(square.area(-3), 9)

    def test_area_large_side(self):
        self.assertEqual(square.area(1000), 1_000_000)

    def test_area_small_fraction(self):
        self.assertAlmostEqual(square.area(0.001), 1e-6)

    def test_area_seven_side(self):
        self.assertEqual(square.area(7), 49)

    def test_area_three_quarters_side(self):
        self.assertAlmostEqual(square.area(0.75), 0.5625)

    def test_area_twelve_side(self):
        self.assertEqual(square.area(12), 144)

    def test_area_mixed_fraction_side(self):
        self.assertAlmostEqual(square.area(10.5), 110.25)

    def test_area_huge_float_side(self):
        self.assertAlmostEqual(square.area(100000.0), 1e10)

    def test_area_pi_side(self):
        expected = math.pi ** 2
        self.assertAlmostEqual(square.area(math.pi), expected)

    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_negative_side(self):
        self.assertEqual(square.perimeter(-5), -20)

    def test_perimeter_large_side(self):
        self.assertEqual(square.perimeter(1000), 4000)

    def test_perimeter_small_fraction(self):
        self.assertAlmostEqual(square.perimeter(0.5), 2)

    def test_perimeter_quarter_side(self):
        self.assertAlmostEqual(square.perimeter(0.25), 1)

    def test_perimeter_pi_side(self):
        expected = 4 * math.pi
        self.assertAlmostEqual(square.perimeter(math.pi), expected)

    def test_perimeter_mixed_fraction_side(self):
        self.assertAlmostEqual(square.perimeter(10.5), 42)

    def test_perimeter_tiny_side(self):
        self.assertAlmostEqual(square.perimeter(0.001), 0.004)

    def test_perimeter_huge_side(self):
        self.assertEqual(square.perimeter(100000), 400000)

    def test_perimeter_seven_side(self):
        self.assertEqual(square.perimeter(7), 28)


if __name__ == "__main__":
    unittest.main()
