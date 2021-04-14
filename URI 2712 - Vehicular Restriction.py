N = int(input())

for plates in range(N):
    plate = input()

    if len(plate) != 8 or plate[3] != '-':
        print('FAILURE')
        continue

    isString, isUpper, isANumber = True, True, True

    firstPart, secondPart = plate.split('-')

    for letter in firstPart:
        if letter.isdigit():
            isString = False
            break

    isUpper = firstPart.isupper()
    isANumber = secondPart.isdigit()

    if isUpper == False or isANumber == False or isString == False:
        print('FAILURE')
        continue

    lastDigit = secondPart[3]
    lastDigit = int(lastDigit)

    if lastDigit == 1 or lastDigit == 2:
        print('MONDAY')
    elif lastDigit == 3 or lastDigit == 4:
        print('TUESDAY')
    elif lastDigit == 5 or lastDigit == 6:
        print('WEDNESDAY')
    elif lastDigit == 7 or lastDigit == 8:
        print('THURSDAY')
    elif lastDigit == 9 or lastDigit == 0:
        print('FRIDAY')
    