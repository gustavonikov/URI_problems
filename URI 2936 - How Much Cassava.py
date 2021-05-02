portions = {
    "Curupira": 300,
    "Boitata": 1500,
    "Boto": 600,
    "Mapinguari": 1000,
    "Iara": 150
}

cassavaGrams = 225

for value in portions.values():
    portion = int(input())

    result = value * portion
    cassavaGrams += result

print(cassavaGrams)