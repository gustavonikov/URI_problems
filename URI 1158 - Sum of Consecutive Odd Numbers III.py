N = int(input())

for cases in range(0, N):
    X, Y = input().split()
    X, Y = int(X), int(Y)

    result = 0

    if X % 2 == 0:
        for number in range(X + 1, X + (Y * 2), 2):
            result += number
    else:
        for number in range(X, X + (Y * 2), 2):
            result += number

    print(result)