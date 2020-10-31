X = float(input())

N = []

for index, value in enumerate(range(0, 100)):
    nextNumber = 0
    if index == 0:
        N.append(X)
    else:
        nextNumber = N[-1]/2
        N.append(nextNumber)

    print('N[%i] = %.4f'%(index, N[index])) 