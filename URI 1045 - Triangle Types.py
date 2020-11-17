numbers = input().split()

numbers = [float(i) for i in numbers]

numbers.sort(reverse = True)

A = numbers[0]
B = numbers[1]
C = numbers[2]

if A >= (B + C):
    print('NAO FORMA TRIANGULO')

else:
    if A**2 == (B**2 + C**2):
        print('TRIANGULO RETANGULO')

    if A**2 > (B**2 + C**2):
        print('TRIANGULO OBTUSANGULO')

    if A**2 < (B**2 + C**2):
        print('TRIANGULO ACUTANGULO')

    if A == B == C:
        print('TRIANGULO EQUILATERO')

    if (A == B != C) or (A == C != B) or (B == C != A):
        print('TRIANGULO ISOSCELES')