L = int(input())
T = input()
array = []

for lines in range(0, 12):
    arrayLine = []

    for numbers in range(0, 12):
        number = input()
        number = float(number)
        arrayLine.append(number)
    
    array.append(arrayLine)

sumOfLine = sum(array[L])

if T == 'S':
    print('%.1f'%sumOfLine)

elif T == 'M':
    averageOfLine = sumOfLine/len(array[L])
    print('%.1f'%averageOfLine)
