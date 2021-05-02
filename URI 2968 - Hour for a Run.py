import math

V, N = input().split()

V, N = int(V), int(N)

totalLaps = V * N

signs = []

for sign in range(1, 10):
    mark = math.ceil(totalLaps*(sign/10))
    signs.append(mark)

print(*signs)