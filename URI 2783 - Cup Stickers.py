N, C, M = input().split()
X = input().split()
Y = input().split()

N, C = int(N), int(C)
stampedStickers = N - C
missingStickers = N - stampedStickers
purchasedStickers = set(Y)

for sticker in purchasedStickers:
    if X.__contains__(sticker): missingStickers -= 1

print(missingStickers)