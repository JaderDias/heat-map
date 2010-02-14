import unittest
import math
from heat_map import point

class GetDistanceTests(unittest.TestCase):
    def testDimension1(self):
        pointA = [0]
        pointB = [[0], [1], [2], [-1]]
        expected = [0, 1, 2, 1]
        for test in zip(pointB, expected):
            actual = point.GetDistance(pointA, test[0])
            self.assertEqual(test[1], actual)
    def testDimension2(self):
        sqrt2 = math.sqrt(2)
        pointA = [1, 1]
        pointB = [[0, 0], [1, 1], [2, 1], [-1, 1]]
        expected = [sqrt2, 0, 1, 2]
        for test in zip(pointB, expected):
            actual = point.GetDistance(pointA, test[0])
            self.assertEqual(test[1], actual)
