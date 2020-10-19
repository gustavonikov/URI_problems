product1 = input().split()
product2 = input().split()

convertedProduct1 = [float(i) if '.' in i else int(i) for i in product1]
convertedProduct2 = [float(i) if '.' in i else int(i) for i in product2]

code1, quantity1, priceForUnit1 = convertedProduct1
code2, quantity2, priceForUnit2 = convertedProduct2

valueToPay = (quantity1 * priceForUnit1) + ( quantity2 * priceForUnit2)

print('VALOR A PAGAR: R$ %.2f'%(valueToPay))