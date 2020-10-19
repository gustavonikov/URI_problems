val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())

numbers = [val1, val2, val3, val4, val5]
evenNumbers = []
oddNumbers = []
positiveNumbers = []
negativeNumbers = []

for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(number)
    if number % 2 != 0:
        oddNumbers.append(number)
    if number > 0:
        positiveNumbers.append(number)
    if number < 0:
        negativeNumbers.append(number)

print(len(evenNumbers),'valor(es) par(es)')
print(len(oddNumbers),'valor(es) impar(es)')
print(len(positiveNumbers),'valor(es) positivo(s)')
print(len(negativeNumbers),'valor(es) negativo(s)')