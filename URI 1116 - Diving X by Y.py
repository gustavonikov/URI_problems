N = int(input())

for numbers in range(0, N):
    X, Y = input().split()
    X, Y = int(X), int(Y)

    try:
        division = X / Y
        print('%.1f'%division)
    except:
        print('divisao impossivel')
   