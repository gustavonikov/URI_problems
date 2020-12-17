C = int(input())

songs = {
    0: 'PROXYCITY',
    1: 'P.Y.N.G.',
    2: 'DNSUEY!',
    3: 'SERVERS',
    4: 'HOST!',
    5: 'CRIPTONIZE',
    6: 'OFFLINE DAY',
    7: 'SALT',
    8: 'ANSWER!',
    9: 'RAR?',
    10: 'WIFI ANTENNAS',
}

for cases in range(C):
    X, Y = input().split()

    for number, music in songs.items():
        if number == (int(X) + int(Y)):
            print(music)