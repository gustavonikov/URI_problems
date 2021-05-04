N, X = input().split()

N, X = int(N), int(X)
adventurers = 2 + N

days = X / adventurers

print('%.2f'%days)