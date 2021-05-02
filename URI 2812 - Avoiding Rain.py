N = int(input())

umbrellasInHome, umbrellasInOffice = 0, 0
accumInHome, accumInOffice = 0, 0

for test in range(N):
    sd, sn = input().split()

    if sd == 'sol' and sn == 'chuva':
        if accumInOffice == 0:
            umbrellasInOffice += 1
        else:
            accumInOffice -= 1
        accumInHome += 1
    elif sd == 'chuva' and sn == 'sol':
        if accumInHome == 0:
            umbrellasInHome += 1
        else:
            accumInHome -= 1
        accumInOffice += 1
    elif sd == 'chuva' and sn == 'chuva':
        if accumInHome == 0:
            umbrellasInHome += 1
        else:
            accumInHome -= 1
        accumInHome += 1

print(umbrellasInHome, umbrellasInOffice)