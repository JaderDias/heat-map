import unittest
import math
from heat_map import point

class get_distance(unittest.TestCase):
    def testDimension1(self):
        pointA = [0]
        pointB = [[0], [1], [2], [-1]]
        expected = [0, 1, 2, 1]
        for test in zip(pointB, expected):
            actual = point.get_distance(pointA, test[0])
            self.assertEqual(test[1], actual)
    def testDimension2(self):
        pointA = [1, 1]
        pointB = [[0, 0], [1, 1], [2, 1], [-1, 1]]
        expected = [math.sqrt(2), 0, 1, 2]
        for test in zip(pointB, expected):
            actual = point.get_distance(pointA, test[0])
            self.assertEqual(test[1], actual)
    def testDimension3(self):
        pointA = [1, 1, 1]
        pointB = [[0, 0, 0], [1, 1, 1], [2, 1, 0], [-1, 1, 0]]
        expected = [math.sqrt(3), 0, math.sqrt(2), math.sqrt(5)]
        for test in zip(pointB, expected):
            actual = point.get_distance(pointA, test[0])
            self.assertEqual(test[1], actual)
