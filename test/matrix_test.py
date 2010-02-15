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

