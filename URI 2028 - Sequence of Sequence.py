countCases = 0

while True:
    try:
        N = int(input())
        countCases += 1
        cases = []
        cases.append(0)

        for number in range(1, N + 1):
            count = 0
            
            while count < number:
                cases.append(number)
                count += 1

        if len(cases) == 1:
            print(f'Caso {countCases}: {len(cases)} numero')
            print(*cases)
        else:
            print(f'Caso {countCases}: {len(cases)} numeros')
            print(*cases)
        print()
        
    except EOFError:
        break