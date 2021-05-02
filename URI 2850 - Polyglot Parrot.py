while True:
    try:
        raisingCondition = input().split(maxsplit=2)
        
        parrotLegsRaisingCondition = ''

        if len(raisingCondition) == 2:
            parrotLegsRaisingCondition = raisingCondition[0] + ' ' + raisingCondition[1]
        else:
            parrotLegsRaisingCondition = raisingCondition[0]
            

        if parrotLegsRaisingCondition == 'esquerda':
            print('ingles')
        elif parrotLegsRaisingCondition == 'direita':
            print('frances')
        elif parrotLegsRaisingCondition == 'nenhuma':
            print('portugues')
        elif parrotLegsRaisingCondition == 'as duas':
            print('caiu')
            
    except EOFError:
        break