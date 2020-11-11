T = int(input())

sheldonWins = 'Bazinga!'
rajWins = 'Raj trapaceou!'
tie = 'De novo!'

for cases in range(T):
    sheldonAnswer, rajAnswer = input().split()

    case = f'Caso #{cases + 1}: '

    if sheldonAnswer == 'papel' and (rajAnswer == 'pedra' or rajAnswer == 'Spock'):
        print(case + sheldonWins)
    elif sheldonAnswer == 'tesoura' and (rajAnswer == 'papel' or rajAnswer == 'lagarto'):
        print(case + sheldonWins)
    elif sheldonAnswer == 'pedra' and (rajAnswer == 'lagarto' or rajAnswer == 'tesoura'):
        print(case + sheldonWins)
    elif sheldonAnswer == 'lagarto' and (rajAnswer == 'Spock' or rajAnswer == 'papel'):
        print(case + sheldonWins)
    elif sheldonAnswer == 'Spock' and (rajAnswer == 'tesoura' or rajAnswer == 'pedra'):
        print(case + sheldonWins)
    elif rajAnswer == 'papel' and (sheldonAnswer == 'pedra' or sheldonAnswer == 'Spock'):
        print(case + rajWins)
    elif rajAnswer == 'tesoura' and (sheldonAnswer == 'papel' or sheldonAnswer == 'lagarto'):
        print(case + rajWins)
    elif rajAnswer == 'pedra' and (sheldonAnswer == 'lagarto' or sheldonAnswer == 'tesoura'):
        print(case + rajWins)
    elif rajAnswer == 'lagarto' and (sheldonAnswer == 'Spock' or sheldonAnswer == 'papel'):
        print(case + rajWins)
    elif rajAnswer == 'Spock' and (sheldonAnswer == 'tesoura' or sheldonAnswer == 'pedra'):
        print(case + rajWins)
    elif sheldonAnswer == rajAnswer:
        print(case + tie)
