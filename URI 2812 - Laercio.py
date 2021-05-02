N = int(input())

for test in range(N):
    M = int(input())

    List = input().split(maxsplit=M)

    oddList = []

    for number in List:
        number = int(number)

        if number % 2 != 0:
            oddList.append(number)

    reorderedOddList = []
    
    for number in range(1, len(oddList) + 1):
        if number % 2 != 0:
            biggestOdd = max(oddList)

            reorderedOddList.append(biggestOdd)
            oddList.remove(biggestOdd)
        else:
            lowestOdd = min(oddList)

            reorderedOddList.append(lowestOdd)
            oddList.remove(lowestOdd)
    
    print(*reorderedOddList)