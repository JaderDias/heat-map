import unittest
from heat_map import heat

class paint(unittest.TestCase):
    def testDimension1(self):
        target = [0, 0, 0]
        expected = [.5, 1, .5]
        point = [1]
        intensity = 1
        heat.paint(target, point, intensity)
        self.assertEqual(expected, target)
    def testDimension2(self):
        corner = 0.37521422724648174
        target = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[corner, .5, corner], [.5, 1, .5], [corner, .5, corner]]
        point = [1, 1]
        intensity = 1
        heat.paint(target, point, intensity)
        self.assertEqual(expected, target)
