N = int(input())
initialPosition = input()

index = 0

if initialPosition == 'B':
    index = 1
elif initialPosition == 'C':
    index = 2

for typeMovement in range(N):
    movement = int(input())

    if movement == 1:
        if index == 1:
            index = 0
        elif index == 0:
            index = 1
    elif movement == 2:
        if index == 1:
            index = 2
        elif index == 2:
            index = 1
    elif movement == 3:
        if index == 0:
            index = 2
        elif index == 2:
            index = 0

if index == 0:
    print('A')
elif index == 1:
    print('B')
elif index == 2:
    print('C')