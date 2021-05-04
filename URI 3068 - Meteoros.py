test = 0

while True:
    x1, y1, x2, y2 = input().split()

    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    test += 1

    if x1 == y1 == x2 == y2 == 0:
        break

    N = int(input())

    meteorites = 0

    for meteorite in range(N):
        x, y = input().split()

        x, y = int(x), int(y)

        if x1 <= x <= x2 and y2 <= y <= y1:
            meteorites += 1

    print(f'Teste {test}\n{meteorites}')