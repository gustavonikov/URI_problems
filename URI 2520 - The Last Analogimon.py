while True:
    try:
        N, M = input().split()
        N, M = int(N), int(M)

        array = []

        for rows in range(N):
            column = input().split()
            column = [int(i) for i in column]
            array.append(column)

        analogimonPosition = []
        myPosition = []

        for rowIndex, rows in enumerate(array):
            for elementIndex, element in enumerate(rows):
                if element == 2:
                    analogimonPosition = [rowIndex, elementIndex]
                elif element == 1:
                    myPosition = [rowIndex, elementIndex]

        minimumTime = abs(myPosition[0] - analogimonPosition[0]) + abs(myPosition[1] - analogimonPosition[1])
        print(minimumTime)

    except EOFError:
        break
