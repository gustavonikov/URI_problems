meetingTimeInMinutes = 480
busMaxTravelTime = 60

while True:
    try:
        hour, minutes = input().split(sep=':')
        hour, minutes = int(hour), int(minutes)
        hourInMinutes = hour * 60
        time = hourInMinutes + minutes
        

        if time + 60 > meetingTimeInMinutes:
            delay = (time + busMaxTravelTime) - meetingTimeInMinutes
            print(f'Atraso maximo: {delay}')
        else:
            print('Atraso maximo: 0')

    except EOFError:
        break