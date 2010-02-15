import math
import operator
import matrix
import point

def wave_dispersion(distance):
    return 1 / math.pow(1 + distance, 2)

def paint(target, center, peak, dispersion = wave_dispersion, overlay = operator.add):
    dictionary = matrix.to_dictionary(target)
    for (key, value) in dictionary.iteritems():
        distance = point.get_distance(center, key)
        intensity = peak * dispersion(distance)
        intensity = overlay(value, intensity)
        matrix.set(target, key, intensity)
