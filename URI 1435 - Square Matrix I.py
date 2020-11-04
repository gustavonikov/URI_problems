while True:
    N = int(input())

    if N == 0:
        break

    array = [[1 for element in range(N)] for vector in range(N)]

    if len(array) > 2 :
        count = 1
        for interval in range(N - 2):
            for arrays in array[count:-count]:
                for index, elements in enumerate(arrays[count:-count]):
                    arrays[index + count] = count + 1

            count += 1

    for lines in range(N):
        result = ''
        for columns in range(N):
            result += ' %3d' %array[lines][columns]
        print(result[1:])
    print()
