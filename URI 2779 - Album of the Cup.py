N = int(input())
M = int(input())

stickers = set({})

for sticker in range(M):
    X = int(input())

    stickers.add(X)

missingCards = N - len(stickers)

print(missingCards)
