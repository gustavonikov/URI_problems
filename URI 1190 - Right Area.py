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
interval = [11, 10, 9, 8, 7, 7, 8, 9, 10, 11]
count = 0

for lines in array[1:11]:
    for numbers in lines[interval[count]:]:
        aboveTheDiagonal.append(numbers)
    
    count +=1
    
elementsSum = sum(aboveTheDiagonal)
elementsAverage = elementsSum/len(aboveTheDiagonal)

if O == 'S':
    print('%.1f'%elementsSum)

elif O == 'M':
    print('%.1f'%elementsAverage)
