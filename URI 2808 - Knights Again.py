initialPosition, lastPosition = input().split()

x1 = ((int(lastPosition[1])) - (int(initialPosition[1])))**(2) 
x2 =  ((ord(lastPosition[0]) - 96) - (ord(initialPosition[0]) - 96))**(2)

result = round((x1 + x2)**(1/2), 2)

if result != 2.24:
    print('INVALIDO')
else:
    print('VALIDO')
