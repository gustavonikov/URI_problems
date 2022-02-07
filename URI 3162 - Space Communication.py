N = int(input())

shipsCoordinates = []

for ship in range(N):
    shipCoordinate = input().split()
    shipsCoordinates.append(shipCoordinate)

for index, ships in enumerate(shipsCoordinates):
    x1, y1, z1 = int(ships[0]), int(ships[1]), int(ships[2])
    distance = 0
    currentDistance = 0
    
    for indexTwo, shipsTwo in enumerate(shipsCoordinates):
        x2, y2, z2 = int(shipsTwo[0]), int(shipsTwo[1]), int(shipsTwo[2])
        if indexTwo != index:
            currentDistance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2)
            
            if distance == 0 or currentDistance < distance:
                distance = currentDistance

    if distance <= 20:
        print('A')
    elif distance > 20 and distance <= 50:
        print('M')
    elif distance > 50:
        print('B')
