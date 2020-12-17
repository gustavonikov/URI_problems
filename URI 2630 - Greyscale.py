T = int(input())

casesCount = 0

for cases in range(T):
    casesCount += 1
    method = input()
    values = input().split()
    values = [int(value) for value in values]

    if method == 'min':
        values.sort()
        print(f'Caso #{casesCount}: {values[0]}')
    elif method == 'max':
        values.sort(reverse=True)
        print(f'Caso #{casesCount}: {values[0]}')
    elif method == 'mean':
        p = (values[0] + values[1] + values [2])/3
        print(f'Caso #{casesCount}: {int(p)}')
    elif method == 'eye':
        p = 0.3 * values[0] + 0.59 * values[1] + 0.11 * values[2]
        print(f'Caso #{casesCount}: {int(p)}')