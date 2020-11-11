while True:
    try:
        L = int(input())

        numbers = input().split(maxsplit=L)

        numbers = [int(number) for number in numbers]

        numbers.sort(reverse=True)

        fastestSlugSpeed = numbers[0]
        level = 0

        if fastestSlugSpeed < 10:
            level = 1
        elif fastestSlugSpeed >= 10 and fastestSlugSpeed < 20:
            level = 2
        elif fastestSlugSpeed >= 20:
            level = 3
        
        print(level)

    except EOFError:
        break