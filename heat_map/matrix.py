import copy

def Create(dimensions, item):
    for dimension in dimensions:
        item = map(copy.copy, [item] * dimension)
    return item
def Get(matrix, position):
    for index in position:
        matrix = matrix[index]
    return matrix
def Set(matrix, position, value):
    for index in position[:-1]:
        matrix = matrix[index]
    matrix[position[-1]] = value
def flatten(matrix, position = []):
    result = []
    for i in range(0, len(matrix)):
        currentItem = matrix[i]
        currentPosition = position + [i]
        if hasattr(currentItem, "__iter__") and not isinstance(currentItem, basestring):
            result.extend(flatten(currentItem, currentPosition))
        else:
            result.append((currentPosition, currentItem))
    return result
