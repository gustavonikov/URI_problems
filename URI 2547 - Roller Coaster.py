while True:
    try:
        N, Amin, Amax = input().split()

        guestsAllowed = 0

        for guests in range(int(N)):
            guestHeight = int(input())
            if guestHeight >= int(Amin) and guestHeight <= int(Amax):
                guestsAllowed += 1
        
        print(guestsAllowed)

    except EOFError:
        break