values = input().split()

A = int(values[0])
B = int(values[1])
C = int(values[2])
D = int(values[3])

sumCD = C + D
sumAB = A + B

if B > C and D > A and sumCD > sumAB and C > 0 and D > 0 and A%2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')