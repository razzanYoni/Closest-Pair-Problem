from time import time as currentTime
from random import uniform as randomUniform

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

    
if __name__ == "__main__":
    arrOfPoint1 = []
    
    # generate random points
    n = 100000
    for i in range(n):
        temp = [randomUniform(-10, 10) for j in range(2)]
        arrOfPoint1 = arrOfPoint1 + [temp]

    #copy
    arrOfPoint2 = [0 for i in range(n)]
    for i in range(n):
        arrOfPoint2[i] = arrOfPoint1[i]

    timex = currentTime()
    #sortArraym(arrOfPoint2, 0, n)
    sortArrayq(arrOfPoint2, 0, 0, n-1)
    print(arrOfPoint2)
    print(currentTime()-timex)

    print("\n------------------------\n")
    
    timex = currentTime()
    print(sorted(arrOfPoint1, key = lambda x: x[0]))
    print(currentTime()-timex)