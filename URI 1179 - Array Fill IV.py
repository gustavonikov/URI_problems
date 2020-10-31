even = []

odd = []

for cases in range(0, 15):
    number = int(input())

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    
    if len(even) == 5:
        for index, evenNumber in enumerate(even):
            print(f'par[{index}] = {evenNumber}')
    
        even = []

    elif len(odd) == 5:
        for index, oddNumber in enumerate(odd):
            print(f'impar[{index}] = {oddNumber}')
    
        odd = []

for index, oddNumber in enumerate(odd):
    print(f'impar[{index}] = {oddNumber}')
for index, evenNumber in enumerate(even):
    print(f'par[{index}] = {evenNumber}')