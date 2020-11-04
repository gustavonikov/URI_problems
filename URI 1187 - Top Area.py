O = input()

array = []

for lines in range(0, 12):
    arrayLine = []

    for numbers in range(0, 12):
        number = input()
        number = float(number)
        arrayLine.append(number)
    
    array.append(arrayLine)

aboveTheDiagonal = []
countLeft = 1
countRight = 11

for lines in array[:5]:
    for numbers in lines[countLeft:countRight]:
        aboveTheDiagonal.append(numbers)
    
    countLeft += 1
    countRight -= 1

elementsSum = sum(aboveTheDiagonal)
elementsAverage = elementsSum/len(aboveTheDiagonal)

if O == 'S':
    print('%.1f'%elementsSum)

elif O == 'M':
    print('%.1f'%elementsAverage)
