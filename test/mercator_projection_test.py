import unittest
from heat_map import mercator_projection

class ToPixel(unittest.TestCase):
    def test(self):
        lat = [0, 0, 0]
        lon = [0, -90, 90]
        zoom = [0, 0, 1, 3]
        expected = [(128, 128), (64, 128), (384, 256), (463, 777)]
        for test in zip(lat, lon, zoom, expected):
            actual = mercator_projection.to_pixel(test[0], test[1], test[2])
            self.assertEqual(test[3], actual)
