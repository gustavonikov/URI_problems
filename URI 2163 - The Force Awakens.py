N, M = input().split()
N, M = int(N), int(M)

array = []

for row in range(N):
    values = input().split()
    values = [int(value) for value in values]
    array.append(values)

haveALightsaber = False
coordinate = []

for vectorIndex, vector in enumerate(array[1:-1], 1):
    for elementIndex, element in enumerate(vector[1:-1], 1):
        if element == 42:
            if vector[elementIndex + 1] == 7 and \
            vector[elementIndex - 1] == 7 and \
            array[vectorIndex - 1][elementIndex] == 7 and \
            array[vectorIndex + 1][elementIndex] == 7  and \
            array[vectorIndex - 1][elementIndex - 1] == 7 and \
            array[vectorIndex + 1][elementIndex - 1] == 7 and \
            array[vectorIndex - 1][elementIndex + 1] == 7 and \
            array[vectorIndex + 1][elementIndex + 1] == 7:
                haveALightsaber = True
                coordinate.append(vectorIndex + 1)
                coordinate.append(elementIndex + 1)
                break
    if haveALightsaber == True:
        break
    
if haveALightsaber == True:
    print(*coordinate)
else:
    print(0, 0)