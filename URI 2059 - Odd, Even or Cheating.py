p, j1, j2, r, a = input().split()
p, j1, j2, r, a = int(p), int(j1), int(j2), int(r), int(a)

result = j1 + j2
cheatingStatus = False

if r == 1 and a == 0:
    cheatingStatus = 'Undiscovered'
elif r == 1 and a == 1:
    cheatingStatus = 'Discovered'

if (result % 2 == 0 and p == 1) and cheatingStatus == False:
    print('Jogador 1 ganha!')
elif (result % 2 != 0 and p == 0) and cheatingStatus == False:
    print('Jogador 1 ganha!')
elif cheatingStatus == 'Undiscovered':
    print('Jogador 1 ganha!')
else:
    print('Jogador 2 ganha!')

