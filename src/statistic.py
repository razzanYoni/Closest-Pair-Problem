from time import time as currentTime
from random import uniform as randomUniform

def getDistanceBetweenPoints(point1:list, point2:list, dimension:int = 3)  -> float:
    distance:float = 0
    for i in range(dimension):
        distance = distance + ((point1[i] - point2[i]) ** 2)
    return distance ** 0.5
