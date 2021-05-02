while True:
    try:
        H, M = input().split()
        xValues = input().split()

        H, M = int(H), int(M)
        xValues = [float(value) for value in xValues]

        width = len(xValues)
        mean = sum(xValues) / width

        portions = []

        for value in xValues:
            portion = (value - mean)**2
            portions.append(portion)

        accuracy = (sum(portions)/(width - 1))**(1/2)

        print('{:.5f}'.format(accuracy))

    except EOFError:
        break