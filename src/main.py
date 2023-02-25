from bruteForce import *
from divideNConquer import *
from statistic import *

if __name__ == '__main__':
    # input n points
    n = int(input("Enter number of points: "))

    # input d dimension
    dimension = int(input("Enter dimension: "))

    while True:
        # inisialize array of points
        arrOfPoint = []
        
        # generate random points
        for i in range(n):
            arrOfPoint = arrOfPoint + [[randomUniform(-10000000, 10000000) for j in range(dimension)]]
        
        # print array of points
        # print("Array of points: ")
        # for i in range(n):
        #     print(arrOfPoint[i])
        # print()

        # get closest pair by brute force
        timeBruteForce = currentTime()
        point1BF, point2BF, minDistanceBF = getClosestPairByBruteForce(arrOfPoint, n, dimension)
        timeBruteForce = currentTime() - timeBruteForce

        # get closest pair by divide and conquer
        timeDivideNConquer = currentTime()
        point1DC, point2DC, minDistanceDC= getClosestPairByDivideNConquer(arrOfPoint, n, dimension)
        timeDivideNConquer = currentTime() - timeDivideNConquer

        # print result
        # print("Closest pair is Using Brute Force: ")
        # print("Point A: ", point1BF)
        # print("Point B: ", point2BF)
        # print("Distance: ", minDistanceBF)
        # print("Time: ", timeBruteForce)

        # print()

        # print("Closest pair is Using Divide and Conquer: ")
        # print("Point A: ", point1DC)
        # print("Point B: ", point2DC)
        # print("Distance: ", minDistanceDC)
        # print("Time: ", timeDivideNConquer)

        if (minDistanceBF != minDistanceDC):
            break
    
    print("Closest pair is Using Brute Force: ")
    print("Point A: ", point1BF)
    print("Point B: ", point2BF)
    print("Distance: ", minDistanceBF)
    print("Time: ", timeBruteForce)

    print()

    print("Closest pair is Using Divide and Conquer: ")
    print("Point A: ", point1DC)
    print("Point B: ", point2DC)
    print("Distance: ", minDistanceDC)
    print("Time: ", timeDivideNConquer)

    # write to file error test case
    import os
    nFile = len(os.listdir("./txt"))
    fileName = "./txt/tc" + str(nFile) + ".txt"

    with open(fileName, "w") as f:
        for i in range(n):
            for j in range(dimension):
                if j == dimension - 1:
                    f.write(str(arrOfPoint[i][j]))
                else:
                    f.write(str(arrOfPoint[i][j]) + ", ")
            f.write("\n")
    f.close()