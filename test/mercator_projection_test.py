import unittest
from heat_map import mercator_projection

class ToPixel(unittest.TestCase):
    def test(self):
        input = [(0, 0, 0), (0, -90, 0), (0, 90, 1)]
        expected = [(128, 128), (64, 128), (384, 256)]
        for test in zip(input, expected):
            actual = mercator_projection.to_pixel(test[0][0], test[0][1], test[0][2])
            self.assertEqual(test[1], actual)

class ToWGS84(unittest.TestCase):
    def test(self):
        input = [(128, 128, 0), (64, 128, 0), (384, 256, 1)]
        expected = [(0, 0), (0, -90), (0, 90)]
        for test in zip(input, expected):
            actual = mercator_projection.to_wgs84(test[0][0], test[0][1], test[0][2])
            self.assertEqual(test[1], actual)
