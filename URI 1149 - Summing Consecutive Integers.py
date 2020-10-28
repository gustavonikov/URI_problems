numbers = input().split()
A = int(numbers[0])
N = int(numbers[-1])

sumCount = 0

for number in range(0, N):
    sumCount += A + number

print(sumCount)