N = int(input())

values = []

for test in range(N):
    values.append(int(input()))

biggest = max(values)

if values.index(biggest) == 0:
    print('S')
else:
    print('N')