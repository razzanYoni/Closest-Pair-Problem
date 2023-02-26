from time import time as currentTime
from random import uniform as randomUniform
import matplotlib.pyplot as plt
from sys import setrecursionlimit

def initializeCounter():
    global euclidN
    euclidN = 0

def getDistanceBetweenPoints(point1:list, point2:list, dimension:int = 3)  -> float:
    global euclidN
    euclidN += 1
    distance:float = 0
    for i in range(dimension):
        distance = distance + ((point1[i] - point2[i]) ** 2)
    return distance ** 0.5

def validchecker(point1: list, point2: list, threshold: float, startcheck: int = 0) -> bool:
    valid = True
    for i in range(startcheck, len(point1)):
        if abs(point1[i] - point2[i]) > threshold:
            valid = False
            break
    return valid

def sortArraym(arrOfPoint:list, key:int, n:int):
    if(n != 1):
        arrOfPoint1 = arrOfPoint[:n//2]
        arrOfPoint2 = arrOfPoint[n//2:]

        len1 = n//2
        len2 = n - n//2

        sortArraym(arrOfPoint1, key, len1)
        sortArraym(arrOfPoint2, key, len2)

        idx = 0
        idx1 = 0
        idx2 = 0
        
        while idx1 < len1 and idx2 < len2:
            if (arrOfPoint1[idx1][key] < arrOfPoint2[idx2][key]):
                arrOfPoint[idx] = arrOfPoint1[idx1]
                idx1 += 1
            else:
                arrOfPoint[idx] = arrOfPoint2[idx2]
                idx2 += 1
            idx += 1
        while idx1 < len1:
            arrOfPoint[idx] = arrOfPoint1[idx1]
            idx1 += 1
            idx += 1
        while idx2 < len2:
            arrOfPoint[idx] = arrOfPoint2[idx2]
            idx2 += 1
            idx += 1

def sortArrayq(arrOfPoint:list, key:int, i:int, j:int):
    if (i < j):
        k = partite2(arrOfPoint, key, i, j)
        sortArrayq(arrOfPoint, key, i, k-1)
        sortArrayq(arrOfPoint, key, k+1, j)

#referensi ppt
def partite(arrOfPoint:list, key:int, i:int, j:int):
    pivot = arrOfPoint[i][key]

    #do while?
    p = i + 1
    q = j

    while arrOfPoint[p][key] < pivot:
        p += 1
        if p > j:
            p -= 1
            break
    while arrOfPoint[q][key] > pivot:
        q -= 1
        if q < i:
            q += 1
            break
    arrOfPoint[p], arrOfPoint[q] = arrOfPoint[q], arrOfPoint[p]

    while p < q:
        while arrOfPoint[p][key] < pivot:
            p += 1
            if p > j:
                p -= 1
                break
        while arrOfPoint[q][key] > pivot:
            q -= 1    
            if q < i:
                q += 1
                break
        arrOfPoint[p], arrOfPoint[q] = arrOfPoint[q], arrOfPoint[p]
    
    arrOfPoint[p], arrOfPoint[q] = arrOfPoint[q], arrOfPoint[p]
    arrOfPoint[i], arrOfPoint[q] = arrOfPoint[q], arrOfPoint[i]
    
    return q

#referensi internet
def partite2(arrOfPoint:list, key:int, i:int, j:int):
    pivot = arrOfPoint[j][key]
    p = i-1

    for l in range(i, j):
        if arrOfPoint[l][key] <= pivot:
            p += 1
            arrOfPoint[p], arrOfPoint[l] = arrOfPoint[l], arrOfPoint[p]
    
    p += 1
    arrOfPoint[p], arrOfPoint[j] = arrOfPoint[j], arrOfPoint[p]
    return p

def three_dimensional_plotting(arrOfPoint:list, pointA:list, pointB:list) :
    fig = plt.figure()

    # 3D plot from array of points
    ax = fig.add_subplot(111, projection='3d')
    for point in arrOfPoint:
        ax.scatter(point[0], point[1], point[2], color='blue')
    
    ax.scatter(pointA[0], pointA[1], pointA[2], color='red')
    ax.scatter(pointB[0], pointB[1], pointB[2], color='red')
    plt.show()

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
        # TODO: optimize this loop
        
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

        return (pointA, pointB, minDistance)

def readFile(fileName:str) -> tuple :
    fileName = '../test/' + fileName

    arrOfPoints = []
    dimension:int
    n:int

    with open(fileName, 'r') as f:
        for line in f:
            temp = line.split(' ')
            point = []
            dimension = len(temp)

            for num in temp:
                if num != '\n':
                    point = point + [float(num)]
            arrOfPoints = arrOfPoints + [point]
    
    f.close()
    
    n = len(arrOfPoints)
    return (arrOfPoints, n, dimension)

if __name__ == '__main__':
    setrecursionlimit(100000)
    exit = False

    while not(exit) :
        inputUser = -1
        print("""
Input action:
1. Random
2. Read File
3. exit""")
        inputUser = int(input("-> "))
        if inputUser == 1 :

            # input n points
            n = int(input("Enter number of points: "))

            # input d dimension
            dimension = int(input("Enter dimension: "))

            # inisialize array of points
            arrOfPoint = []
            
            # generate random points
            for i in range(n):
                temp = [randomUniform(-10000000, 10000000) for j in range(dimension)]
                arrOfPoint = arrOfPoint + [temp]
        elif inputUser == 2 :
            fileName = input("Input File Name: ")
            arrOfPoint, n, dimension = readFile(fileName)
        elif inputUser == 3 :
            exit = True
            quit()
        else :
            pass
        
        if ((inputUser == 1) or (inputUser == 2)) :
            # get closest pair by brute force
            initializeCounter()
            timeBruteForce = currentTime()
            point1BF, point2BF, minDistanceBF = getClosestPairByBruteForce(arrOfPoint, n, dimension)
            timeBruteForce = currentTime() - timeBruteForce

            # get closest pair by divide and conquer
            print("Closest pair is Using Brute Force: ")
            print("Point A: ", point1BF)
            print("Point B: ", point2BF)
            print("Distance: ", minDistanceBF)
            print("Time: ", timeBruteForce)
            print("Times euclidean distance called: ", euclidN)

            initializeCounter()
            timeDivideNConquer = currentTime()
            point1DC, point2DC, minDistanceDC= getClosestPairByDivideNConquer(arrOfPoint, n, dimension)
            timeDivideNConquer = currentTime() - timeDivideNConquer
            
            print("Closest pair is Using Divide and Conquer: ")
            print("Point A: ", point1DC)
            print("Point B: ", point2DC)
            print("Distance: ", minDistanceDC)
            print("Time: ", timeDivideNConquer)
            print("Times euclidean distance called: ", euclidN)

            print()

            # plot 3D
            if ((n > 0) and (dimension == 3)):
                three_dimensional_plotting(arrOfPoint, point1BF, point2BF)
                three_dimensional_plotting(arrOfPoint, point1DC, point2DC)
