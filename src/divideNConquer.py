from bruteForce import getClosestPairByBruteForce
from statistic import getDistanceBetweenPoints

# TODO: implement sorted array
# TODO: implement getClosestPairByDivideNConquer in the right way

def sortArray(arrOfPoint:list, key:int) -> list:
    return sorted(arrOfPoint, key = lambda x: x[key])

def getClosestPairByDivideNConquer(arrOfPoint:list, n:int, dimension:int = 3) -> tuple :
    if n <= 3: # if there are 3 or less points, use brute force
        return getClosestPairByBruteForce(arrOfPoint, n, dimension)
    else :
        # sort array of points by x coordinate
        arrOfPoint = sortArray(arrOfPoint, 0)

        # divide array of points into 2 sub arrays
        arrOfPoint1 = arrOfPoint[:n // 2]
        arrOfPoint2 = arrOfPoint[n // 2:]

        # find closest pair in each sub array
        pointA, pointB, minDistance = getClosestPairByDivideNConquer(arrOfPoint1, n // 2, dimension)
        pointA, pointB, minDistance = getClosestPairByDivideNConquer(arrOfPoint2, n - (n // 2), dimension)

        # find closest pair that cross the middle line
        # find middle line
        middleLine = (arrOfPoint[n // 2 - 1][0] + arrOfPoint[n // 2][0]) / 2

        nMiddleLine = 0
        # find points that are in the middle line respect to x
        arrOfPointInMiddleLine = []
        for i in range(n):
            if abs(arrOfPoint[i][0] - middleLine) < minDistance:
                arrOfPointInMiddleLine = arrOfPointInMiddleLine + [arrOfPoint[i]]
                nMiddleLine += 1
        
        # sort array of points by y coordinate
        arrOfPointInMiddleLine = sortArray(arrOfPointInMiddleLine, 1)

        # find closest pair that cross the middle line
        for i in range(nMiddleLine):
            # nPointToCheck = (2*(3**dimension)) if (nMiddleLine > (2*(3**dimension))) else nMiddleLine
            nPointToCheck = nMiddleLine

            for j in range(i + 1, nPointToCheck):
                if abs(arrOfPointInMiddleLine[i][1] - arrOfPointInMiddleLine[j][1]) < minDistance :
                    distance = getDistanceBetweenPoints(arrOfPointInMiddleLine[i], arrOfPointInMiddleLine[j], dimension)
                    if distance < minDistance:
                        minDistance = distance
                        pointA = arrOfPointInMiddleLine[i]
                        pointB = arrOfPointInMiddleLine[j]

        return (pointA, pointB, minDistance)