from bruteForce import getClosestPairByBruteForce
from divideNConquer import getClosestPairByDivideNConquer
from visualization import three_dimensional_plotting
import tools
from sys import setrecursionlimit

def main():
    setrecursionlimit(100000)
    exit = False
    while not(exit) :
        inputUser = -1
        print("""
Input action:
1. Random
2. Read File
3. exit""")
        try:
            inputUser = int(input("-> "))
            if inputUser == 1 :
                n = int(input("Enter number of points: "))
                if n < 2:
                    raise Exception("Number of points must be larger than 1")
                dimension = int(input("Enter dimension: "))
                if dimension < 1:
                    raise Exception("Dimension must be larger than 0")
                arrOfPoint = []
                for i in range(n):
                    temp = [randomUniform(-100, 100) for j in range(dimension)]
                    arrOfPoint = arrOfPoint + [temp]
            elif inputUser == 2 :
                fileName = input("Input File Name: ")
                arrOfPoint, n, dimension = readFile(fileName)
            elif inputUser == 3 :
                exit = True
            else :
                pass    
        except Exception as exception:
            print(exception)
            inputUser = -1
        if ((inputUser == 1) or (inputUser == 2)) :
            tools.initializeCounter()
            timeBruteForce = tools.currentTime()
            point1BF, point2BF, minDistanceBF = getClosestPairByBruteForce(arrOfPoint, n, dimension)
            timeBruteForce = tools.currentTime() - timeBruteForce
            print("Closest pair is Using Brute Force: ")
            print("Point A: ", point1BF)
            print("Point B: ", point2BF)
            print("Distance: ", minDistanceBF)
            print("Time: ", timeBruteForce)
            print("Times euclidean distance called: ", tools.euclidN)
            tools.initializeCounter()
            timeDivideNConquer = tools.currentTime()
            tools.sortArrayq(arrOfPoint, 0, 0, n-1)
            point1DC, point2DC, minDistanceDC= getClosestPairByDivideNConquer(arrOfPoint, n, dimension)
            timeDivideNConquer = tools.currentTime() - timeDivideNConquer
            print("Closest pair is Using Divide and Conquer: ")
            print("Point A: ", point1DC)
            print("Point B: ", point2DC)
            print("Distance: ", minDistanceDC)
            print("Time: ", timeDivideNConquer)
            print("Times euclidean distance called: ", tools.euclidN)
            print()
            if ((1 < n <= 1000) and (dimension == 3)):            
                three_dimensional_plotting(arrOfPoint, point1BF, point2BF, "Brute Force")
                three_dimensional_plotting(arrOfPoint, point1DC, point2DC, "Divide and Conquer")


if __name__ == '__main__':
    main()