val1 = float(input())
val2 = float(input())
val3 = float(input())
val4 = float(input())
val5 = float(input())

numbers = [val1, val2, val3, val4, val5]
evenNumbers = []

for number in numbers:
    if number % 2 == 0:
        evenNumbers.append(number)

print(len(evenNumbers),'valores pares')