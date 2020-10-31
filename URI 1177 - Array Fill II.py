T = int(input())

N = [value for value in range(0, T)]

N.__imul__(500)

while True:
    for index, value in enumerate(N):
        if index == 1000:
            break

        print(f'N[{index}] = {value}') 
    break 