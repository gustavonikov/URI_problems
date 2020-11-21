N = int(input())

numbers = input().split(maxsplit = N)
numbers = [int(number) for number in numbers]

multipleOf2 = 0
multipleOf3 = 0
multipleOf4 = 0
multipleOf5 = 0

for number in numbers:
    if number % 2 == 0:
        multipleOf2 += 1
    if number % 3 == 0:
        multipleOf3 += 1
    if number % 4 == 0:
        multipleOf4 += 1
    if number % 5 == 0:
        multipleOf5 += 1

print(f'{multipleOf2} Multiplo(s) de 2')
print(f'{multipleOf3} Multiplo(s) de 3')
print(f'{multipleOf4} Multiplo(s) de 4')
print(f'{multipleOf5} Multiplo(s) de 5')