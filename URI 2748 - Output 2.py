top = []
lines = []
bottom = []

for dash in range(39):
    top.append('-')
    bottom.append('-')

for number in range(5):
    line = ['|', '|']

    for verticalSlash in range(28):
        line.insert(1, '')

    lines.append(line)

lines[0].insert(8, 'Roberto')
lines[1].insert(8, '       ')
lines[2].insert(8, '5786   ')
lines[3].insert(8, '       ')
lines[4].insert(8, 'UNIFEI ')

print(*top, sep='')

for line in lines:
    print(*line)

print(*bottom, sep='')