N = int(input())
result = N

for factorial in range(1, N):
    result *= (N - factorial)

print(result)