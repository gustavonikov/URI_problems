O = input()

array = []

for lines in range(0, 12):
    arrayLine = []

    for numbers in range(0, 12):
        number = input()
        number = float(number)
        arrayLine.append(number)
    
    array.append(arrayLine)

bellowTheDiagonal = []
count = 0

for lines in array:
    for numbers in lines[:count]:
        bellowTheDiagonal.append(numbers)
    
    count += 1

    if count == 12:
        break

elementsSum = sum(bellowTheDiagonal)
elementsAverage = elementsSum/len(bellowTheDiagonal)

if O == 'S':
    print('%.1f'%elementsSum)

elif O == 'M':
    print('%.1f'%elementsAverage)
