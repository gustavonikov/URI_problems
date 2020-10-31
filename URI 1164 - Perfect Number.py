N = int(input())

for number in range(0, N):
    X = int(input())

    divisors = []

    for divisor in range(1, X):
        if X % divisor == 0:
            divisors.append(divisor)
    
    if sum(divisors) == X:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')