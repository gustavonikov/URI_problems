N = int(input())

for cases in range(0, N):
    X = int(input())

    divisors = []

    for divisor in range(1, X + 1):
        if X % divisor == 0:
            divisors.append(divisor)
    
    if sum(divisors) == (X + 1):
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')