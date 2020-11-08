O = input()

array = []

for lines in range(0, 12):
    arrayLine = []

    for numbers in range(0, 12):
        number = input()
        number = float(number)
        arrayLine.append(number)
    
    array.append(arrayLine)

belowTheDiagonal = []
count = 11

for lines in array[1:]:
    for numbers in lines[count:]:
        belowTheDiagonal.append(numbers)
    
    count -= 1

elementsSum = sum(belowTheDiagonal)
elementsAverage = elementsSum/len(belowTheDiagonal)

if O == 'S':
    print('%.1f'%elementsSum)

elif O == 'M':
    print('%.1f'%elementsAverage)
