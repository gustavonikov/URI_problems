X = int(input())

while True:
    Z = int(input())

    if Z > X:
        break

numbers = []

for number in range(X, Z):
    numbers.append(number)

    if sum(numbers) > Z:
        print(len(numbers))
        break