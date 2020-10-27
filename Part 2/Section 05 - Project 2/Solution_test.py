import unittest
import math
from Solution import Polygon


class BasicPolygonTests(unittest.TestCase):
    def setUp(self):
        self.n = 4
        self.R = 1
        self._polygon = Polygon(self.n, self.R)

    def test_string_repr(self):
        self.assertEqual(str(self._polygon), f'Polygon(n=4,R=1)')

    def test_vertices_equal_to_n(self):
        self.assertEqual(self._polygon.count_vertices, self.n)

    def test_count_edges_equal_to_n(self):
        self.assertEqual(self._polygon.count_edges, self.n)

    def test_circumradius_equal_to_R(self):
        self.assertEqual(self._polygon.circumradius, self.R)

    def test_interior_angle(self):
        self.assertEqual(self._polygon.interior_angle, 90)

    def test_area(self):
        self.assertAlmostEqual(self._polygon.area, 2.0, 4)

    def test_side_length(self):
        self.assertAlmostEqual(self._polygon.side_length, math.sqrt(2), 4)

    def test_perimeter(self):
        self.assertAlmostEqual(self._polygon.perimeter, 4*math.sqrt(2), 4)

    def test_apothem(self):
        self.assertAlmostEqual(self._polygon.apothem, 0.707, 3)


class PolygonComparisonsTests(unittest.TestCase):
    def setUp(self):
        self.p1 = Polygon(3, 100)
        self.p2 = Polygon(10, 10)
        self.p3 = Polygon(15, 10)
        self.p4 = Polygon(15, 100)
        self.p5 = Polygon(15, 100)

    def test_greater_than(self):
        self.assertTrue(self.p2 > self.p1)
        self.assertTrue(self.p2 < self.p3)
        self.assertTrue(self.p3 != self.p4)
        self.assertTrue(self.p1 != self.p4)
        self.assertTrue(self.p4 == self.p5)

    def test_invalid_polygon_raises_exception(self):

        self.assertRaises(ValueError, Polygon, 2, 3)


if __name__ == '__main__':
    # run all TestsCase's in this module
    unittest.main()
