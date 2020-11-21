cases = int(input())

for case in range(cases):
    H, M, O = input().split()

    if len(H) == 1:
        H = '0' + H
    if len(M) == 1:
        M = '0' + M

    if O == '1':
        print(f'{H}:{M} - A porta abriu!')
    else:
        print(f'{H}:{M} - A porta fechou!')