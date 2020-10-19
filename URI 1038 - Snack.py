productBuyInfo = input().split()

X, Y = productBuyInfo

productsPrices = { 1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50 }
    
for code, price in productsPrices.items():
    if int(X) == code:
        valueToPay = price * int(Y)

        print('Total: R$ %.2f'%valueToPay)