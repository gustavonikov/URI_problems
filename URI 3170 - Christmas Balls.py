import math

b = int(input())
g = int(input())

numberOfBallsThatShouldHave = math.floor(g/2)

numberOfBallsToComplete = numberOfBallsThatShouldHave - b

if numberOfBallsToComplete <= 0:
    print('Amelia tem todas bolinhas!')
else:
    print(f'Faltam {numberOfBallsToComplete} bolinha(s)')