N = []

for value in range(0, 20):
    N.append(input())

N.reverse()

for index, number in enumerate(N):
    print(f'N[{index}] = {number}')