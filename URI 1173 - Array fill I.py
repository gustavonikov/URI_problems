V = int(input())

X = [V]
count = 1
number = V

while True:
    number *= 2
    X.append(number)

    count += 1

    if count == 10:
        break

for index, value in enumerate(X):
    print(f'N[{index}] = {value}')