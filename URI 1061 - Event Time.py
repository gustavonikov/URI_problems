initialDayString = input().split()
initialTime = input().split(' : ')
finalDayString = input().split()
finalTime = input().split(' : ')

if initialDayString == '' or finalDayString == '' or initialTime == '' or finalTime== '':
    totalDays = 0
    totalHours = 0
    totalMinutes = 0
    totalSeconds = 0

else :

    initialDay = int(initialDayString[1])
    finalDay = int(finalDayString[1])

    initialHours, initialMinutes, initialSeconds = list(map(int, initialTime))
    finalHours, finalMinutes, finalSeconds = list(map(int, finalTime))
    
    totalDays = finalDay - initialDay
    totalHours = finalHours - initialHours
    totalMinutes = finalMinutes - initialMinutes
    totalSeconds = finalSeconds - initialSeconds
    
    if totalSeconds < 0:
        totalSeconds += 60
        totalMinutes -= 1

    if totalMinutes < 0:
        totalMinutes += 60
        totalHours -= 1

    if totalHours < 0:
        totalHours += 24
        totalDays -= 1

    if totalDays < 0:
        totalDays = 0

print('%i dia(s)'%totalDays)
print('%i hora(s)'%totalHours)
print('%i minuto(s)'%totalMinutes)
print('%i segundo(s)'%totalSeconds)