N = int(input())

for number in range(0, N + 1, 2)[1:]:
    square = number**2
    print('%i^2 = %i'%(number,square))