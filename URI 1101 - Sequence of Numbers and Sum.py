while True:
    M, N = input().split()
    M, N = int(M), int(N)

    if M <= 0 or N <= 0:
        break

    numbers = []
    numbers.append(M), numbers.append(N)
    numbers.sort()
    newNumbers = []
    
    for number in range(numbers[0], numbers[1] + 1):
        newNumbers.append(number)
    
    numbersSum = sum(newNumbers)
    print(*newNumbers, 'Sum=%i'%numbersSum)
    

