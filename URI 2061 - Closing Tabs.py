N, M = input().split()
N, M = int(N), int(M)

for actions in range(M):
    action = input()
    if action == 'fechou':
        N -= 1
        N += 2
    else:
        N -= 1

print(N)
