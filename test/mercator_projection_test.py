import unittest
from heat_map import matrix
from heat_map import mercator_projection

class ToPixel(unittest.TestCase):
    def test(self):
        input = [
                 (0, 0, 0),
                 (0, -90, 0),
                 (0, 90, 1),
                 (-85.0511287798066, 0, 1),
                 (85.0511287798066, 0, 2),
                ]
        expected = [
                    (128, 128),
                    (64, 128),
                    (384, 256),
                    (256, 512),
                    (512, 0),
                   ]
        for test in zip(input, expected):
            actual = mercator_projection.to_pixel(test[0][0], test[0][1], test[0][2])
            matrix.assertFlattenAlmostEqual(self, test[1], actual)

class ToWGS84(unittest.TestCase):
    def test(self):
        input = [
                 (128, 128, 0),
                 (64, 128, 0),
                 (384, 256, 1),
                 (256, 512, 1),
                 (512, 0, 2),
                ]
        expected = [
                    (0, 0),
                    (0, -90),
                    (0, 90),
                    (-85.0511287798066, 0),
                    (85.0511287798066, 0),
                   ]
        for test in zip(input, expected):
            actual = mercator_projection.to_wgs84(test[0][0], test[0][1], test[0][2])
            matrix.assertFlattenAlmostEqual(self, test[1], actual)

class GetExtent(unittest.TestCase):
    def test(self):
        input = [
                 (1, 1, 1),
                 (0, 1, 2),
                ]
        expected = [
                    ((0, 180), (-85.0511287798066, 0)),
                    ((66.513260443111847, -90), (0, -180)),
                   ]
        for test in zip(input, expected):
            actual = mercator_projection.get_extent(test[0][0], test[0][1], test[0][2])
            matrix.assertFlattenAlmostEqual(self, test[1], actual)
