countCases = 0

while True:
    try:
        N1 = input()
        N2 = input()
        countCases += 1
        subSequences = 0
        position = []

        for index, letter in enumerate(N2):
            subString = N2[index:index + len(N1)]
            
            if subString == N1:
                subSequences += 1
                position.append(index + 1)

        print(f'Caso #{countCases}:')
        if subSequences == 0:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: {subSequences}')
            print(f'Pos: {position[-1]}')
        print()
        
    except EOFError:
        break