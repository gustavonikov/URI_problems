import math

while True:
    try:
        N = int(input())

        array = [[0 for element in range(N)] for vector in range(N)]


        firstDiagonalCountLeft = 0
        firstDiagonalCountRight = 1

        for vector in array:
            for number in vector[firstDiagonalCountLeft:firstDiagonalCountRight]:
                vector[firstDiagonalCountLeft] = 2
            firstDiagonalCountLeft += 1
            firstDiagonalCountRight += 1

        secondDiagonalCountLeft = N-1
        secondDiagonalCountRight = N

        for vector in array:
            for number in vector[secondDiagonalCountLeft:secondDiagonalCountRight]:
                vector[secondDiagonalCountLeft] = 3
            secondDiagonalCountLeft -= 1
            secondDiagonalCountRight -= 1

        middle = math.floor(N/2)

        startIndex = math.floor(N/3)
        finalIndex = N - startIndex 
        
        for indexVector, vector in enumerate(array[startIndex:finalIndex], startIndex):
            for indexElement, element in enumerate(vector[startIndex:finalIndex], startIndex):
                array[indexVector][indexElement] = 1
                
        array[middle][middle] = 4

        for vector in array:
            print(*vector, sep='')

        print()

    except EOFError:
        break