measures = input().split()

measures = [int(i) for i in measures]

measures.sort(reverse = True)

A, B, C = measures[0], measures[1], measures[2]
rectangle = ''

if A >= (B + C):
    print('Invalido')
else:
    if A**2 == (B**2 + C**2):
        rectangle = 'S'
    else:
        rectangle = 'N'
        
    if A == B == C:
        print('Valido-Equilatero')
        print(f'Retangulo: {rectangle}')
    elif (A == B != C) or (A == C != B) or (B == C != A):
        print('Valido-Isoceles')
        print(f'Retangulo: {rectangle}')
    elif A != B != C:
        print('Valido-Escaleno')
        print(f'Retangulo: {rectangle}')
    