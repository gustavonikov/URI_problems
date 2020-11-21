bills = [2, 5, 10, 20, 50, 100]

while True:
    N, M = input().split()
    N, M = int(N), int(M)

    if N == 0 and M == 0:
        break

    difference = M - N
    possible = False

    for index, bill in enumerate(bills[:5]):
        for bill2 in bills[index + 1:]:
            if bill + bill2 == difference:
                possible = True
                break
        
        if possible == True:
            break
    
    if possible == True:
        print('possible')
    else:
        print('impossible')
