numbers = []

for integers in range(0, 10):
    numbers.append(int(input()))

for index, number in enumerate(numbers):
    number = int(number)
    if number <= 0:
        number = 1
    
    print(f'X[{index}] = {number}')