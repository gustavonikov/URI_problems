N = int(input())

for cases in range(N):
    signPlayer1 = input()
    signPlayer2 = input()

    if signPlayer1 == 'ataque' and (signPlayer2 == 'pedra' or signPlayer2 == 'papel'):
        print('Jogador 1 venceu')
    elif signPlayer2 == 'ataque' and (signPlayer1 == 'pedra' or signPlayer1 == 'papel'):
        print('Jogador 2 venceu')
    elif signPlayer1 == 'pedra' and signPlayer2 == 'papel':
        print('Jogador 1 venceu')
    elif signPlayer2 == 'pedra' and signPlayer1 == 'papel':
        print('Jogador 2 venceu')
    elif signPlayer1 == 'ataque' and signPlayer2 == 'ataque':
        print('Aniquilacao mutua')
    elif signPlayer1 == 'pedra' and signPlayer2 == 'pedra':
        print('Sem ganhador')
    elif signPlayer1 == 'papel' and signPlayer2 == 'papel':
        print('Ambos venceram')