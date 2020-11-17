QT = int(input())

for cases in range(QT):
    nameAndChoice = input().split()
    firstPersonName = nameAndChoice[0]
    firstPersonChoice = nameAndChoice[1]
    secondPersonName = nameAndChoice[2]
    secondPersonChoice = nameAndChoice[3]
    N, M = input().split()
    N, M = int(N), int(M)

    sumResult = N + M
    theSumIsEvenOrOdd = ''

    if sumResult % 2 == 0:
        theSumIsEvenOrOdd = 'PAR'
    else:
        theSumIsEvenOrOdd = 'IMPAR'
    
    if theSumIsEvenOrOdd == firstPersonChoice:
        print(firstPersonName)
    else:
        print(secondPersonName)
