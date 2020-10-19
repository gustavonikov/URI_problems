N = int(input())

insertedNumbers = []

def ClassifyNumber(Array):
    for X in Array:
        if X == 0:
            print('NULL')
        
        if X < 0:
            if X % 2 == 0:
                print('EVEN NEGATIVE')
            else:
                print('ODD NEGATIVE')
        elif X > 0:
            if X % 2 != 0:
                print('ODD POSITIVE')
            else:
                print('EVEN POSITIVE')

for number in range(N):
    
    X = int(input())
    insertedNumbers.append(X)

ClassifyNumber(insertedNumbers)