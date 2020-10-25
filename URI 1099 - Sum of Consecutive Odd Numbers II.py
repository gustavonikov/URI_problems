N = int(input())

allOddNumbersSum = []

for numb in range(0, N):
    X, Y = input().split()
    X, Y = int(X), int(Y)

    oddNumbers = []

    if X > Y:
        X1 = Y
        X2 = X
    else:
        X1 = X
        X2 = Y

    if X1 % 2 != 0:
        for number in range(X1, X2, 2)[1:]:
            oddNumbers.append(number)
    else:
        for number in range(X1 + 1, X2, 2):
            oddNumbers.append(number)
    
    allOddNumbersSum.append(sum(oddNumbers))

for oddNumber in allOddNumbersSum:
    print(oddNumber)
