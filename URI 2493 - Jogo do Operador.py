while True:
    try:
        T = int(input())
        
        expressionsResult = []

        for expression in range(T):
            X, expression2 = input().split()
            Y, Z = expression2.split('=')
            X, Y, Z = int(X), int(Y), int(Z)
            answer = ''

            if Z == X + Y:
                answer = '+'
            elif Z == X - Y:
                answer = '-'
            elif Z == X * Y:
                answer = '*'
            else:
                answer = 'I'

            expressionsResult.append(answer)
        
        playersThatWontAdvance = []

        for player in range(T):
            name, choice, response = input().split()

            for index, result in enumerate(expressionsResult, 1):
                if int(choice) == index:
                    if response != result:
                        playersThatWontAdvance.append(name)
        
        playersThatWontAdvance.sort()

        if len(playersThatWontAdvance) == 0:
            print('You Shall All Pass!')
        elif len(playersThatWontAdvance) == T:
            print('None Shall Pass!')
        else:
            print(*playersThatWontAdvance)

    except EOFError:
        break
