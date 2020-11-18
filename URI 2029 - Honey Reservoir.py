while True:
    
    try:
        V = float(input())
        D = float(input())

        height = V/(3.14 * (D/2)**2)
        area = V/height

        print('ALTURA = %.2f'%height)
        print('AREA = {:.2f}'.format(area))

    except EOFError:
        break