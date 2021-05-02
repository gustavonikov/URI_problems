E, D = input().split()

E, D = int(E), int(D)

if E > D or D >= 24:
    print('Eu odeio a professora!')
elif E <= 20:
    print('Muito bem! Apresenta antes do Natal!')
elif E >= 21:
    if D < 23:
        print('Parece o trabalho do meu filho!\nTCC Apresentado!')
    else:
        print('Parece o trabalho do meu filho!\nFail! Entao eh nataaaaal!')