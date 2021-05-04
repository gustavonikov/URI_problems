N = int(input())

cars = 0
dolls = 0

for test in range(N):
    name, gender = input().split()

    if gender == 'F':
        dolls += 1
    else:
        cars += 1

print(f'{cars} carrinhos')
print(f'{dolls} bonecas')