def reduce(index, iterable):
    total = 0
    total += reduce(index + 1, iterable)
    return total

while True:
    try:
        N = int(input())
        e1, e2 = input().split(maxsplit=2)
        stepLine1 = input().split(maxsplit=N)
        stepLine2 = input().split(maxsplit=N)
        timeToSwitch1 = input().split(maxsplit=(N-1))
        timeToSwitch2 = input().split(maxsplit=(N-1))
        x1, x2 = input().split(maxsplit=2)

        e1, e2 = int(e1), int(e2)
        stepLine1 = [int(step) for step in stepLine1]
        stepLine2 = [int(step) for step in stepLine2]
        timeToSwitch1 = [int(step) for step in timeToSwitch1]
        timeToSwitch2 = [int(step) for step in timeToSwitch2]
        stepLine1Switch = []
        stepLine2Switch = []
        x1, x2 = int(x1), int(x2)

        total = 0

        for index, step in enumerate(range(0, N - 1)):
            value = timeToSwitch1[index] + stepLine2[index + 1]
            stepLine1Switch.append(value)

        for index, step in enumerate(range(0, N - 1)):
            value = timeToSwitch2[index] + stepLine1[index + 1]
            stepLine2Switch.append(value)

        for index, step in enumerate(range(N)):
            total = reduce(index, stepLine1)
        
        print(total)
    except EOFError:
        break