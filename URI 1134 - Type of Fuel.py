Alcohol = 0
Gasoline = 0
Diesel = 0

while True:
    X = int(input())

    if X < 1 or X > 4:
        X = int(input())

    if X == 1:
        Alcohol += 1
    elif X == 2:
        Gasoline += 1
    elif X == 3:
        Diesel += 1
    elif X == 4:
        print('MUITO OBRIGADO')
        print(f'Alcool: {Alcohol}')
        print(f'Gasolina: {Gasoline}')
        print(f'Diesel: {Diesel}')
        break
