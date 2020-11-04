C = int(input())
T = input()
array = []

for lines in range(0, 12):
    arrayLine = []

    for numbers in range(0, 12):
        number = input()
        number = float(number)
        arrayLine.append(number)
    
    array.append(arrayLine)

columnNumbers = []

for columns in array:
    columnNumbers.append(columns[C])

sumOfColumn = sum(columnNumbers)

if T == 'S':
    print('%.1f'%sumOfColumn)

elif T == 'M':
    averageOfColumn = sumOfColumn/len(columnNumbers)
    print('%.1f'%averageOfColumn)
