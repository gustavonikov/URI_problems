N = float(input())

valores = [100.00,50.00,20.00,10.00,5.00,2.00, 1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")

for x in valores:

    if x > 1.00:

        print ("%i nota(s) de R$ %.2f"%((N/x), x))

        N %= x   
        N = round(N, 2)

print("MOEDAS:")

for x in valores:

    if x <= 1.00:

        print("%i moeda(s) de R$ %.2f"%((N/x), x))

        N %= x
        N = round(N, 2)

        

