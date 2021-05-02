N = int(input())

hobbit, human, elf, dwarf, mage = 0, 0, 0, 0, 0

for test in range(N):
    name, race = input().split(maxsplit=2)

    if race == 'X':
        hobbit += 1
    elif race == 'H':
        human += 1
    elif race == 'E':
        elf += 1
    elif race == 'A':
        dwarf += 1
    elif race == 'M':
        mage += 1

print(f'{hobbit} Hobbit(s)')
print(f'{human} Humano(s)')
print(f'{elf} Elfo(s)')
print(f'{dwarf} Anao(s)')
print(f'{mage} Mago(s)')