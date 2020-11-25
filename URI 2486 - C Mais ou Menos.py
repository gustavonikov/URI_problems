tableOfVitamins = {
    'suco de laranja': 120,
    'morango fresco' : 85,
    'mamao': 85,
    'goiaba vermelha': 70,
    'manga': 56,
    'laranja': 50,
    'brocolis': 34,
}

while True:
    T = int(input())

    if T == 0:
        break

    dailyIntakes = 0

    for intake in range(T):
        dailyIntake  = input().split()
        quantity = int(dailyIntake[0])
        source = ''

        for food in dailyIntake[1:]:
            source += food + ' '
        
        source = source[:-1]

        for food, mg in tableOfVitamins.items():
            if food == source:
                dailyIntakes += quantity * mg
    
    if dailyIntakes < 110:
        result = 110 - dailyIntakes
        print(f'Mais {result} mg')
    elif dailyIntakes > 130:
        result = dailyIntakes - 130
        print(f'Menos {result} mg')
    else:
        print(f'{dailyIntakes} mg')
