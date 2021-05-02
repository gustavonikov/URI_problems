T = int(input())

for test in range(T):
    N, K = input().split()

    N, K = int(N), int(K)

    result = (N // K) + (N % K)

    print(result)