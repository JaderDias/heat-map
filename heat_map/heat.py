import math
import matrix
import point

def paint(target, center, peak):
    for item in matrix.flatten(target):
        distance = point.get_distance(center, item[0])
        intensity = math.pow(2, -distance) # alternative to 1 / math.pow(1 + distance, 2)
        matrix.set(target, item[0], intensity)
