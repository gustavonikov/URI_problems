while True:
    try:
        alphabet = input()
        N = int(input())
        bulbsBlinked = input().split(maxsplit=N)
        bulbsBlinked = [int(bulb) for bulb in bulbsBlinked]

        message = ''

        for bulb in bulbsBlinked:
            message += alphabet[bulb - 1]

        print(message)

    except EOFError:
        break