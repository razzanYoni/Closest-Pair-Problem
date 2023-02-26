from tools import getDistanceBetweenPoints

def getClosestPairByBruteForce(arrOfPoint:list, n:int, dimension:int = 3) -> tuple :

    minDistance = 9999999999999999999999999999999999999999999999

    for i in range(n):
        for j in range(i + 1, n):
            distance = getDistanceBetweenPoints(arrOfPoint[i], arrOfPoint[j], dimension)
            if distance < minDistance:
                minDistance = distance
                pointA = arrOfPoint[i]
                pointB = arrOfPoint[j]
    
    return (pointA, pointB, minDistance)