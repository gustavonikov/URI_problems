N = int(input())

lastHo = 'Ho!'

howManyHo = ''

for Hos in range(N-1):
    howManyHo += 'Ho '

howManyHo += lastHo
print(howManyHo)