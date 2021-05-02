while True:
    try:
        T = int(input())

        dailyBattery = []

        for test in range(T):
            dailyBattery.append(float(input()))

        print(min(dailyBattery))

    except EOFError:
        break