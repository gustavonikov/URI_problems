N = int(input())

value = 1

for number in range(N):
    print(value, value**2, value**3)
    print(value, value**2 + 1, value**3 + 1)

    value += 1
