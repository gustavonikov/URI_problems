N = int(input())

PUM = [1, 2, 3]

for numb in range(N):
    print(*PUM, 'PUM')
    PUM[:] = [numb + 4 for numb in PUM]