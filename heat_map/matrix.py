import copy
import struct
from PIL import Image

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

def to_image(matrix):
    mode = 'P' #8bpp
    size = get_dimensions(matrix)
    flattened = flatten(matrix)
    data = struct.pack('b' * len(flattened), *flattened)
    image = Image.frombuffer(mode, size, data, 'raw', mode, 0, 1)
    return image
