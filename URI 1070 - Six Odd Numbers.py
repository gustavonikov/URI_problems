number = int(input())

numberPlus1 = number + 1
numberPlus12 = number + 12

if number % 2 == 0:
    for numb in range(numberPlus1, numberPlus12, 2):
        print(numb)       
else:
    for numb in range(number, numberPlus12, 2):
        print(numb)