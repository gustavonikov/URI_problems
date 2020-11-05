while True:
    N = int(input())

    if N == 0:
        break

    array = [[1 for element in range(N)] for vector in range(N)]

    aboveCountLine = 1

    for indexLine, lines in enumerate(array[:(N-1)]):
        aboveCount = 0
        newIndex = indexLine + 1
        for numbers in lines[aboveCountLine:]:
            lines[newIndex + aboveCount] = aboveCount + 2
            aboveCount += 1
        aboveCountLine += 1

    bellowCountLine = 1

    for indexLine, lines in enumerate(array[1:N]):
        indexNumber = 0
        bellowCount = 0
        newValue = indexLine + 2
        for numbers in lines[:bellowCountLine]:
            lines[indexNumber] = newValue + bellowCount
            indexNumber += 1
            bellowCount -= 1
        bellowCountLine += 1

    for vector in array:
        result = ''
        for element in vector:
            result += ' %3d' %element
        print(result[1:])
    print()
