N = int(input())

fibArray = [1, 1]

if N == 1:
    print(fibArray[0])
elif N == 2:
    print(*fibArray)
elif N >= 3:
    for index, number in enumerate(range(N - 2)):
        newFibNumber = fibArray[index] + fibArray[index + 1]
        fibArray.append(newFibNumber)

    fibArray.reverse()
    print(*fibArray)