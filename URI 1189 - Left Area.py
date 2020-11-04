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
interval = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
count = 0

for lines in array[1:11]:
    for numbers in lines[:interval[count]]:
        aboveTheDiagonal.append(numbers)
    
    count +=1
    


elementsSum = sum(aboveTheDiagonal)
elementsAverage = elementsSum/len(aboveTheDiagonal)

if O == 'S':
    print('%.1f'%elementsSum)

elif O == 'M':
    print('%.1f'%elementsAverage)
