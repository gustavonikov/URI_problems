T = int(input())

for interval in range(0, T):
    PA, PB, G1, G2 = input().split()
    PA, PB, G1, G2 = int(PA), int(PB), float(G1,), float(G2)

    years = 0

    while PA <= PB:
        PA = PA + int(PA * (G1/100))
        PB = PB + int(PB * (G2/100))

        years += 1
        
        if years > 100:
            break

    if years > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{years} anos.')
        