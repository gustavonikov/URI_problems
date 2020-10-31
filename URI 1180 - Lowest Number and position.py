N = int(input())

X = input().split()
X = [int(element) for element in X]

X_copy = X.copy()
X_copy.sort()

lowest_value = X_copy[0]
lowest_value_position = X.index(lowest_value)

print(f'Menor valor: {lowest_value}')
print(f'Posicao: {lowest_value_position}')