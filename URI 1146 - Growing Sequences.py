while True:
    X = int(input())

    if X == 0:
        break

    numbers = []

    for number in range(1, X + 1):
        numbers.append(number)
    
    print(*numbers)