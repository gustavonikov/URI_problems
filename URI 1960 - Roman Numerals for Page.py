N = int(input())

romanNumberList = {
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}

result = ''

for number, romamNumber in romanNumberList.items():
    while N >= number:
        N -= number
        result += romamNumber

print(result)
