while True:
    try:
        N = int(input())

        array = [[3 for element in range(N)] for vector in range(N)]

        firstDiagonalCountLeft = 0
        firstDiagonalCountRight = 1

        for lines in array:
            for number in lines[firstDiagonalCountLeft:firstDiagonalCountRight]:
                lines[firstDiagonalCountLeft] = 1
            firstDiagonalCountLeft += 1
            firstDiagonalCountRight += 1

        secondDiagonalCountLeft = N-1
        secondDiagonalCountRight = N

        for lines in array:
            for number in lines[secondDiagonalCountLeft:secondDiagonalCountRight]:
                lines[secondDiagonalCountLeft] = 2
            secondDiagonalCountLeft -= 1
            secondDiagonalCountRight -= 1

        for lines in array:
            print(*lines, sep='')

    except EOFError:
        break