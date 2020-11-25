while True:
    X, M = input().split()
    X, M = int(X), int(M)

    if X == 0 and M == 0:
        break
    
    result = X * M
    print(result)