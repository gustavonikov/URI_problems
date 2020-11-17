N = int(input())

sheepNumbers = input().split(maxsplit = N)
sheepNumbers = [int(sheep) for sheep in sheepNumbers]
sheepNumbers_copy = sheepNumbers.copy()

totalOfSheep = sum(sheepNumbers)
stolenSheep = 0
starsAttacked = []

for crescentIndex, sheep in enumerate(sheepNumbers):
    stolenSheep += 1
    sheepNumbers[crescentIndex] -= 1

    if sheep % 2 == 0:
        if crescentIndex == 0:
            break

        for decrescentIndex, sheep in enumerate(sheepNumbers[(crescentIndex - 1)::-1], -crescentIndex + 1):
            if sheep == 0:
                continue

            stolenSheep += 1
            sheepNumbers[abs(decrescentIndex)] -= 1

        break

for index, sheepCopies in enumerate(sheepNumbers_copy):
    if sheepCopies != sheepNumbers[index]:
        starsAttacked.append(1)

numberOfStarsAttacked = sum(starsAttacked)

print(numberOfStarsAttacked, totalOfSheep - stolenSheep)
