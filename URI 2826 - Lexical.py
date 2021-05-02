A = input()
B = input()

if A in B:
    print(f'{A}\n{B}')
elif B in A:
    print(f'{B}\n{A}')
else:
    for index, letter in enumerate(A):
        lettA = ord(A[index]) - 96
        lettB = ord(B[index]) - 96
        if lettA < lettB:
            print(f'{A}\n{B}')
            break
        elif lettB < lettA:
            print(f'{B}\n{A}')
            break
        if lettA == lettB:
            next