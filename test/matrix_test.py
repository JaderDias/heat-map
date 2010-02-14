import unittest
from heat_map import matrix

class CreateTests(unittest.TestCase):
    def testDimension1(self):
        input = [[0], [1], [2]]
        expected = [[], [0], [0, 0]]
        for test in zip(input, expected):
            actual = matrix.Create(test[0], 0)
            self.assertEqual(test[1], actual)
    def testDimension2(self):
        input = [[0, 0], [0, 1], [1, 2]]
        expected = [[], [[]], [[0], [0]]]
        for test in zip(input, expected):
            actual = matrix.Create(test[0], 0)
            self.assertEqual(test[1], actual)

class GetTests(unittest.TestCase):
    def testDimension1(self):
        target = [0, 1, 3, 4]
        input = [[0], [1], [3]]
        expected = [0, 1, 4]
        for test in zip(input, expected):
            actual = matrix.Get(target, test[0])
            self.assertEqual(test[1], actual)
    def testDimension2(self):
        target = [[0, 1], [3, 5], [-1, -2]]
        input = [[0, 0], [2, 1], [1, 1]]
        expected = [0, -2, 5]
        for test in zip(input, expected):
            actual = matrix.Get(target, test[0])
            self.assertEqual(test[1], actual)


if __name__ == "__main__":
    unittest.main()
