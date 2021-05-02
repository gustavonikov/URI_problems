N, G = input().split()

N, G = int(N), int(G)

runesCollection = {}

for test in range(N):
    rune, friendShipValue = input().split()

    friendShipValue = int(friendShipValue)

    runesCollection[rune] = friendShipValue

X = int(input())
runesRecited = input().split() 

count = 0

for rune in runesRecited:
    if rune in runesCollection:
        count += runesCollection[rune]

print(count)

if count >= G:
    print('You shall pass!')
else:
    print('My precioooous')
