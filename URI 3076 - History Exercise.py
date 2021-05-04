while True:
    try:
        N = int(input())

        quotient = N/100

        century = 0

        if int(quotient) == float(quotient):
            century = int(quotient)
        else:
            century = int(quotient) + 1
        
        print(century)
        
    except EOFError:
        break