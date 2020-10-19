X = int(input())
Y = int(input())

oddNumbers = []

if X > Y:
    for numb in range(X, Y, -1)[1:]:
        if numb % 2 != 0:
            oddNumbers.append(numb)
else:
    for numb in range(X, Y)[1:]:
        if numb % 2 != 0:
            oddNumbers.append(numb)

print(sum(oddNumbers))