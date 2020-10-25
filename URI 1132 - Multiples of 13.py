n1 = int(input())
n2 = int(input())

X, Y = 0, 0

if n1 > n2:
    X, Y = n2, n1
else:
    X, Y = n1, n2

numbersNotDivisiblePer13 = []

for number in range(X, Y + 1):
    if number % 13 != 0:
        numbersNotDivisiblePer13.append(number)

print(sum(numbersNotDivisiblePer13))