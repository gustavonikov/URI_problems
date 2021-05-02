number = input()

firstPart, secondPart = number.split('.')
firstPart, secondPart = int(firstPart), int(secondPart)

print(f'{secondPart}.{firstPart}')