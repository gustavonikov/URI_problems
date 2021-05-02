import functools

K = int(input())

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fibonot = list(range(4, fib(26)))

fibonacci = 0
count = 1

while fibonacci <= (K):
    fibonacci = fib(count)

    if fibonot.__contains__(fibonacci):
        fibonot.remove(fibonacci)

    count += 1

print(fibonot[K-1])