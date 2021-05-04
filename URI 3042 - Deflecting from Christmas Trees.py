while True:
    M = int(input())

    if M == 0:
        break

    lastPosition = 1

    for test in range(M):
        positions = input().split()
        positions = [int(i) for i in positions]

        for index, position in enumerate(positions):        
            if position == 1 and lastPosition == index:
                if index == 0:
                    if position[index + 1] == 0:
                        lastPosition = index + 1
                        break
                    else:
                        lastPosition = index + 2
                    break
                elif index == 1:
                    if position[index - 1] == 0:
                        lastPosition = index


