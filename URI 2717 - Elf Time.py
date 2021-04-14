N = int(input())

A, B = input().split()
A, B = int(A), int(B)

if A + B > N:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')
