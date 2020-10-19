hundredNumbers = []

for numb in range(0,100):
    number = int(input())
    
    hundredNumbers.append(number)
    
hundredNumbersCopy = list(hundredNumbers)
hundredNumbers.sort(reverse = True)

highestValue = hundredNumbers[0]
highestValueIndex = hundredNumbersCopy.index(highestValue) + 1

print(highestValue)
print(highestValueIndex)