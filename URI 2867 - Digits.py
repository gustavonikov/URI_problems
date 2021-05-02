C = int(input())

for test in range(C):
    N, M = input().split()

    N, M = int(N), int(M)

    result = N**M

    result = str(result)

    print(len(result))