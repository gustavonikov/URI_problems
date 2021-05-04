N = int(input())

for test in range(N):
    h, d, g = input().split()

    h, d, g = int(h), int(d), int(g)

    if 200 <= h <= 300 and d >= 50 and g >= 150:
        print('Sim')
    else:
        print('Nao')
