A, B, C = input().split()
A, B, C = int(A), int(B), int(C)

if A == B + C or B == A + C or C == A + B or A == B or B == C or A == C:
    print('S')
else:
    print('N')