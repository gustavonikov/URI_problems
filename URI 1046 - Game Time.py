times = input().split()

startTime = int(times[0])
endTime = int(times[1])

duration = endTime - startTime

if duration == 0:
    print('O JOGO DUROU 24 HORA(S)')
    
elif duration > 0:
    print('O JOGO DUROU %i HORA(S)'%duration)

elif duration < 0:
    duration += 24
    
    print('O JOGO DUROU %i HORA(S)'%duration)
