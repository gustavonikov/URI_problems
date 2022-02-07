N, M = input().split()
N, M = int(N), int(M)

legibleFruits = []
illegibleFruits = []
fruitsThatSheldonLikes = set()

for fruit in range(N):
    legibleFruit = input().lower()
    legibleFruits.append(legibleFruit)

for encryptedWord in range(M):
    illegibleFruit = input().lower()
    illegibleFruits.append(illegibleFruit)

for fruitName in legibleFruits:
    reversedFruitName = fruitName[::-1]

    for illegibleFruit in illegibleFruits:
        if (fruitName in illegibleFruit) or (reversedFruitName in illegibleFruit):
            fruitsThatSheldonLikes.add(fruitName)

for fruit in legibleFruits:
    if fruit in fruitsThatSheldonLikes:
        print(f'Sheldon come a fruta {fruit}')
    else:
        print(f'Sheldon detesta a fruta {fruit}')
        