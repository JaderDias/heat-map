import copy

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
