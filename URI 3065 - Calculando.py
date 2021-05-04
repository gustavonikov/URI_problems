test = 0

while True:
    m = int(input())
    test += 1

    if m == 0:
        break

    entry = input()

    newEntry = ''

    for index, digit in enumerate(entry):
        if 0 < index < (len(entry) - 1) and (entry[index - 1] == '+' or entry[index - 1] == '-') and digit == '0' and entry[index + 1].isdigit():
            newEntry += ''
        else:
            newEntry += digit

    result = eval(newEntry)

    print(f'Teste {test}\n{result}')
    print()