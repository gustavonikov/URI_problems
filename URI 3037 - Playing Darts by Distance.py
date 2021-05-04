N = int(input())

for test in range(N):
    x1, d1 = input().split()
    x2, d2 = input().split()
    x3, d3 = input().split()
    x4, d4 = input().split()
    x5, d5 = input().split()
    x6, d6 = input().split()

    x1, x2, x3 = int(x1), int(x2), int(x3)
    d1, d2, d3 = int(d1), int(d2), int(d3)
    x4, x5, x6 = int(x4), int(x5), int(x6)
    d4, d5, d6 = int(d4), int(d5), int(d6)

    johnResult = (x1*d1) + (x2*d2) + (x3*d3)
    maryResult = (x4*d4) + (x5*d5) + (x6*d6)

    if johnResult > maryResult:
        print('JOAO')
    else:
        print('MARIA')