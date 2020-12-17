movements = 0
totalPeople = 0

while True:
    try:
        movement, people = input().split()
    except ValueError:
        print(totalPeople)
        print(movements)
        break

    if movement == 'SALIDA':
        movements += 1
        totalPeople += int(people)
    elif movement == 'VUELTA':
        movements -= 1
        totalPeople -= int(people)
