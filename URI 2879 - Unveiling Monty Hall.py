N = int(input())

count = 0

for test in range(N):
    doorNumber = int(input())

    if doorNumber != 1:
        count += 1

print(count)