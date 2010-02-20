import unittest
from heat_map import matrix

class Create(unittest.TestCase):
    def testDimension1(self):
        input = [[0], [1], [2]]
        expected = [[], [0], [0, 0]]
        for test in zip(input, expected):
            actual = matrix.create(test[0], 0)
            self.assertEqual(test[1], actual)
    def testDimension2(self):
        input = [[0, 0], [0, 1], [1, 2]]
        expected = [[], [[]], [[0], [0]]]
        for test in zip(input, expected):
            actual = matrix.create(test[0], 0)
            self.assertEqual(test[1], actual)

class Get(unittest.TestCase):
    def testDimension1(self):
        target = [0, 1, 3, 4]
        input = [[0], [1], [3]]
        expected = [0, 1, 4]
        for test in zip(input, expected):
            actual = matrix.get(target, test[0])
            self.assertEqual(test[1], actual)
    def testDimension2(self):
        target = [[0, 1], [3, 5], [-1, -2]]
        input = [[0, 0], [2, 1], [1, 1]]
        expected = [0, -2, 5]
        for test in zip(input, expected):
            actual = matrix.get(target, test[0])
            self.assertEqual(test[1], actual)

class Set(unittest.TestCase):
    def testDimension1(self):
        target = [0, 1, 3, 4]
        input = [([0], 1), ([2], 6)]
        expected = [[1, 1, 3, 4], [1, 1, 6, 4]]
        for test in zip(input, expected):
            matrix.set(target, test[0][0], test[0][1])
            self.assertEqual(test[1], target)
    def testDimension2(self):
        target = [[0, 1], [3, 5], [-1, -2]]
        input = [([0, 0], 1), ([2, 1], 2), ([1, 1], 3)]
        expected = [[[1, 1], [3, 5], [-1, -2]],
                    [[1, 1], [3, 5], [-1, 2]],
                    [[1, 1], [3, 3], [-1, 2]]]
        for test in zip(input, expected):
            matrix.set(target, test[0][0], test[0][1])
            self.assertEqual(test[1], target)

class Flatten(unittest.TestCase):
    def testDimension1(self):
        target = [0, 1, 3, 4]
        expected = [0, 1, 3, 4]
        actual = matrix.flatten(target)
        self.assertEqual(expected, actual)
    def testDimension2(self):
        target = [[0, 1], [3, 4]]
        expected = [0, 1, 3, 4]
        actual = matrix.flatten(target)
        self.assertEqual(expected, actual)
    def testDimension2Tuple(self):
        target = [(0, (1, 2)), ((3, 5), 4)]
        expected = [0, 1, 2, 3, 5, 4]
        actual = matrix.flatten(target)
        self.assertEqual(expected, actual)

class ToDictionary(unittest.TestCase):
    def testDimension1(self):
        target = [0, 1, 3, 4]
        expected = {(0,): 0, (1,): 1, (2,): 3, (3,): 4}
        actual = matrix.to_dictionary(target)
        self.assertEqual(expected, actual)
    def testDimension2(self):
        target = [[0, 1], [3, 4]]
        expected = {(0, 0): 0, (0, 1): 1, (1, 0): 3, (1, 1): 4}
        actual = matrix.to_dictionary(target)
        self.assertEqual(expected, actual)

class GetDimensions(unittest.TestCase):
    def testList(self):
        target = [[], [[]], [[], []], [[0], [0]]]
        expected = [[0], [1, 0], [2, 0], [2, 1]]
        for test in zip(target, expected):
            actual = matrix.get_dimensions(test[0])
            self.assertEqual(test[1], actual)
    def testTuple(self):
        target = [tuple([]), ([],), ([], []), ([0], [0])]
        expected = [[0], [1, 0], [2, 0], [2, 1]]
        for test in zip(target, expected):
            actual = matrix.get_dimensions(test[0])
            self.assertEqual(test[1], actual)

class ToPNGCanvas(unittest.TestCase):
    def test(self):
        target = [[0, 127], [127, 255]]
        expected = [[[0] * 4, [127] * 4], [[127] * 4, [255] * 4]]
        actual = matrix.to_PNGCanvas(target)
        matrix.assertFlattenAlmostEqual(self, expected, actual.canvas)

class Normalize(unittest.TestCase):
    def test(self):
        target = [[0, 1, 2], [3, 6, 7]]
        max_value = 6
        expected = [[0, 43, 85], [128, 255, 255]]
        actual = matrix.normalize(target, max_value)
        matrix.assertFlattenAlmostEqual(self, expected, actual)
