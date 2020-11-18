p = int(input())
products = {
    '1001': 1.50,
    '1002': 2.50,
    '1003': 3.50,
    '1004': 4.50,
    '1005': 5.50,
}
totalPrice = 0

for product in range(p):
    productCode, q = input().split()
    q = int(q)

    for productNumber, value in products.items():
        if productCode == productNumber:
            shopPrice = q * value
            totalPrice += shopPrice

print('%.2f'%totalPrice)