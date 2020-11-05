while True:
    N = int(input())

    if N == 0:
        break

    array = [[] for vector in range(N)]

    value = 1

    for vector in array:
        multiplier = 1
        for number in range(N):
            number = multiplier * value
            vector.append(number)
            multiplier *= 2
        value *= 2

    allNumbers = []

    for vector in array:
        for element in vector:
            allNumbers.append(element)

    allNumbers.sort(reverse=True)
    biggestNumber = str(allNumbers[0])
    T = len(biggestNumber)

    for vector in array:
        result = ''
        for element in vector:
            elementLen = len(str(element))
            numberOfSpaces = T - elementLen
            space = numberOfSpaces * ' '
            result += space + f' {element}'
        print(result[1:])
    print()
    