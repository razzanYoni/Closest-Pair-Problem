from bruteForce import getClosestPairByBruteForce
from tools import getDistanceBetweenPoints, validchecker, sortArrayq


#buat perbadingan
def getClosestPairByDivideNConquer(arrOfPoint:list, n:int, dimension:int = 3) -> tuple :
    if n <= 3: # if there are 3 or less points, use brute force
        return getClosestPairByBruteForce(arrOfPoint, n, dimension)
    else :
        # sort array of points by x coordinate
        sortArrayq(arrOfPoint, 0, 0, n-1)

        # divide array of points into 2 sub arrays
        arrOfPoint1 = arrOfPoint[:n // 2]
        arrOfPoint2 = arrOfPoint[n // 2:]

        # find closest pair in each sub array
        pointA1, pointB1, minDistance1 = getClosestPairByDivideNConquer(arrOfPoint1, n // 2, dimension)
        pointA2, pointB2, minDistance2 = getClosestPairByDivideNConquer(arrOfPoint2, n - (n // 2), dimension)

        # find min distance
        pointA, pointB, minDistance = (pointA1, pointB1, minDistance1) if (minDistance1 < minDistance2) else (pointA2, pointB2, minDistance2)

        # find closest pair that cross the middle line
        # find middle line
        middleLine = (arrOfPoint[n // 2 - 1][0] + arrOfPoint[n // 2][0]) / 2

        nMiddleLine1 = 0
        nMiddleLine2 = 0
        # find points that are in the middle line respect to x
        arrOfPointInMiddleLine1 = []
        arrOfPointInMiddleLine2 = []


        # TODO: optimize this loop
        for i in range(n):
            val = arrOfPoint[i][0] - middleLine
            if val < minDistance and val >= 0:
                arrOfPointInMiddleLine1 = arrOfPointInMiddleLine1 + [arrOfPoint[i]]
                nMiddleLine1 += 1
            elif val > (-1)*minDistance and val <= 0:
                arrOfPointInMiddleLine2 = arrOfPointInMiddleLine2 + [arrOfPoint[i]]
                nMiddleLine2 += 1
        

        #''' Alternative 
        # sort array of points by y coordinate
        sortArrayq(arrOfPointInMiddleLine1, 1, 0, nMiddleLine1-1)
        sortArrayq(arrOfPointInMiddleLine2, 1, 0, nMiddleLine2-1)

        # find closest pair that cross the middle line
        j = 0
        k = 0
        for i in range(nMiddleLine1):
            j = k
            while j < nMiddleLine2:
                if arrOfPointInMiddleLine2[j][1] - arrOfPointInMiddleLine1[i][1] > minDistance:
                    break

                if arrOfPointInMiddleLine2[j][1] - arrOfPointInMiddleLine1[i][1] < (-1)*minDistance:
                    k += 1
                    
                elif validchecker(arrOfPointInMiddleLine1[i], arrOfPointInMiddleLine2[j], minDistance, 2):
                    distance = getDistanceBetweenPoints(arrOfPointInMiddleLine1[i], arrOfPointInMiddleLine2[j], dimension)
                    if distance < minDistance:
                        minDistance = distance
                        pointA = arrOfPointInMiddleLine1[i]
                        pointB = arrOfPointInMiddleLine2[j]
                j += 1

        '''
            nPointToCheck = (6) if (nMiddleLine - i - 1 > (6)) else nMiddleLine - i - 1
            # nPointToCheck = nMiddleLine

            for j in range(1, nPointToCheck+1):
                if abs(arrOfPointInMiddleLine[i][1] - arrOfPointInMiddleLine[i+j][1]) < minDistance :
                    distance = getDistanceBetweenPoints(arrOfPointInMiddleLine[i], arrOfPointInMiddleLine[i+j], dimension)
                    if distance < minDistance:
                        minDistance = distance
                        pointA = arrOfPointInMiddleLine[i]
                        pointB = arrOfPointInMiddleLine[i+j]
        #'''


        return (pointA, pointB, minDistance)