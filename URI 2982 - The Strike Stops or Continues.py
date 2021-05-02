N = int(input())

expenses = 0
granted = 0

for test in range(N):
    T, C = input().split()

    C = int(C)

    if T == 'G':
        expenses += C
    else:
        granted += C

if expenses > granted:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
else:
    print('A greve vai parar.')