from main import *

"""DEBUG MODE"""	
if __name__ == '__main__':
    sys.setrecursionlimit(100000)

    fileName = './test/tc6.txt'

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

    tools.initializeCounter()
    timeBruteForce = tools.currentTime()
    point1BF, point2BF, minDistanceBF = getClosestPairByBruteForce(arrOfPoints, n, dimension)
    timeBruteForce = tools.currentTime() - timeBruteForce

    print("Closest pair is Using Brute Force: ")
    print("Point A: ", point1BF)
    print("Point B: ", point2BF)
    print("Distance: ", minDistanceBF)
    print("Time: ", timeBruteForce)
    print("Times euclidean distance called: ", tools.euclidN)

    print()

    tools.initializeCounter()
    timeDivideNConquer = tools.currentTime()
    point1DC, point2DC, minDistanceDC= getClosestPairByDivideNConquer(arrOfPoints, n, dimension)
    timeDivideNConquer = tools.currentTime() - timeDivideNConquer

    print("Closest pair is Using Divide and Conquer: ")
    print("Point A: ", point1DC)
    print("Point B: ", point2DC)
    print("Distance: ", minDistanceDC)
    print("Time: ", timeDivideNConquer)
    print("Times euclidean distance called: ", tools.euclidN)

    #if ((n > 0) and (dimension == 3)):
    #    three_dimensional_plotting(arrOfPoints, point1BF, point2BF)
    #    three_dimensional_plotting(arrOfPoints, point1DC, point2DC)
