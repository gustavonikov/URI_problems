X, Y = input().split()
X, Y = int(X), int(Y)


for numberY in range(0, Y, X):
    numbers = []
    for numberX in range(1, X + 1):
        numberY += 1
        numbers.append(numberY)
    print(*numbers)