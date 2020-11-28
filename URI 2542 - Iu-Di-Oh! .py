while True:
    try:
        N = int(input())
        M, L = input().split()

        marcosCards = []
        leonardoCards = []

        for cards in range(int(M)):
            marcosCards.append(input().split(maxsplit = N)) 

        for cards in range(int(L)):
            leonardoCards.append(input().split(maxsplit = N))
        
        Cm, Cl = input().split()
        A = int(input())

        marcosPower = int(marcosCards[int(Cm) - 1][A - 1])
        leonardoPower = int(leonardoCards[int(Cl) - 1][A - 1])

        if marcosPower > leonardoPower:
            print('Marcos')
        elif marcosPower < leonardoPower:
            print('Leonardo')
        else:
            print('Empate')

    except EOFError:
        break