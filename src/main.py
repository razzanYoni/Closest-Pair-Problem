from bruteForce import getClosestPairByBruteForce
from divideNConquer import getClosestPairByDivideNConquer
from visualization import three_dimensional_plotting
import tools
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    # input n points
    n = int(input("Enter number of points: "))

    # input d dimension
    dimension = int(input("Enter dimension: "))

    #while True and (n > 0) and (dimension > 0):
    # inisialize array of points
    arrOfPoint = []
    
    # generate random points
    for i in range(n):
        temp = [tools.randomUniform(0, 10000000) for j in range(2)] + [tools.randomUniform(-10, 0) for j in range(dimension - 2)]
        arrOfPoint = arrOfPoint + [temp]
    
    # print array of points
    # print("Array of points: ")
    # for i in range(n):
    #     print(arrOfPoint[i])
    # print()

    # get closest pair by brute force
    tools.initializeCounter()
    timeBruteForce = tools.currentTime()
    point1BF, point2BF, minDistanceBF = getClosestPairByBruteForce(arrOfPoint, n, dimension)
    timeBruteForce = tools.currentTime() - timeBruteForce

    # get closest pair by divide and conquer
    

    # print result
    # print("Closest pair is Using Brute Force: ")
    # print("Point A: ", point1BF)
    # print("Point B: ", point2BF)
    # print("Distance: ", minDistanceBF)
    # print("Time: ", timeBruteForce)

    # print("Closest pair is Using Divide and Conquer: ")
    # print("Point A: ", point1DC)
    # print("Point B: ", point2DC)
    # print("Distance: ", minDistanceDC)
    # print("Time: ", timeDivideNConquer)

    # print()

    #    if (minDistanceBF != minDistanceDC):
    #        break
    
    # print difference between 2 methods
    print("Closest pair is Using Brute Force: ")
    print("Point A: ", point1BF)
    print("Point B: ", point2BF)
    print("Distance: ", minDistanceBF)
    print("Time: ", timeBruteForce)
    print("Times euclidean distance called: ", tools.euclidN)

    tools.initializeCounter()
    timeDivideNConquer = tools.currentTime()
    point1DC, point2DC, minDistanceDC= getClosestPairByDivideNConquer(arrOfPoint, n, dimension)
    timeDivideNConquer = tools.currentTime() - timeDivideNConquer
    
    print("Closest pair is Using Divide and Conquer: ")
    print("Point A: ", point1DC)
    print("Point B: ", point2DC)
    print("Distance: ", minDistanceDC)
    print("Time: ", timeDivideNConquer)
    print("Times euclidean distance called: ", tools.euclidN)

    print()

    # plot 3D
    if ((n > 0) and (dimension == 3)):
        three_dimensional_plotting(arrOfPoint, point1BF, point2BF)
        three_dimensional_plotting(arrOfPoint, point1DC, point2DC)

    # write to file error test case
    import os
    nFile = len(os.listdir("./test"))
    fileName = "./test/tc" + str(nFile) + ".txt"

    with open(fileName, "w") as f:
        for i in range(n):
            for j in range(dimension):
                if j == dimension - 1:
                    f.write(str(arrOfPoint[i][j]))
                else:
                    f.write(str(arrOfPoint[i][j]) + " ")
            f.write("\n")
    f.close()
