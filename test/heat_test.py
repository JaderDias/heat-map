import math
import unittest
from heat_map import heat

class Paint(unittest.TestCase):
    def testDimension1(self):
        target = [0, 0, 0]
        expected = [.25, 1, .25]
        point = [1]
        intensity = 1
        heat.paint(target, point, intensity)
        self.assertEqual(expected, target)
    def testDimension2(self):
        corner = 0.1715728752538099
        target = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[corner, 0.25, corner],
                    [0.25, 1.0, 0.25],
                    [corner, 0.25, corner]]
        point = [1, 1]
        intensity = 1
        heat.paint(target, point, intensity)
        self.assertEqual(expected, target)
    def testOverlay(self):
        corner = 0.1715728752538099
        target = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [[corner + 0.25, 1.25, corner + 0.25],
                    [corner + 0.25, 1.25, corner + 0.25],
                    [0.26706437806633621, 0.3611111111111111, 0.26706437806633621]]
        point1 = [1, 1]
        point2 = [0, 1]
        intensity = 1
        heat.paint(target, point1, intensity)
        heat.paint(target, point2, intensity)
        self.assertEqual(expected, target)

class WaveDispersion(unittest.TestCase):
    def test(self):
        input = [0, 1, math.sqrt(2), 2]
        expected = [1, 0.25, 0.1715728752538099, 0.1111111111111111]
        for test in zip(input, expected):
            actual = heat.wave_dispersion(test[0])
            self.assertEqual(test[1], actual)
