while True:
    try:
        N = int(input())

        ninjas = 1
        howManyTimesWasUsedTheJutsu = 0

        while ninjas < N:
            ninjas *= 2
            howManyTimesWasUsedTheJutsu += 1
        
        print(howManyTimesWasUsedTheJutsu)

    except EOFError:
        break