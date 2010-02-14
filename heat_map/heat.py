import math
import matrix
import point

def Paint(target, center, peak):
    for i in range(0, len(target)):
        for j in range(0, len(target[i])):
            current = [i, j]
            distance = point.GetDistance(center, current)
            intensity = math.pow(2, -distance)
            matrix.Set(target, current, intensity)
