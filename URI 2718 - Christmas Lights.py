N = int(input())

for X in range(N):
    X = int(input())

    binary = bin(X)
    count = 0
    accumulator = 0

    for number in binary:
        if number == '1':
            accumulator += 1
        else:
            accumulator = 0
        
        if accumulator > count:
            count = accumulator
    
    print(count)