T = int(input())

for cases in range(T):
    B = int(input())
    Ad, Dd, Ld = input().split()
    Ag, Dg, Lg = input().split()
    Ad, Dd, Ld = int(Ad), int(Dd), int(Ld)
    Ag, Dg, Lg = int(Ag), int(Dg), int(Lg)

    dabrielBonus = 0
    guarteBonus = 0

    if Ld % 2 == 0:
        dabrielBonus = B
    if Lg % 2 == 0:
        guarteBonus = B

    dabrielPokemonValue =  ((Ad + Dd)/2) + dabrielBonus
    guartePokemonValue =  ((Ag + Dg)/2) + guarteBonus

    if dabrielPokemonValue > guartePokemonValue:
        print('Dabriel')
    elif guartePokemonValue > dabrielPokemonValue:
        print('Guarte')
    else:
        print('Empate')