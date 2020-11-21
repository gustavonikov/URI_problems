calendar = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

while True:
    try:
        month, days = input().split()
        month, days = int(month), int(days)

        if month == 12 and days == 24:
            print('E vespera de natal!')
        elif month == 12 and days == 25:
            print('E natal!')
        elif month == 12 and days > 25:
            print('Ja passou!')
        else:
            totalDaysPassed = sum(calendar[0:month])
            daysLeft = 360 - (totalDaysPassed + days)
            print(f'Faltam {daysLeft} dias para o natal!')

    except EOFError:
        break