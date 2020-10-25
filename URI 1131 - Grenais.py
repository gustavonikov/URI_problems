X = 0
grenaisGoals = []
interVictories = 0
gremioVictories = 0
ties = 0

while True:
    InterGoals, GremioGoals = input().split()
    InterGoals, GremioGoals = int(InterGoals), int(GremioGoals)
    goals = [InterGoals, GremioGoals]
    grenaisGoals.append(goals)

    print('Novo grenal (1-sim 2-nao)')
    X = int(input())

    if X == 1:
        continue
    elif X == 2:
        print(f'{len(grenaisGoals)} grenais')

        for grenais in grenaisGoals:
            if grenais[0] > grenais[1]:
                interVictories += 1
            elif grenais[0] < grenais[1]:
                gremioVictories += 1
            elif grenais[0] == grenais[1]:
                ties += 1
        
        print(f'Inter:{interVictories}')
        print(f'Gremio:{gremioVictories}')
        print(f'Empates:{ties}')

        if interVictories > gremioVictories:
            print('Inter venceu mais')
        elif interVictories < gremioVictories:
            print('Gremio venceu mais')
        elif interVictories == gremioVictories:
            print('Nao houve vencedor')
        break
