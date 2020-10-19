numbers = input().split()

originalNumbers = numbers

numbers = [int(i) for i in numbers]

numbers.sort()

for number in numbers:
    print(number)

print()

for number in originalNumbers:
    print(number)
