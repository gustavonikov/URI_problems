snowballs = input().split()
reindeers = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

snowballs = [int(snowball) for snowball in snowballs]
totalSnowballs = sum(snowballs)

while True:
    if (totalSnowballs - 9) > 0:
        totalSnowballs -= 9
    else:
        break

print(reindeers[totalSnowballs - 1])
