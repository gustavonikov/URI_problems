L = int(input())
C = int(input())

verticalType1 = L / 1
verticalType2 = (verticalType1 - 1) * 2
horizontalType1 = C / 1
horizontalType2 = (C - 1) * 2

print(int(verticalType1 * horizontalType1 + (verticalType1 - 1) * (horizontalType1 - 1)))
print(int(verticalType2 + horizontalType2))