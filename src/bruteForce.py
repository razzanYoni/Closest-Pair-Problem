from statistic import *

def getClosestPairByBruteForce(arrOfPoint:list, n:int, dimension:int = 3) -> tuple :

    minDistance = getDistanceBetweenPoints(arrOfPoint[0], arrOfPoint[1], dimension)
    pointA = arrOfPoint[0]
    pointB = arrOfPoint[1]

    for i in range(n):
        for j in range(i + 1, n):
            distance = getDistanceBetweenPoints(arrOfPoint[i], arrOfPoint[j], dimension)
            if distance < minDistance:
                minDistance = distance
                pointA = arrOfPoint[i]
                pointB = arrOfPoint[j]
    
    return (pointA, pointB, minDistance)