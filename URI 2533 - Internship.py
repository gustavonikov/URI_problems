while True:
    try:
        M = int(input())

        numerators = []
        workloads = []

        for case in range(M):
            N, C = input().split()
            numerator = int(N) * int(C)
            numerators.append(numerator)
            workload = int(C) * 100
            workloads.append(workload)
        
        API = sum(numerators)/sum(workloads)
        print('%.4f'%API)

    except EOFError:
        break