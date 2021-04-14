top = []
lines = []
bottom = []

for dash in range(39):
    top.append('-')
    bottom.append('-')

for number in range(5):
    line = ['|']

    lines.append(line)

lines[0].insert(1, 'x = 35                               |')
lines[1].insert(1, '                                     |')
lines[2].insert(1, '               x = 35                |')
lines[3].insert(1, '                                     |')
lines[4].insert(1, '                               x = 35|')

print(*top, sep='')

for line in lines:
    print(*line, sep='')

print(*bottom, sep='')