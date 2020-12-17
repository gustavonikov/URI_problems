import math

while True:
    def secondsToMoments(M):
        conversionCoefficient = 0.0041666667
        momentInSeconds = round(M/conversionCoefficient) + 21600
        minutesAndSeconds, hours = math.modf(momentInSeconds/3600)
        minutesAndSeconds = round(minutesAndSeconds * 3600, 2)
        seconds, minutes = math.modf(minutesAndSeconds/60)
        seconds = round(seconds * 60, 2)

        if int(hours) >= 24:
            hours -= 24

        hours, minutes, seconds = str(int(hours)), str(int(minutes)), str(int(seconds))
        
        if len(hours) < 2:
            hours = '0' + hours
        if len(minutes) < 2:
            minutes = '0' + minutes
        if len(seconds) < 2:
            seconds = '0' + seconds

        moment = f'{hours}:{minutes}:{seconds}'
        return moment

    try:
        M = float(input())

        if M == 360:
            M = 0

        if M >= 0 and M < 90:
            moment = secondsToMoments(M)
            print('Bom Dia!!')
            print(moment)
        elif M >= 90 and M < 180:
            moment = secondsToMoments(M)
            print('Boa Tarde!!')
            print(moment)
        elif M >= 180 and M < 270:
            moment = secondsToMoments(M)
            print('Boa Noite!!')
            print(moment)
        elif M >= 270 and M < 360:
            moment = secondsToMoments(M)
            print('De Madrugada!!')
            print(moment)

    except EOFError:
        break