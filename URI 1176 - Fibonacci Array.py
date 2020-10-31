fibonacciSequence = [0, 1]

for number in range(2, 62):
    fibonacciNumber = fibonacciSequence[-1] + fibonacciSequence[-2]
    fibonacciSequence.append(fibonacciNumber)

T = int(input())

for case in range(0, T):
    N = int(input())

    print(f'Fib({N}) = {fibonacciSequence[N]}')
