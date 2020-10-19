val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())
val6 = float(input())

numbers = [val1, val2, val3, val4, val5, val6]
positiveNumbers = []

for number in numbers:
    if number > 0:
        positiveNumbers.append(number)

positiveNumbersQuantity = len(positiveNumbers)

print(positiveNumbersQuantity,'valores positivos')

average = sum(positiveNumbers)/ len(positiveNumbers)

print('%.1f'%average)