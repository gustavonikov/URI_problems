N = int(input())

totalQuantity = 0
rabbits = 0
frogs = 0
mice = 0

for number in range(N):
    quantity, sort = input().split()
    totalQuantity += int(quantity)

    if sort == 'C':
        rabbits += int(quantity)
    if sort == 'S':
        frogs += int(quantity)
    if sort == 'R':
        mice += int(quantity)

rabbitsPercentage = (rabbits/totalQuantity) * 100
frogsPercentage = (frogs/totalQuantity) * 100
micePercentage = (mice/totalQuantity) * 100

print('Total: %i cobaias'%totalQuantity)
print('Total de coelhos: %i'%rabbits)
print('Total de ratos: %i'%mice)
print('Total de sapos: %i'%frogs)
print('Percentual de coelhos: %.2f'%rabbitsPercentage,'%')
print('Percentual de ratos: %.2f'%micePercentage,'%')
print('Percentual de sapos: %.2f'%frogsPercentage,'%')