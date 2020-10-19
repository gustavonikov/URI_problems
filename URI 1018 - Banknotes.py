N = int(input())

banknotes = [100, 50, 20, 10, 5, 2, 1]

print(N)

for x in banknotes:
    
    numberOfBankNotes = int(N/x)
    
    print ("%i nota(s) de R$ %i,00"%(numberOfBankNotes,x))

    N %= (x)  