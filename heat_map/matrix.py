import copy
from pngcanvas import PNGCanvas

def create(dimensions, item):
    for dimension in dimensions:
        item = map(copy.copy, [item] * dimension)
    return item

def get(matrix, position):
    for index in position:
        matrix = matrix[index]
    return matrix

def set(matrix, position, value):
    for index in position[:-1]:
        matrix = matrix[index]
    matrix[position[-1]] = value

def flatten(matrix):
    result = []
    for currentItem in matrix:
        if hasattr(currentItem, "__iter__") \
           and not isinstance(currentItem, basestring):
            result.extend(flatten(currentItem))
        else:
            result.append(currentItem)
    return result

def to_dictionary(matrix, position = []):
    result = {}
    for i in range(0, len(matrix)):
        currentItem = matrix[i]
        currentPosition = position + [i]
        if hasattr(currentItem, "__iter__") \
           and not isinstance(currentItem, basestring):
            result.update(to_dictionary(currentItem, currentPosition))
        else:
            result[tuple(currentPosition)] = currentItem
    return result

def get_dimensions(matrix):
    result = [len(matrix)]
    if result[0] > 0 and hasattr(matrix[0], '__iter__'):
        for item in matrix:
            result.extend(get_dimensions(item))
            break
    return result

def to_PNGCanvas(matrix):
    size = get_dimensions(matrix)
    image = PNGCanvas(size[0], size[1], bgcolor = [0, 0, 0, 0])
    for key, value in to_dictionary(matrix).iteritems():
        set(image.canvas, key, [value, value, value, value])
    return image

def assertFlattenAlmostEqual(test_case, expected, actual):
    expected = flatten(expected)
    actual = flatten(actual)
    for item in zip(expected, actual):
        test_case.assertAlmostEqual(item[0], item[1])

def normalize(matrix, max_value):
    factor = 255.0 / max_value
    dic = to_dictionary(matrix)
    for key, value in dic.iteritems():
        result = round(factor * value)
        if result > 255:
            result = 255
        set(matrix, key, result)
    return matrix
