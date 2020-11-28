while True:
    try:
        N = int(input())

        day = 0
        speedRecords = [0]
        daysOfTheRecords = []

        for runs in range(N):
            T, D = input().split()

            speed = int(D)/(int(T)/60)
            day += 1

            if speed > speedRecords[-1]:
                speedRecords.append(speed)
                daysOfTheRecords.append(day)

        for days in daysOfTheRecords:
            print(days)

    except EOFError:
        break