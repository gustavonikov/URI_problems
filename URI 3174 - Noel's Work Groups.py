n = int(input())
gifts = 0
dollsCompTime = 0
architectsCompTime = 0
musiciansCompTime = 0
drawnersCompTime = 0

for elf in range(n):
    elfName, group, hoursOfWork = input().split()
    hoursOfWork = int(hoursOfWork)

    if group == 'bonecos':
        dolls = hoursOfWork//8
        dollsCompTime += hoursOfWork - (dolls * 8)
        gifts += dolls
    elif group == 'arquitetos':
        architects = hoursOfWork//4
        architectsCompTime += hoursOfWork - (architects * 4)
        gifts += architects
    elif group == 'musicos':
        musicians = hoursOfWork//6
        musiciansCompTime += hoursOfWork - (musicians * 6)
        gifts += musicians
    elif group == 'desenhistas':
        drawners =  hoursOfWork//12
        drawnersCompTime += hoursOfWork - (drawners * 12)
        gifts += drawners

dollsResult = dollsCompTime // 8
architectsResult = architectsCompTime // 4
musiciansResult = musiciansCompTime // 6
drawnersResult = drawnersCompTime // 12

result = gifts + dollsResult + architectsResult + musiciansResult + drawnersResult
print(result)
