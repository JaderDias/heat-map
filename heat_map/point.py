import math

def GetDistance(pointA, pointB):
    sum = 0
    for pair in zip(pointA, pointB):
        sum += math.pow((pair[0] - pair[1]), 2)
    return math.sqrt(sum)
