dimensions = input().split()

A = float(dimensions[0])
B = float(dimensions[1])
C = float(dimensions[2])

triangleArea = (A * C)/2
circleArea = 3.14159 * C**2
trapeziumArea = ((A + B) * C)/2
squareArea = B * B
rectangleArea = A * B

print('TRIANGULO: %.3f'%(triangleArea))
print('CIRCULO: %.3f'%(circleArea))
print('TRAPEZIO: %.3f'%(trapeziumArea))
print('QUADRADO: %.3f'%(squareArea))
print('RETANGULO: %.3f'%(rectangleArea))