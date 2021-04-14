top = []
lines = []
bottom = []

for dash in range(39):
    top.append('-')
    bottom.append('-')

for number in range(5):
    line = ['|', '|']

    for verticalSlash in range(36):
        line.insert(1, '')

    lines.append(line)

print(*top, sep='')

for line in lines:
    print(*line)

print(*bottom, sep='')