while True:
    T = int(input())

    if T == 0:
        break

    for cases in range(T):
        N = int(input())

        if N % 2 != 0:
            sumOfOrders = N * 2 - 1
            print(sumOfOrders)
        else:
            sumOfOrders = N * 2 - 2
            print(sumOfOrders)
