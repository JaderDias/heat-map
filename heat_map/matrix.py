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
