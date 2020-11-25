N = int(input())

teamServes, teamBlocks, teamAttacks = 0, 0, 0
teamSuccessfulServes, teamSuccessfulBlocks, teamSuccessfulAttacks = 0, 0, 0

for player in range(N):
    name = input()
    serves, blocks, attacks = input().split()
    successfulServes, successfulBlocks, successfulAttacks = input().split()
    serves, blocks, attacks = int(serves), int(blocks), int(attacks)
    successfulServes, successfulBlocks = int(successfulServes), int(successfulBlocks)
    successfulAttacks = int(successfulAttacks)

    teamServes += serves
    teamSuccessfulServes += successfulServes
    teamBlocks += blocks
    teamSuccessfulBlocks += successfulBlocks
    teamAttacks += attacks
    teamSuccessfulAttacks += successfulAttacks

servesRate = (teamSuccessfulServes/teamServes) * 100
blocksRate = (teamSuccessfulBlocks/teamBlocks) * 100
attacksRate = (teamSuccessfulAttacks/teamAttacks) * 100

print('Pontos de Saque: {:.2f} %.'.format(servesRate))
print('Pontos de Bloqueio: {:.2f} %.'.format(blocksRate))
print('Pontos de Ataque: {:.2f} %.'.format(attacksRate))
