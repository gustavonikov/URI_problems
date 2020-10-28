while True:
    X = int(input())

    if X == 0:
        break
    
    numbers = []

    if X % 2 == 0:
        for number in range(X, X + 10, 2):
            numbers.append(number)
    else:
        for number in range(X + 1, X + 10, 2):
            numbers.append(number)
    
    print(sum(numbers))