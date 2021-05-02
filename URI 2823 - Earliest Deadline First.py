N = int(input())

total = 0

for test in range(N):
    C, P = input().split()
    C, P = int(C), int(P)

    total += C/P

if total > 1:
    print('FAIL')
else:
    print('OK')
