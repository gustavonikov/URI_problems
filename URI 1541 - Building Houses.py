while True:
    parameters = input().split()

    if parameters == ['0']:
        break

    A, B, C = parameters
    A, B, C = int(A), int(B), float(C)/100 
    
    houseSize = A * B
    sizeLand = (houseSize * 1)/C
    houseRealSize = int(sizeLand**(1/2))

    print(houseRealSize)
