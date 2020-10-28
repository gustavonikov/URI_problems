N = int(input())

fibonacciNumbers = [0, 1, 1]

for number in range(3, N):
    fibonacciNumber = fibonacciNumbers[-1] + fibonacciNumbers[-2]
    fibonacciNumbers.append(fibonacciNumber)

print(*fibonacciNumbers)
