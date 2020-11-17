P, N = input().split()
P, N = int(P), int(N)

pipesHeight = input().split(maxsplit = N)
pipesHeight = [int(i) for i in pipesHeight]
gameIsOver = False

for index, pipeHeight in enumerate(pipesHeight[:-1]):
    difference = pipesHeight[index + 1] - pipesHeight[index]
    if abs(difference) > P:
        gameIsOver = True
        break

if gameIsOver == True:
    print('GAME OVER')
else:
    print('YOU WIN')
